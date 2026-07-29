import { defineStore } from "pinia";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: null,
    usuario: null,
  }),

  actions: {
    setToken(token) {
      this.token = token;
    },

    logout() {
      this.token = null;
      this.usuario = null;
    },
  },
});