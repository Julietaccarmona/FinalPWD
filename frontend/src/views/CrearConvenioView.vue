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
        <input type="number" v-model="pais_id" />
      </div>

      <br />

      <div>
        <label>Actor</label><br />
        <input type="number" v-model="actor_id" />
      </div>

      <br />

      <div>
        <label>Tipo de convenio</label><br />
        <input type="number" v-model="tipo_convenio_id" />
      </div>

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
import { ref } from "vue";

const titulo = ref("");
const descripcion = ref("");
const fecha_firma = ref("");
const estado = ref("En negociación");

const pais_id = ref("");
const actor_id = ref("");
const tipo_convenio_id = ref("");

function guardarConvenio() {
  console.log({
    titulo: titulo.value,
    descripcion: descripcion.value,
    fecha_firma: fecha_firma.value,
    estado: estado.value,
    pais_id: pais_id.value,
    actor_id: actor_id.value,
    tipo_convenio_id: tipo_convenio_id.value,
  });
}
</script>
