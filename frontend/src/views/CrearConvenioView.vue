<template>
  <div>
    <h2>Nuevo Convenio</h2>

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
import { useAuthStore } from "../stores/auth";
import { crearConvenio } from "../services/convenioService";
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
    console.log(auth.token);
    const respuesta = await crearConvenio(datos, auth.token);

    console.log(respuesta);
    console.log("TOKEN:", auth.token);
    console.log("USUARIO:", auth.usuario);

    alert("Convenio creado correctamente.");
  } catch (error) {
    console.error(error);
    console.log(error.response);
    console.log(error.response.data);

    alert(error.response?.data?.mensaje || "Error al crear el convenio.");
  }
}

onMounted(async () => {
  try {
    const [listaPaises, listaActores, listaTipos] = await Promise.all([
      obtenerPaises(auth.token),
      obtenerActores(auth.token),
      obtenerTiposConvenio(auth.token),
    ]);

    paises.value = listaPaises;
    actores.value = listaActores;
    tiposConvenio.value = listaTipos;

  } catch (error) {
    console.error("Error cargando datos del formulario:", error);

    alert(
      "No se pudieron cargar los datos. Probablemente la sesión expiró."
    );
  }
});
</script>
