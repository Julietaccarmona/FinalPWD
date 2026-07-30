<template>
  <div>
    <h2>Editar Convenio</h2>

    <form @submit.prevent="guardarConvenio">
      <div>
        <label>Título</label><br />
        <input type="text" v-model="titulo" />
      </div>

      <br />
      <br />

      <div>
        <label>Fecha de firma</label><br />
        <input type="date" v-model="fecha_firma" />
      </div>

      <br />

      <div>
        <label>Estado</label><br />
        <input type="text" v-model="estado" />
      </div>

      <br />

      <div>
        <label>País</label><br />

        <select v-model="pais_id">
          <option value="">Seleccione un país</option>

          <option v-for="pais in paises" :key="pais.id" :value="pais.id">
            {{ pais.nombre }}
          </option>
        </select>
      </div>
      <br />

      <div>
        <label>Actor</label><br />

        <select v-model="actor_id">
          <option value="">Seleccione un actor</option>

          <option v-for="actor in actores" :key="actor.id" :value="actor.id">
            {{ actor.nombre }}
          </option>
        </select>
      </div>

      <br />

      <div>
        <label>Tipo de convenio</label><br />

        <select v-model="tipo_convenio_id">
          <option value="">Seleccione un tipo</option>

          <option v-for="tipo in tiposConvenio" :key="tipo.id" :value="tipo.id">
            {{ tipo.nombre }}
          </option>
        </select>
      </div>

      <br />
      <div>
        <label>Descripción</label><br />
        <textarea v-model="descripcion"></textarea>
      </div>

      <br />

      <button type="submit">Guardar</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { useRoute, useRouter } from "vue-router";
import { useAuthStore } from "../stores/auth";

import {
  obtenerConvenio,
  actualizarConvenio,
} from "../services/convenioService";

import { obtenerPaises } from "../services/paisService";
import { obtenerActores } from "../services/actorService";
import { obtenerTiposConvenio } from "../services/tipoConvenioService";

const titulo = ref("");
const descripcion = ref("");
const fecha_firma = ref("");
const estado = ref("En negociación");

const pais_id = ref("");
const actor_id = ref("");
const tipo_convenio_id = ref("");
const auth = useAuthStore();
const route = useRoute();
const router = useRouter();

const paises = ref([]);
const actores = ref([]);
const tiposConvenio = ref([]);

async function guardarConvenio() {
  try {
    const datos = {
      titulo: titulo.value,
      descripcion: descripcion.value,
      fecha_firma: fecha_firma.value,
      estado: estado.value,
      pais_id: Number(pais_id.value),
      actor_id: Number(actor_id.value),
      tipo_convenio_id: Number(tipo_convenio_id.value),
    };

    await actualizarConvenio(route.params.id, datos, auth.token);

    alert("Convenio actualizado correctamente.");

    router.push("/convenios");
  } catch (error) {
    console.error(error);

    alert(error.response?.data?.mensaje || "Error al actualizar el convenio.");
  }
}

onMounted(async () => {
  const [listaPaises, listaActores, listaTipos, convenio] = await Promise.all([
    obtenerPaises(auth.token),
    obtenerActores(auth.token),
    obtenerTiposConvenio(auth.token),
    obtenerConvenio(route.params.id, auth.token),
  ]);

  paises.value = listaPaises;
  actores.value = listaActores;
  tiposConvenio.value = listaTipos;

  titulo.value = convenio.titulo;
  descripcion.value = convenio.descripcion;
  fecha_firma.value = convenio.fecha_firma;
  estado.value = convenio.estado;

  pais_id.value = convenio.pais_id;
  actor_id.value = convenio.actor_id;
  tipo_convenio_id.value = convenio.tipo_convenio_id;
});
</script>
