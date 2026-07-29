<template>
  <div>
    <h1>Observatorio de Cooperación Internacional</h1>

    <nav>
      <RouterLink to="/">Inicio</RouterLink> |
      <RouterLink to="/login">Login</RouterLink> |
      <RouterLink to="/register">Registro</RouterLink> |
      <RouterLink to="/convenios">Convenios</RouterLink>
    </nav>

    <hr />

    <RouterView />
  </div>
</template>