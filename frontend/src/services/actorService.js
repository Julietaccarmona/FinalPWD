import api from "./api";

export async function obtenerActores(token) {
  const response = await api.get("/actores/", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
}