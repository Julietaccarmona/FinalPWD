import { createRouter, createWebHistory } from "vue-router";

import HomeView from "../views/HomeView.vue";
import LoginView from "../views/LoginView.vue";
import RegisterView from "../views/RegisterView.vue";
import ConveniosView from "../views/ConveniosView.vue";
import CrearConvenioView from "../views/CrearConvenioView.vue";

import { useAuthStore } from "../stores/auth";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/login",
      name: "login",
      component: LoginView,
    },
    {
      path: "/register",
      name: "register",
      component: RegisterView,
    },
    {
      path: "/convenios",
      name: "convenios",
      component: ConveniosView,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/convenios/nuevo",
      component: CrearConvenioView,
      meta: {
        requiresAuth: true,
      },
    },
  ],
});

router.beforeEach((to, from, next) => {
  const auth = useAuthStore();

  if (to.meta.requiresAuth && !auth.autenticado) {
    next("/login");
  } else {
    next();
  }
});

export default router;
