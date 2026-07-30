```vue
<template>
  <div class="home">
    <section class="hero">
      <div class="texto">
        <h2>Observatorio de Cooperación Internacional</h2>

        <p>
          La cooperación internacional ya no se desarrolla únicamente entre
          Estados nacionales. Provincias, municipios, universidades y otros
          actores subnacionales participan cada vez más en redes internacionales
          mediante acuerdos y proyectos de cooperación.
        </p>

        <p>
          Este observatorio tiene como objetivo registrar, organizar y
          visibilizar iniciativas de cooperación internacional desde los
          territorios, construyendo una biblioteca colaborativa de convenios y
          experiencias de paradiplomacia.
        </p>

        <p>
          La plataforma permite cargar, consultar y gestionar convenios
          internacionales, facilitando el acceso al conocimiento sobre las
          relaciones internacionales subnacionales. Un área que, en la
          disciplina de las Relaciones Internacionales, es relativamente nueva y
          no cuenta con un registro sistemático de información.
        </p>

        <RouterLink to="/convenios" class="boton">
          Explorar convenios
        </RouterLink>
      </div>

      <div class="imagen">
        <img
          src="/argentina.png"
          alt="Mapa de Argentina con conexiones internacionales"
        />
      </div>
    </section>

    <section class="tarjetas">
      <div class="tarjeta">
        🌎
        <h3>Registrar</h3>
        <p>Incorporar convenios de cooperación internacional.</p>
      </div>

      <div class="tarjeta">
        📚
        <h3>Construir conocimiento</h3>
        <p>Crear una biblioteca colaborativa de experiencias.</p>
      </div>

      <div class="tarjeta">
        🤝
        <h3>Conectar territorios</h3>
        <p>Visualizar vínculos de cooperación subnacional.</p>
      </div>
    </section>
  </div>
</template>

<style scoped>
.home {
  padding: 20px;
}

.hero {
  display: flex;
  align-items: center;
  gap: 40px;
}

.texto {
  flex: 1;
}

.texto h2 {
  color: #2c3e50;
  font-size: 32px;
}

.texto p {
  line-height: 1.6;
  color: #444;
}

.imagen {
  flex: 1;
  text-align: center;
}

.imagen img {
  max-width: 100%;
  max-height: 350px;
}

.boton {
  display: inline-block;
  margin-top: 20px;
  background: #1976d2;
  color: white;
  padding: 12px 22px;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
}

.boton:hover {
  background: #1565c0;
}

.tarjetas {
  margin-top: 40px;
  display: flex;
  gap: 20px;
}

.tarjeta {
  flex: 1;
  text-align: center;
  padding: 20px;
  background: #f5f7fb;
  border-radius: 12px;
}

.tarjeta h3 {
  color: #2c3e50;
}
</style>
```
