<template>
  <div class="registro">

    <h2>Crear cuenta</h2>

    <form @submit.prevent="registrarUsuario">

      <label>
        Nombre
      </label>

      <input 
        v-model="nombre"
        type="text"
      />


      <label>
        Email
      </label>

      <input 
        v-model="email"
        type="email"
      />


      <label>
        Contraseña
      </label>

      <input 
        v-model="password"
        type="password"
      />


      <button>
        Registrarse
      </button>

    </form>

  </div>
</template>


<script setup>

import { ref } from "vue";
import { useRouter } from "vue-router";
import { registrar } from "../services/authService";


const router = useRouter();


const nombre = ref("");
const email = ref("");
const password = ref("");


async function registrarUsuario(){

  try{

    await registrar({
      nombre: nombre.value,
      email: email.value,
      password: password.value
    });


    alert("Usuario creado correctamente");

    router.push("/login");


  }catch(error){

    console.error(error);

    alert(
      error.response?.data?.mensaje ||
      "Error al registrar usuario"
    );

  }

}

</script>