<script setup>
import axios from "axios";
import { onMounted, ref } from "vue";

const user = ref(null);

const logOut = () => {
  axios.post("users/logout/");
  user.value = null;
};

const adminURL = ref(axios.defaults.baseURL + "/admin/");

const getCurrentUser = async () => {
  try {
    const response = await axios.get("users/current_user/", {
      withCredentials: true,
    });
    if (response.status === 200) {
      user.value = response.data;
    }
  } catch (error) {
    if (error.response.status === 403) {
      /* empty, avoid console spaming without logged user */
    } else {
      console.log(error);
    }
  }
};

onMounted(() => {
  getCurrentUser();
});
</script>

<template>
  <q-header reveal elevated class="bg-grey-10 text-white" height-hint="98">
    <q-toolbar>
      <q-icon name="question_answer" size="xl"></q-icon>
      <q-toolbar-title> The Chamber of Chatting </q-toolbar-title>
    </q-toolbar>
    <q-tabs align="left">
      <q-route-tab :to="{ name: 'home' }" label="Home" />
      <q-route-tab :to="{ name: 'topics.create' }" label="New Topic" />
      <q-route-tab :to="{ name: 'about' }" label="About" />
      <q-space />
      <q-route-tab v-if="user?.is_admin" :href="adminURL" label="Admin Panel" />
      <q-tab v-if="user" :label="user.username" />
      <q-route-tab v-else :to="{ name: 'login' }" label="login" />
      <q-route-tab
        v-if="user"
        :to="{ name: 'logout' }"
        label="logout"
        @click="logOut()"
      />
      <q-route-tab v-else :to="{ name: 'register' }" label="register" />
    </q-tabs>
  </q-header>
</template>

<style scoped></style>
