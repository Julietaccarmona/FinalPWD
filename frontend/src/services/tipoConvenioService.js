import api from "./api";

export async function obtenerTiposConvenio(token) {
  const response = await api.get("/tipos-convenio/", {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
}