<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";

const topics = ref([]);

const fetchTopics = async () => {
  const response = await axios.get("/topics/");
  topics.value = response.data;
};

onMounted(() => {
  fetchTopics();
});
</script>

<template>
  <q-page padding>
    <q-btn color="primary" :to="{ name: 'topics.create' }"> New Topic </q-btn>
    <q-list bordered>
      <q-item v-for="topic in topics" :key="topic.id">
        <q-item-section>
          <q-item-label>{{ topic.topic_name }}</q-item-label>
        </q-item-section>
      </q-item>
    </q-list>
  </q-page>
</template>
