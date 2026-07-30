import api from "./api";

export async function obtenerConvenios(token) {
  const response = await api.get("/convenios/", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
}

export async function crearConvenio(datos, token) {
  const response = await api.post("/convenios/", datos, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
}