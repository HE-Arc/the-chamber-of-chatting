<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const topics = ref([]);

const fetchTopics = async () => {
  const response = await axios.get("/topics/");
  topics.value = response.data;
};
const name = ref("");
const submit = async () => {
  try {
    await axios.post("/topics/", {
      topic_name: name.value,
    });
    name.value = null;
    fetchTopics();
  } catch (error) {
    errors.value = error.response.data;
  }
};

const errors = ref(null);

onMounted(() => {
  fetchTopics();
});
</script>

<template>
  {{ errors }}
  <q-page padding>
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
      </q-form>
    </div>
    <q-list bordered>
      <q-item v-for="topic in topics" :key="topic.id">
        <q-item-section>
          <q-item-label>{{ topic.topic_name }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </q-page>
</template>
