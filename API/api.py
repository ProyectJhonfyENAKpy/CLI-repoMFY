# api.py

from fastapi import FastAPI

app = FastAPI(
    title="API de Jhonfy - Ingeniero en Informática y Científico de Datos",
    description="Explora mis proyectos, habilidades y áreas de especialización en Ciencia de Datos, Machine Learning, Big Data, Computer Vision, y más.",
    version="1.0.0",
    contact={
        "name": "Jhonfy",
        "url": "https://github.com/jhonfy3320",
        "email": "tu-email@example.com",
    },
)

@app.get("/")
async def read_root():
    return {
        "mensaje": "¡Bienvenido a la API de Jhonfy!",
        "profesion": "Ingeniero en Informática | Científico de Datos",
        "enfoque": [
            "Desarrollo de Software",
            "Alta Gerencia de Proyectos",
            "Big Data y Machine Learning con GCP",
            "Procesamiento de Lenguaje Natural (NLP) con Python y NLTK",
            "Computer Vision con TensorFlow",
            "Análisis de Datos con Pandas, NumPy y Matplotlib",
            "Visualización de Datos y Storytelling (Tableau)",
            "Bases de Datos con PostgreSQL",
            "Redes Neuronales con Keras y TensorFlow",
            "Geoespacial Analysis con QGIS",
        ],
        "proyectos_destacados": [
            "Detección de vehículos en carreteras (TensorFlow)",
            "Clasificación de sentimientos en reseñas de texto",
            "Dashboard de ventas para Carmatd (Tableau)",
            "Análisis de asesinatos en Game of Thrones (Storytelling de Datos)",
            "Clasificador de nombres en español (NLP)",
        ],
        "github": "https://github.com/jhonfy3320",
    }

@app.get("/proyectos")
async def listar_proyectos():
    return {
        "proyectos": [
            {
                "nombre": "Detección de Vehículos",
                "tecnologías": ["TensorFlow", "Computer Vision"],
                "descripcion": "Sistema de detección de carros y motos en videos de tráfico en tiempo real."
            },
            {
                "nombre": "Clasificador de Sentimientos",
                "tecnologías": ["NLP", "NLTK", "Machine Learning"],
                "descripcion": "Modelo para clasificar reseñas como positivas o negativas."
            },
            {
                "nombre": "Dashboard Carmatd",
                "tecnologías": ["Tableau", "Storytelling"],
                "descripcion": "Dashboard interactivo para la gerencia de ventas automotrices."
            },
            {
                "nombre": "Clasificador de Nombres",
                "tecnologías": ["NLP", "scikit-learn"],
                "descripcion": "Clasificación de nombres en español por género utilizando ML."
            },
        ]
    }

@app.get("/tecnologias")
async def listar_tecnologias():
    return {
        "tecnologias": [
            "Python", "TensorFlow", "Keras", "Pandas", "NumPy",
            "NLTK", "PostgreSQL", "GitHub", "Tableau", "QGIS",
            "FastAPI", "Docker", "BigQuery", "GCP", "Linux",
        ]
    }
