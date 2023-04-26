<script setup>
import axios from "axios";
import { ref } from "vue";

import router from "../router";

const username = ref("");
const password = ref("");



const submit = async () => {
  try {
    errors.value = null;
    success.value = false;
    await axios.post("users/login/", {
      username: username.value,
      password: password.value,
    });
    success.value = true;
  } catch (error) {
    errors.value = error.response.data;
  }
  router.push({ name: "home" });
};

const errors = ref(null);
const success = ref(null);
</script>

<template>
  <q-page padding>
    <div class="row self-center justify-evenly">
      <div class="col-6 q-mt-md">
        <q-btn color="blue-grey-8" @click="this.$router.back()">
          <q-icon left name="arrow_back" />
          <div>Back</div>
        </q-btn>
      </div>
    </div>
    <div class="row self-center justify-evenly">
      <div class="col-6 q-mt-md">
        <q-card class="q-pa-lg">
          <q-card-section class="text-center">
            <div class="text-h5">Login</div>
          </q-card-section>

          <q-form @submit="submit()" class="q-gutter-md">
            <q-input
              filled
              v-model="username"
              label="username"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'User name is requiered',
              ]"
            />
            <q-input
              type="password"
              filled
              v-model="password"
              label="password"
              lazy-rules
              :rules="[
                (val) => (val && val.length > 0) || 'Password is requiered',
              ]"
            />
            <div>
              <q-btn label="Submit" type="submit" color="blue-grey-8" />
            </div>
            <q-banner
              v-if="success"
              inline-actions
              class="q-mb-lg text-white bg-green"
            >
              <div class="text-h6">
                <q-icon left size="md" name="mdi-check-circle-outline" />
                Login successfull
              </div>
            </q-banner>
          </q-form>
          <router-link to="/register">Register</router-link>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<style scoped></style>
