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
          <th>Cargado por</th>
          <th>Acciones</th>
          <th v-if="auth.esAdmin">Acciones</th>
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
          <td>{{ convenio.usuario }}</td>
          <td v-if="auth.esAdmin">
            <button @click="borrarConvenio(convenio.id)">Eliminar</button>
          </td>
          <td>
            <RouterLink
              v-if="auth.esAdmin || convenio.usuario_id === auth.usuario?.id"
              :to="`/convenios/${convenio.id}/editar`"
            >
              <button class="btn-editar">Editar</button>
            </RouterLink>

            <button
              v-if="auth.esAdmin"
              class="btn-eliminar"
              @click="eliminar(convenio.id)"
            >
              Eliminar
            </button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useAuthStore } from "../stores/auth";
import {
  obtenerConvenios,
  eliminarConvenio,
} from "../services/convenioService";

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

async function borrarConvenio(id) {
  if (!confirm("¿Seguro que desea eliminar este convenio?")) {
    return;
  }

  try {
    await eliminarConvenio(id, auth.token);

    convenios.value = convenios.value.filter((convenio) => convenio.id !== id);

    alert("Convenio eliminado correctamente.");
  } catch (error) {
    console.error(error);

    alert(error.response?.data?.mensaje || "Error al eliminar convenio.");
  }
}

async function eliminar(id) {
  const confirmar = confirm(
    "¿Está seguro de que desea eliminar este convenio?",
  );

  if (!confirmar) return;

  try {
    await eliminarConvenio(id, auth.token);

    convenios.value = convenios.value.filter((convenio) => convenio.id !== id);

    alert("Convenio eliminado correctamente.");
  } catch (error) {
    console.error(error);

    alert(error.response?.data?.mensaje || "Error al eliminar el convenio.");
  }
}
</script>

<style scoped>
.btn-editar {
  background: #1976d2;
  margin-right: 8px;
}

.btn-eliminar {
  background: #d32f2f;
}

.btn-eliminar:hover {
  background: #b71c1c;
}
</style>
