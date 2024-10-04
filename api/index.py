
from fastapi import FastAPI, Request
import random 

from fastapi.middleware.cors import CORSMiddleware


### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    return {"message": "Hello from FastAPI"}





origins = [
    "http://localhost",
    "http://localhost:3000",  # Si estás usando React o alguna aplicación frontend local
    "https://sddfclc7-8000.brs.devtunnels.ms",  # Añade el dominio desde donde haces fetch
    # Puedes agregar más orígenes si es necesario
]

# Añadir el middleware CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir los orígenes definidos
    allow_credentials=True,  # Permitir el envío de cookies (si es necesario)
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)


jugadores = {}
cartas = [
    # Corazones
    "As de Corazones", "Dos de Corazones", "Tres de Corazones", "Cuatro de Corazones", "Cinco de Corazones", 
    "Seis de Corazones", "Siete de Corazones", "Ocho de Corazones", "Nueve de Corazones", "Diez de Corazones", 
    "J de Corazones", "Q de Corazones", "K de Corazones",
    
    # Diamantes
    "As de Diamantes", "Dos de Diamantes", "Tres de Diamantes", "Cuatro de Diamantes", "Cinco de Diamantes", 
    "Seis de Diamantes", "Siete de Diamantes", "Ocho de Diamantes", "Nueve de Diamantes", "Diez de Diamantes", 
    "J de Diamantes", "Q de Diamantes", "K de Diamantes",
    
    # Tréboles
    "As de Tréboles", "Dos de Tréboles", "Tres de Tréboles", "Cuatro de Tréboles", "Cinco de Tréboles", 
    "Seis de Tréboles", "Siete de Tréboles", "Ocho de Tréboles", "Nueve de Tréboles", "Diez de Tréboles", 
    "J de Tréboles", "Q de Tréboles", "K de Tréboles",
    
    # Picas
    "As de Picas", "Dos de Picas", "Tres de Picas", "Cuatro de Picas", "Cinco de Picas", 
    "Seis de Picas", "Siete de Picas", "Ocho de Picas", "Nueve de Picas", "Diez de Picas", 
    "J de Picas", "Q de Picas", "K de Picas"
]


cartas_barajadas = [
    # Corazones
    "As de Corazones", "Dos de Corazones", "Tres de Corazones", "Cuatro de Corazones", "Cinco de Corazones", 
    "Seis de Corazones", "Siete de Corazones", "Ocho de Corazones", "Nueve de Corazones", "Diez de Corazones", 
    "J de Corazones", "Q de Corazones", "K de Corazones",
    
    # Diamantes
    "As de Diamantes", "Dos de Diamantes", "Tres de Diamantes", "Cuatro de Diamantes", "Cinco de Diamantes", 
    "Seis de Diamantes", "Siete de Diamantes", "Ocho de Diamantes", "Nueve de Diamantes", "Diez de Diamantes", 
    "J de Diamantes", "Q de Diamantes", "K de Diamantes",
    
    # Tréboles
    "As de Tréboles", "Dos de Tréboles", "Tres de Tréboles", "Cuatro de Tréboles", "Cinco de Tréboles", 
    "Seis de Tréboles", "Siete de Tréboles", "Ocho de Tréboles", "Nueve de Tréboles", "Diez de Tréboles", 
    "J de Tréboles", "Q de Tréboles", "K de Tréboles",
    
    # Picas
    "As de Picas", "Dos de Picas", "Tres de Picas", "Cuatro de Picas", "Cinco de Picas", 
    "Seis de Picas", "Siete de Picas", "Ocho de Picas", "Nueve de Picas", "Diez de Picas", 
    "J de Picas", "Q de Picas", "K de Picas"
]
random.shuffle(cartas_barajadas)
cartas_locales = cartas_barajadas

print(cartas_barajadas)

@app.get("/")
def read_root():
    return {"Juego": "BlackJack"}

@app.get("/jugar")
def read_root():
    return {"opcion": "Estas jugando"}

@app.get("/pedircartas")
def read_root(request: Request):
      # Obtener la IP del cliente
    client_ip = request.client.host

    # Si el jugador ya existe, usa su lista de cartas, si no, crea una nueva
    if client_ip not in jugadores:
        jugadores[client_ip] = []
    

    # Pedir cartas para el jugador
    pedir_cartas(jugadores[client_ip])

    # Imprimir tipo y contenido para depuración
    print(f"Tipo de jugador: {type(jugadores[client_ip])}")
    print(f"Contenido de jugador: {jugadores[client_ip]}")

    # Retornar las cartas del jugador
    return {"ip": client_ip, "cartas": jugadores[client_ip]}

@app.get("/posicion")
async def read_root(request: Request):
    numero_aleatorio = random.randint(1, 8)
    return {
        "numero_aleatorio": numero_aleatorio
    }

import random




def pedir_cartas(jugador):
   #print(cartas_barajadas)
   if len(jugador) > 1:
        jugador.append(cartas_barajadas[0])
        del cartas_barajadas[0]
   else:
        jugador.append(cartas_barajadas[0])
        jugador.append(cartas_barajadas[1])
        del cartas_barajadas[0]
        del cartas_barajadas[0]
        #print(cartas_barajadas)
        #print(jugador)
   return jugador
  

jugador1 = []
jugador2 = []


""" print(cartas_barajadas)
pedir_cartas(jugador1)
pedir_cartas(jugador2)
print(jugador1)
print(jugador2)
print(cartas_barajadas) """

@app.get("/cartas-barajadas")
def read_root():
    return {"cartas barajadas": cartas_barajadas}

async def get_ip(request: Request):
    client_ip = request.client.host
    return {"client_ip": client_ip}


