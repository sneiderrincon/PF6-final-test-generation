#importamos las librerias necesarias
import json
import requests

# aqui definimos la funcion que solicitan el readme y que será evaluada en el test

def dish_fetch(num):
        #nos conectanos a la API para obtener la lista de platos típicos de Colombia
        response = requests.get("https://api-colombia.com/api/v1/TypicalDish")
        dishes = response.json()

        # implementamos un blucle for para Buscar el plato con el ID solicitado
        for dish in dishes:
            #aqui nos aseguramos de que el ID del plato coincida con el número ingresado por el usuario 
            if dish.get("id") == num:
                return {
                    "id": dish.get("id"),
                    "name": dish.get("name")
                }

        # Si no se encuentra el ID
        return {
            "id": num,
            "name": "Plato típico no encontrado"
        }




def main():
    print("🍽️ MENÚ DE PLATOS TÍPICOS DE COLOMBIA 🍽️\n")

    try:
        opcion = int(input("Ingresa el ID del plato típico: "))

        # Plato (función evaluada)
        plato = dish_fetch(opcion)

        print("\n📌 Plato seleccionado")
        print(f"ID: {plato['id']}")
        print(f"Nombre: {plato['name']}")
    
    #esto lo colocamos en caso de que no coloque un numero o coloque un numero que no exista en la API
    except ValueError:
        print("❌ Debes ingresar un número válido.")


if __name__ == "__main__":
    main()