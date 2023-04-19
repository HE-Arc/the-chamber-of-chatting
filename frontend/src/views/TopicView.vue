<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const topic = ref([]);
const route = useRoute();

const fetchTopic = async () => {
  const response = await axios.get("/topics/" + route.params.id);
  topic.value = response.data;
};

onMounted(() => {
  fetchTopic();
});
</script>

<template>
  <q-page padding>
    <q-btn color="primary" @click="this.$router.back()">
      <q-icon left name="arrow_back" />
      <div>Back</div>
    </q-btn>
    <div class="row self-center justify-evenly">
      <div class="col-12 q-mt-md">
        <q-card class="q-pa-lg">
          <q-card-section class="text-center">
            <div class="text-h5">{{ topic.topic_name }}</div>
          </q-card-section>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<style scoped></style>
