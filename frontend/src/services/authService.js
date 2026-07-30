import api from "./api";


export async function registrar(datos) {

  const response = await api.post("/auth/register", datos);

  return response.data;

}


export async function login(datos) {

  const response = await api.post("/auth/login", datos);

  return response.data;

}