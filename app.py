print("Inframonitor Iniciado! \n Hello world!")
from flask import Flask
import psutil

app = Flask(__name__)
memoria = psutil.virtual_memory()


@app.route('/')
def inicio():
	memoria = psutil.virtual_memory().percent
	return f"Uso de RAM do Ubuntu: {memoria}%"
