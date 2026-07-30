<template>
  <div>
    <h2>Convenios</h2>

    <p v-if="cargando">Cargando...</p>

    <table v-else border="1" cellpadding="8">
      <thead>
        <tr>
          <th>ID</th>
          <th>Título</th>
          <th>País</th>
          <th>Actor</th>
          <th>Tipo</th>
          <th>Estado</th>
        </tr>
      </thead>

      <tbody>
        <tr v-for="convenio in convenios" :key="convenio.id">
          <td>{{ convenio.id }}</td>
          <td>{{ convenio.titulo }}</td>
          <td>{{ convenio.pais }}</td>
          <td>{{ convenio.actor }}</td>
          <td>{{ convenio.tipo_convenio }}</td>
          <td>{{ convenio.estado }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useAuthStore } from "../stores/auth";
import { obtenerConvenios } from "../services/convenioService";

const auth = useAuthStore();

const convenios = ref([]);
const cargando = ref(true);

onMounted(async () => {
  console.log("Token:", auth.token);
  console.log("Usuario:", auth.usuario);

  try {
    const datos = await obtenerConvenios(auth.token);

    console.log("Respuesta API:", datos);

    convenios.value = datos;
  } catch (error) {
    console.error(error);
  } finally {
    cargando.value = false;
  }
});

</script>
