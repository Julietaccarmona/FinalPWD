```vue
<template>
  <div id="app">
    <header>
      <h1>🌎 Observatorio de Cooperación Internacional</h1>

      <nav>
        <RouterLink to="/">Inicio</RouterLink>

        <template v-if="!auth.autenticado">
          <RouterLink to="/login">Login</RouterLink>
          <RouterLink to="/register">Registro</RouterLink>
        </template>

        <template v-else>
          <RouterLink to="/convenios">Convenios</RouterLink>
          <RouterLink to="/convenios/nuevo"> Nuevo convenio </RouterLink>

          <span class="usuario">
            {{ auth.usuario?.nombre }}
            <strong v-if="auth.esAdmin">(Admin)</strong>
          </span>

          <button @click="cerrarSesion">Cerrar sesión</button>
        </template>
      </nav>
    </header>

    <main>
      <RouterView />
    </main>
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

<style>
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
  background: #f5f7fb;
}

#app {
  max-width: 1100px;
  margin: auto;
}

header {
  background: #2c3e50;
  color: white;
  padding: 20px 30px;
  border-radius: 0 0 12px 12px;
}

header h1 {
  margin: 0 0 18px;
}

nav {
  display: flex;
  align-items: center;
  gap: 15px;
  flex-wrap: wrap;
}

nav a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

nav a:hover {
  text-decoration: underline;
}

.usuario {
  margin-left: auto;
}

button {
  background: #1976d2;
  color: white;
  border: none;
  padding: 8px 14px;
  border-radius: 6px;
  cursor: pointer;
}

button:hover {
  background: #1565c0;
}

main {
  margin-top: 30px;
  background: white;
  padding: 25px;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

th {
  background: #1976d2;
  color: white;
}

th,
td {
  padding: 10px;
  border: 1px solid #ddd;
}

tr:nth-child(even) {
  background: #f8f8f8;
}

input,
select,
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  box-sizing: border-box;
}

label {
  font-weight: bold;
}
</style>
```
