import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import axios from "axios";
import "@fortawesome/fontawesome-free/css/all.min.css";
import "@/assets/styles/index.css";

axios.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response.status === 401) {
      return store.dispatch("refreshToken").catch(() => {
        return Promise.reject(error);
      });
    }
    return Promise.reject(error);
  }
);

createApp(App).use(store).use(router).mount("#app");
