import api from "./api";

export async function obtenerPaises(token) {
  const response = await api.get("/paises/", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
}