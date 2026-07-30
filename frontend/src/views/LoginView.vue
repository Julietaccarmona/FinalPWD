<template>
  <div>
    <h2>Iniciar sesión</h2>

    <form @submit.prevent="iniciarSesion">
      <div>
        <label>Email</label><br>
        <input
          v-model="email"
          type="email"
          required
        >
      </div>

      <br>

      <div>
        <label>Contraseña</label><br>
        <input
          v-model="password"
          type="password"
          required
        >
      </div>

      <br>

      <button type="submit">
        Ingresar
      </button>
    </form>

    <br>

    <p v-if="mensaje">
      {{ mensaje }}
    </p>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";

const email = ref("");
const password = ref("");
const mensaje = ref("");

const router = useRouter();
const auth = useAuthStore();

async function iniciarSesion() {
  try {
    await auth.login(email.value, password.value);

    mensaje.value = "Inicio de sesión correcto.";

    router.push("/convenios");

  } catch (error) {

    mensaje.value =
      error.response?.data?.mensaje ||
      "Error al iniciar sesión.";
  }
}
</script>