<script setup>
import axios from "axios";
import { ref } from "vue";

import router from "../router";

const name = ref("");
const message = ref("");
const submit = async () => {
  try {
    errors.value = null;
    success.value = false;
    let user = await axios.get("/users/current_user/");
    const userUrl =
      axios.defaults.baseURL + "/users/" + user.data.user_id + "/";
    const topic = await axios.post("/topics/", {
      user_id: userUrl,
      topic_name: name.value,
      messages: [],
    });
    await axios.post("/messages/", {
      user_id: userUrl,
      topic_id: topic.data.url,
      message: message.value,
    });

    success.value = true;
    router.push({ name: "home" });
  } catch (error) {
    console.log(error);
    if (error.response.status == 403) {
      errors.value = "You are not logged in. Please log in to create a topic.";
    } else {
      errors.value = error.response.data;
    }
  }
};

const errors = ref(null);
const success = ref(null);
</script>

<template>
  {{ errors }}
  <q-page padding>
    <div class="row self-center justify-evenly">
      <div class="col-8 q-mt-md">
        <q-btn color="blue-grey-8" @click="router.back()">
          <q-icon left name="arrow_back" />
          <div>Back</div>
        </q-btn>
      </div>
    </div>
    <div class="row self-center justify-evenly">
      <div class="col-8 q-mt-md">
        <q-card class="q-pa-lg">
          <q-form @submit="submit()" class="q-gutter-md">
            <q-input
              filled
              v-model="name"
              label="Topic Name *"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length > 0) || 'Please give a name to your topic',
              ]"
            />
            <q-input
              filled
              v-model="message"
              label="Message *"
              lazy-rules
              :rules="[
                (val) =>
                  (val && val.length > 0) ||
                  'Please give a message to your topic',
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
                New Topic created!
              </div>
            </q-banner>
          </q-form>
        </q-card>
      </div>
    </div>
  </q-page>
</template>
