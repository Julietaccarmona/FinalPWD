import { defineStore } from "pinia";
import api from "../services/api";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("token") || null,
    refreshToken: localStorage.getItem("refreshToken") || null,
    usuario: JSON.parse(localStorage.getItem("usuario")) || null,
  }),

  getters: {
    autenticado: (state) => !!state.token,
    esAdmin: (state) => state.usuario?.rol === "admin",
  },

  actions: {
    async login(email, password) {
      const response = await api.post("/auth/login", {
        email,
        password,
      });

      this.token = response.data.access_token;
      this.refreshToken = response.data.refresh_token;
      this.usuario = response.data.usuario;

      localStorage.setItem("token", this.token);
      localStorage.setItem("refreshToken", this.refreshToken);
      localStorage.setItem("usuario", JSON.stringify(this.usuario));
    },

    logout() {
      this.token = null;
      this.refreshToken = null;
      this.usuario = null;

      localStorage.removeItem("token");
      localStorage.removeItem("refreshToken");
      localStorage.removeItem("usuario");
    },
  },
});