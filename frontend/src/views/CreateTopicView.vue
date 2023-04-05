<script setup>
import axios from "axios";
import { ref } from "vue";

import router from "../router";

const name = ref("");
const submit = async () => {
  try {
    errors.value = null;
    success.value = false;
    await axios.post("/topics/", {
      topic_name: name.value,
      message: [],
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
  {{ errors }}
  <q-page padding>
    <div class="row self-center justify-evenly">
      <div class="col-8 q-mt-md">
        <q-btn color="primary" @click="this.$router.back()">
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
            <div>
              <q-btn label="Submit" type="submit" color="primary" />
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
