<script setup>
import axios from "axios";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import moment from "moment";

import router from "../router";

const topic = ref(null);
const route = useRoute();

const fetchTopic = async () => {
  try {
    const response = await axios.get("/topics/" + route.params.id + "/");
    topic.value = response.data;
  } catch (error) {
    console.log(error);
  }
};

const user = ref(null);
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

const isSender = (msg) => {
  return msg.user_id.id == user?.value.id;
};

onMounted(() => {
  fetchTopic();
  getCurrentUser();
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
                :sent="[isSender(msg)]"
                :stamp="[moment(msg.created).fromNow()]"
                text-color="white"
                bg-color="blue-grey-8"
              />
            </div>
            <!-- ajouter un v-if pour mettre le "sent" quand c'est nos messages -->
          </div>
        </q-card>
        <q-btn
          color="blue-grey-8"
          :to="{ name: 'topics.reply', params: { id: topic.id } }"
        >
          <q-icon left name="reply" />
          <div>Reply</div>
        </q-btn>
      </div>
    </div>
  </q-page>
</template>

<style scoped></style>
