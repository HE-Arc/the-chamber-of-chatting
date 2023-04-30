import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import CreateTopicView from "../views/CreateTopicView.vue";
import LoginView from "../views/LoginView.vue";
import RegiterView from "../views/RegisterView.vue";
import TopicView from "../views/TopicView.vue";
import ReplayView from "../views/ReplayView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/topics/create",
      name: "topics.create",
      component: CreateTopicView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "register",
      component: RegiterView,
    },
    {
      path: "/topics/:id",
      name: "topics.show",
      component: TopicView,
    },
    {
      path: "/about",
      name: "about",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/AboutView.vue"),
    },
    {
      path: "/topics/:id/reply",
      name: "topics.reply",
      component: ReplayView,
    },
  ],
});

export default router;
