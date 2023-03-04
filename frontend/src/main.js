import { createApp } from "vue";
import { Quasar } from "quasar";
import App from "./App.vue";
import router from "./router";

import "./assets/main.css";

import "@quasar/extras/material-icons/material-icons.css";
import "@quasar/extras/mdi-v6/mdi-v6.css";

import "quasar/dist/quasar.css";

import axios from "axios";

axios.defaults.baseURL = import.meta.env.VITE_APP_API_URL;
axios.defaults.xsrfHeaderName = "X-CSRFToken";
axios.defaults.xsrfCookieName = "csrftoken";

const app = createApp(App);

app.use(router);
app.use(Quasar, {
  plugins: {},
});

app.mount("#app");
