<script setup>
import axios from "axios";
import { ref } from "vue";

const name = ref("");
const submit = async () => {
  try {
    errors.value = null;
    success.value = false;
    await axios.post("/topics/", {
      topic_name: name.value,
    });
    success.value = true;
  } catch (error) {
    errors.value = error.response.data;
  }
};

const errors = ref(null);
const success = ref(null);
</script>

<template>
  {{ errors }}
  <q-page padding>
    <q-btn color="primary" :to="{ name: 'home' }">
      <q-icon left name="arrow_back" />
      Back
    </q-btn>
    <div class="q-pa-md bg-white" style="max-width: 400px">
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
    </div>
  </q-page>
</template>
