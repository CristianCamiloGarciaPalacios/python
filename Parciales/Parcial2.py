# Autor: Cristian Camilo García Palacios
# PIN: 1000796221
# Fecha: 6/12/2021
# El programa ingresa una lista a un archivo tipo json, para enseguida pedir por modificaciones que se realizaran al archivo

import json

"""
Metodo para pasar datos al archivo json:
"""
def Pasar_datos_al_json(datos):
    with open("python/Parciales/arch.json", "w+", encoding = "utf8") as f: 
	    json.dump(datos, f, indent=2) 

"""
Metodo para obtener datos del archivo json:
"""
def Obtener_datos_del_json():
    with open("python/Parciales/arch.json", "r") as f:
        datos = json.load(f)
    return datos

"""
Metodo para esperar hasta un enter:
"""
def Esperar_enter():
    a = input("Precione < ENTER > para continuar")

"""
Metodo para modificar la cantidad de Tomate:
"""
def Modificar_tomate():
    datos = Obtener_datos_del_json()
    print("    Nombre:", datos["Fruteria"][1]["Verduras"][0]["Nombre"], "; Cantidad:", datos["Fruteria"][1]["Verduras"][0]["Cantidad"])
    Modificacion = int(input("    Ingrese el valor por el que quiere cambiar la cantidad de tomate: "))
    datos["Fruteria"][1]["Verduras"][0]["Cantidad"] = Modificacion
    print("    Nombre:", datos["Fruteria"][1]["Verduras"][0]["Nombre"], "; Cantidad:", datos["Fruteria"][1]["Verduras"][0]["Cantidad"])
    Pasar_datos_al_json(datos)
    print("    Se modifico la estructura de: Tomate")

"""
Metodo para eliminar la estructura relacionada con Mandarina:
""" 
def Eliminar_mandarina():
    datos = Obtener_datos_del_json()
    while True:
        Decision = input("""    Ingrese \"si\" si desea eliminar la estructura mandarina
    Ingrese \"no\" si NO desea eliminar la estructura mandarina
    """)
        if Decision == "si":
            datos["Fruteria"][0]["Frutas"].pop(0)
            Pasar_datos_al_json(datos)
            print("    Se elimino la estructura de: Mandarina")
            break
        elif Decision == "no":
            print("    No se a modificado")
            break
        else:
            print("    El dato ingresado no coincide con una de las opciones, intente otra vez")

"""
Metodo para imprimir los datos del archivo json:
"""
def Imprimir_archivo():
    while True:
        Decision = input("""    Ingrese \"si\" si desea imprimir el archivo
    Ingrese \"no\" si NO desea imprimir el archivo
    """)
        if Decision == "si":
            datos = Obtener_datos_del_json()
            print(datos)
            break
        elif Decision == "no":
            print("    No se imprimio")
            break
        else:
            print("    El dato ingresado no coincide con una de las opciones, intente otra vez")

"""
Metodo principal:
"""
def main():
    datos = {"Fruteria":
         [{"Frutas":
           [{"Nombre": "Mandarina", "Cantidad": 30},
            {"Nombre": "Piña", "Cantidad": 10},
            {"Nombre": "Naranja", "Cantidad": 60}
            ]
           },
          {"Verduras":
           [{"Nombre": "Tomate", "Cantidad": 90},
            {"Nombre": "Aguacate", "Cantidad": 25},
            {"Nombre": "Lechuga", "Cantidad": 10}
            ]
           }
          ]
         }
    Pasar_datos_al_json(datos)
    Imprimir_archivo()
    Esperar_enter()
    Modificar_tomate()
    Esperar_enter()
    Eliminar_mandarina()
    Esperar_enter()
    Imprimir_archivo()

"""
Estructura de ejecucion:
"""
if True:
    main()