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
  {{ errors }}
  <q-page padding>
    <div class="row self-center justify-evenly">
      <div class="col-12 q-mt-md">
        <q-btn color="blue-grey-8" :to="{ name: 'topics.create' }">
          New Topic
        </q-btn>
      </div>
    </div>
    <div class="row self-center justify-evenly">
      <div class="col-12 q-mt-md">
        <q-card class="q-pa-lg">
          <q-list bordered>
            <q-item v-for="topic in topics" :key="topic.id">
              <q-item-section>
                <q-btn
                  rounded
                  outline
                  color="blue-grey-8"
                  v-bind:id="topic.id"
                  :to="{ name: 'topics.show', params: { id: topic.id } }"
                  >{{ topic.topic_name }}</q-btn
                >
              </q-item-section>
            </q-item>
          </q-list>
        </q-card>
      </div>
    </div>
  </q-page>
</template>
