# config valid for current version and patch releases of Capistrano
lock "~> 3.17.2"

set :application, "the_chamber_of_chatting"
set :repo_url, "git@github.com:HE-Arc/the-chamber-of-chatting.git"


# Default branch is :master
# ask :branch, `git rev-parse --abbrev-ref HEAD`.chomp

# Default deploy_to directory is /var/www/my_app_name
# set :deploy_to, "/var/www/my_app_name"

# Default value for :format is :airbrussh.
# set :format, :airbrussh

# You can configure the Airbrussh format using :format_options.
# These are the defaults.
# set :format_options, command_output: true, log_file: "log/capistrano.log", color: :auto, truncate: :auto

# Default value for :pty is false
# set :pty, true

# Default value for :linked_files is []
# append :linked_files, "config/database.yml", 'config/master.key'

# Default value for linked_dirs is []
# append :linked_dirs, "log", "tmp/pids", "tmp/cache", "tmp/sockets", "tmp/webpacker", "public/system", "vendor", "storage"

# Default value for default_env is {}
# set :default_env, { path: "/opt/ruby/bin:$PATH" }

# Default value for local_user is ENV['USER']
# set :local_user, -> { `git config user.name`.chomp }

# Default value for keep_releases is 5
# set :keep_releases, 5

# Uncomment the following to require manually verifying the host key before first deploy.
# set :ssh_options, verify_host_key: :secure

after 'deploy:updating', 'pip:install'

namespace :pip do
    desc 'Install pip packages'
    task :install do
        on roles([:app, :web]) do |h|
            execute "pip install -r #{release_path}/api/requirements.txt"
        end
    end
end

after 'pip:install', 'npm:install'
namespace :npm do
    desc 'Install npm packages'
    task :install do
        on roles([:app, :web]) do |h|
            execute "cd #{release_path}/frontend && npm install"
        end
    end
end

after 'deploy:publishing',  'django:migrate'

namespace :django do
    desc 'Migrate'
    task :migrate do
        on roles(:web) do |h|
            execute "python3 #{release_path}/api/manage.py migrate"
        end
    end
end

after 'django:migrate', 'django:collectstatic'
namespace :django do
    desc 'Collect static files'
    task :collectstatic do
        on roles(:web) do |h|
            execute "python3 #{release_path}/api/manage.py collectstatic --noinput"
        end
    end
end

after 'django:collectstatic', 'gunicorn:restart'

namespace :gunicorn do
    desc 'Restart application'
    task :restart do
        on roles(:web) do |h|
            execute :sudo, "systemctl restart gunicorn"
        end
    end
end

after 'gunicorn:restart', 'vue:build'

namespace :vue do
    desc 'Build vue'
    task :build do
        on roles(:web) do |h|
            execute "cd #{release_path}/frontend && npm run build"
        end
    end
end




