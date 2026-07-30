import axios from "axios";

const api = axios.create({
  baseURL: "http://127.0.0.1:5000",
});

// Agrega automáticamente el access token
api.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

// Renueva el token si expiró
api.interceptors.response.use(
  (response) => response,
  async (error) => {
    const originalRequest = error.config;

    // Si es 401 o 422 y todavía no reintentamos
    if (
      (error.response?.status === 401 || error.response?.status === 422) &&
      !originalRequest._retry
    ) {
      originalRequest._retry = true;

      try {
        const refreshToken = localStorage.getItem("refreshToken");

        const response = await axios.post(
          "http://127.0.0.1:5000/auth/refresh",
          {},
          {
            headers: {
              Authorization: `Bearer ${refreshToken}`,
            },
          },
        );

        const nuevoToken = response.data.access_token;

        localStorage.setItem("token", nuevoToken);

        // Actualizamos el header original
        originalRequest.headers.Authorization = `Bearer ${nuevoToken}`;

        // Reintentamos la petición que falló
        return api(originalRequest);
      } catch (refreshError) {
        console.error("No se pudo renovar el token", refreshError);

        localStorage.removeItem("token");
        localStorage.removeItem("refreshToken");
        localStorage.removeItem("usuario");

        window.location.href = "/login";
      }
    }

    return Promise.reject(error);
  }
);

export default api;
