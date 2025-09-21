import requests

def sumatoria(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

# crea una funcion para dividir dos numeros
def division(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

def potencia(a, b):
    return a ** b

def obtener_pokemon(nombre):
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Pokemon no encontrado"}

print(obtener_pokemon("Charmander"))
