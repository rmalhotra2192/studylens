import axios from "axios";
import { createStore } from "vuex";

export default createStore({
  state: {
    accessToken: null,
    refreshToken: null,
  },
  getters: {},
  mutations: {
    setAccessToken(state, token) {
      state.accessToken = token;
    },
    setRefreshToken(state, token) {
      state.refreshToken = token;
    },
  },
  actions: {
    refreshToken() {
      axios
        .post(`${process.env.VUE_APP_API_BASE_URL}/api/user/token/refresh`, {
          refresh: this.$store.state.refreshToken,
        })
        .then((response) => {
          this.$store.commit('setAccessToken', response.data.access);
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },
  modules: {},
});
