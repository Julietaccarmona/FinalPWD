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

export async function eliminarConvenio(id, token) {
  const response = await api.delete(`/convenios/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
}

export async function obtenerConvenio(id, token) {
  const response = await api.get(`/convenios/${id}`, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
}

export async function actualizarConvenio(id, datos, token) {
  const response = await api.put(`/convenios/${id}`, datos, {
    headers: {
      Authorization: `Bearer ${token}`,
    },
  });

  return response.data;
}