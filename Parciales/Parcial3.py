# Autor: Cristian Camilo García Palacios
# PIN: 1000796221
# Fecha: 18/12/2021
# El programa recibe una cadena de caracteres, de la cual saca sus datos, clasificándolos según su título, para devolver una lista con en valor de los datos.

import re #Importa la biblioteca para expreciones regulares

"""
No estaba seguro si se podía usar re.split(), pues en otros lenguajes, como JavaScript, también lo usan,
pero, nos había dicho que no usáramos el split del lenguaje para el parcial,
entonces lo hice de ambas maneras, por si acaso.
"""
"""
Metodo para separar los datos en la cadena ingresada, usando el metodo re.split():
"""
def Convertir_en_lista_con_split(cadena):
    Lista_cadena = re.split(";",cadena)
    # print(Lista_cadena)
    return Lista_cadena

"""
Metodo para separar los datos en la cadena ingresada, sin usar el metodo re.split():
"""
def Convertir_en_lista_sin_split(cadena):
    Lista_cadena = re.findall("[ .,\w]+",cadena, re.I)
    # print(Lista_cadena)
    return Lista_cadena

"""
Metodo que identifica el titulo del dato de la lista de datos:
"""
def Verificar_dato(dato):
    # print(dato)
    if re.match("id[\d]+", dato, re.I):
        Ingresar = Dato_ID(dato)
    elif re.match(r"materia", dato, re.I):
        Ingresar = Dato_materia(dato)
    elif re.match(r"nombre", dato, re.I):
        Ingresar = Dato_nombre(dato)
    elif re.match(r"nota", dato, re.I):
        Ingresar = Dato_nota(dato)
    else:
        print(f"Este programa no sabe del titulo del dato: {dato}")
        Ingresar = None
    return Ingresar

"""
Metodo para sacar el valor del ID:
"""
def Dato_ID(dato):
    Ingresar = re.search("\d+",dato).group()
    return Ingresar

"""
Metodo para sacar el valor del nombre:
"""
def Dato_nombre(dato):
    Posicion = re.search(r"nombre",dato,re.I).end()
    Ingresar = dato[Posicion:len(dato):1]
    return Ingresar

"""
Metodo para sacar el valor de la nota:
"""
def Dato_nota(dato):
    Posicion = re.search("nota[ \d\W]",dato,re.I).end()
    Ingresar = dato[Posicion:len(dato):1]
    return Ingresar

"""
Metodo para sacar el valor de la materia:
"""
def Dato_materia(dato):
    Posicion = re.search(r"materia",dato,re.I).end()
    Ingresar = dato[Posicion:len(dato):1]
    return Ingresar

"""
Metodo principal para arrancar el programa:
"""
def main():
    cadena = input("""Ingrese una cadena de caracteres, con Los titulos a procesar:
""")
    # cadena = r"ID1001011111;NOMBREJUANFERNANDEZ;NOTA15.0;NOTA23.0;NOTA34.0;MATERIAPROGRAMACIÓN 1"
    while True:
        Opcion =  input("¿Decea resolverlo con re.split()? (si o no): ")
        Opcion = Opcion.lower()
        if Opcion == "si":
            Lista_cadena = Convertir_en_lista_con_split(cadena)
            break
        elif Opcion == "no":
            Lista_cadena = Convertir_en_lista_sin_split(cadena)
            break
        else:
            print("Opcion no valida, vuelva a intentar")
    Resultado = []
    for i in Lista_cadena:
        Ingresar = Verificar_dato(i)
        if Ingresar != None:
            Resultado.append(Ingresar)     
    print("La lista de los datos, es:", Resultado)
    
"""
Inicio del programa:
"""
if True:
    main()