<template>
  <div>
    <h1>Observatorio de Cooperación Internacional</h1>

    <nav>
      <RouterLink to="/">Inicio</RouterLink>

      <template v-if="!auth.autenticado">
        |
        <RouterLink to="/login">Login</RouterLink>
        |
        <RouterLink to="/register">Registro</RouterLink>
      </template>

      <template v-if="auth.autenticado">
        |
        <RouterLink to="/convenios">Convenios</RouterLink>
        |
        <RouterLink to="/convenios/nuevo">
          Nuevo convenio
        </RouterLink>

        |
        Usuario:
        {{ auth.usuario?.nombre }}

        <span v-if="auth.esAdmin">
          (admin)
        </span>

        |
        <button @click="cerrarSesion">
          Cerrar sesión
        </button>
      </template>
    </nav>

    <hr />

    <RouterView />
  </div>
</template>


<script setup>
import { useRouter } from "vue-router";
import { useAuthStore } from "./stores/auth";


const auth = useAuthStore();
const router = useRouter();


function cerrarSesion() {

  auth.logout();

  router.push("/login");

}
</script>