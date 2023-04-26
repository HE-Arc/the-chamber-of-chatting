<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import moment from "moment";

import router from "../router";

const topic = ref(null);
const route = useRoute();

const fetchTopic = async () => {
  const response = await axios.get("/topics/" + route.params.id + "/");
  topic.value = response.data;
};

onMounted(() => {
  fetchTopic();
});
</script>

<template>
  <q-page padding>
    <q-btn color="blue-grey-8" @click="router.back()">
      <q-icon left name="arrow_back" />
      <div>Back</div>
    </q-btn>
    <div class="row self-center justify-evenly">
      <div class="col-12 q-mt-md">
        <q-card class="q-pa-lg">
          <q-card-section class="text-center">
            <div class="text-h5">{{ topic.topic_name }}</div>
          </q-card-section>
          <div class="q-pa-md row justify-center">
            <div style="width: 100%">
              <q-chat-message
                v-for="msg in topic.messages"
                :key="msg.id"
                :name="[msg.user_id.username]"
                :text="[msg.message]"
                :stamp="[moment(msg.created).fromNow()]"
                text-color="white"
                bg-color="blue-grey-8"
              />
            </div>
            <!-- ajouter un v-if pour mettre le "sent" quand c'est nos messages -->
          </div>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<style scoped></style>
