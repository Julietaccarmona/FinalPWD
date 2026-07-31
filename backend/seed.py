from run import app

from app.extensions import db
from app.models.pais import Pais
from app.models.actor import Actor
from app.models.tipo_convenio import TipoConvenio


with app.app_context():

    # --------------------
    # Países
    # --------------------

    paises = [
        {
            "nombre": "Argentina",
            "codigo_iso": "ARG",
            "continente": "América"
        },
        {
            "nombre": "Chile",
            "codigo_iso": "CHL",
            "continente": "América"
        },
        {
            "nombre": "Brasil",
            "codigo_iso": "BRA",
            "continente": "América"
        },
        {
            "nombre": "Uruguay",
            "codigo_iso": "URY",
            "continente": "América"
        },
        {
            "nombre": "China",
            "codigo_iso": "CHN",
            "continente": "Asia"
        },
        {
            "nombre": "España",
            "codigo_iso": "ESP",
            "continente": "Europa"
        },
        {
            "nombre": "Francia",
            "codigo_iso": "FRA",
            "continente": "Europa"
        },
        {
            "nombre": "Estados Unidos",
            "codigo_iso": "USA",
            "continente": "América"
        },
    ]


    for p in paises:

        existe = Pais.query.filter_by(
            nombre=p["nombre"]
        ).first()

        if not existe:
            db.session.add(
                Pais(**p)
            )


    # --------------------
    # Actores
    # --------------------

    actores = [
        {
            "nombre": "Gobierno de Río Negro",
            "tipo": "Gobierno provincial"
        },
        {
            "nombre": "Municipalidad de Viedma",
            "tipo": "Gobierno municipal"
        },
        {
            "nombre": "Universidad Nacional del Comahue",
            "tipo": "Universidad"
        },
        {
            "nombre": "Universidad Nacional del Centro",
            "tipo": "Universidad"
        },
        {
            "nombre": "Gobierno de Neuquén",
            "tipo": "Gobierno provincial"
        },
        {
            "nombre": "Agencia de Cooperación Internacional",
            "tipo": "Organismo internacional"
        },
    ]


    for a in actores:

        existe = Actor.query.filter_by(
            nombre=a["nombre"]
        ).first()

        if not existe:
            db.session.add(
                Actor(**a)
            )


    # --------------------
    # Tipos de convenio
    # --------------------

    tipos = [
        {
            "nombre": "Cooperación Técnica",
            "descripcion": "Intercambio de conocimientos, asistencia técnica y capacitación."
        },
        {
            "nombre": "Cooperación Académica",
            "descripcion": "Colaboración entre instituciones educativas y de investigación."
        },
        {
            "nombre": "Cooperación Científica",
            "descripcion": "Proyectos conjuntos de investigación e innovación."
        },
        {
            "nombre": "Cooperación Cultural",
            "descripcion": "Intercambios y proyectos culturales."
        },
        {
            "nombre": "Memorándum de Entendimiento",
            "descripcion": "Acuerdo marco de colaboración entre instituciones."
        },
    ]


    for t in tipos:

        existe = TipoConvenio.query.filter_by(
            nombre=t["nombre"]
        ).first()

        if not existe:
            db.session.add(
                TipoConvenio(**t)
            )


    db.session.commit()


    print("Datos iniciales cargados correctamente.")