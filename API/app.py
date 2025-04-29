import os
from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/familia")
def get_familia():
    rows = ["Amin", "Marce", "Miranda"]
    return rows

@app.get("/superheroesDC")
def get_superheroes():
    rows = ["Superman", "Batman", "Flash", "Linterna Verde", "Mujer maravilla", "Aquaman", "Shazam", "Cyborg"]
    return rows

@app.get("/CursosPlatzi")
def get_superheroes():
    rows = ["linux", "python", "git y github", "ingles A1", "terminal comandos", "Introduccion a la IA", "excel", "chapGPT"]
    return rows