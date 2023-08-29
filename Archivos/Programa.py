"""Modos para abrir un árchivo:
r --> abre un árchivo sólo para lectura. El puntero esta localizado al inicio del árchivo.
rb --> abre un árchivo sólo para lectura en formato binario.
r+ --> abre un árchivo para lectura y escritura.
w --> abre un árchivo sólo para escritura. Sobre escribe el árchivo si ya existe.Si el árchivo no existe,
crea un nuevo árchivo para escritura.
wb --> abre un árchivo sólo para escritura en formato binario. Sobre escribe el árchivo si ya existe.
Si el árchivo no existe, crea un nuevo árchivo para escritura.
w+ --> abre un árchivo para lectura y escritura. Sobre escribe el árchivo si ya existe.Si el árchivo no existe,
crea un nuevo árchivo para escritura.
a --> abre un árchivo para append. Si el árchivo existe, el puntero esta localizado al final del árchivo.
Si el archivo no existe, crea un nuevo archivo para escritura.
"""
"""
Primera forma de abrir un árchivo:
"""
# f = open('Archivos/Texto.txt', 'w+', encoding = 'utf = 8')
# print("Nombre del archibo:", f.name)
# print("El archibo esta cerrado?:", f.closed)
# print("Modo de acceso:",f.mode)
# f.close()
# print("El archibo esta cerrado?:", f.closed)
"""
Segunda forma de abrir un árchivo:
"""
# with open('Archivos/Texto1.txt','w+',encoding = 'utf=8') as f:
#     data = 'primera linea del árchivo\n'
#     f.write(data)
#     data = 'segunda linea del árchivo\n'
#     f.write(data)
#     data = 'tercera linea del árchivo\n'
#     f.write(data)

    # f.write("")

"""
Leer contenido de un árchivo:
"""
with open('python/Archivos/Texto1.txt','r',encoding = 'utf=8') as f:
    for i in f:
        print(i,end="")

    print(f.readlines())

    print(f.readline())
    print(f.readline(2))
    print(f.readline(10))

    print(f.read())
    print(f.read(9))
"""
Escribir elementos de una lista, de forma directa
"""
# Lista_1 = ["Primera linea","Segunda linea","...","Cuarta linea"]
# with open('Archivos/Texto1.txt','w+',encoding = 'utf=8') as f:
#     f.writelines(Lista_1)
"""
Crear archivo binario serializado
"""
# import pickle

# años = ["1991","2021","2003","4000"]
# dias = ["01","02","30","15"]
# with open('Texto1.txt','wb') as f:
#     pickle.dump(años, f)
#     pickle.dump(dias, f)
"""
Leer archivo binario serializado
"""
# import pickle

# with open('Archivos/Texto1.txt','rb') as f:
#     Lista_1 = pickle.load(f)
#     Lista_2 = pickle.load(f)
#     print(Lista_1)
#     print(Lista_2)
"""
Serializar archivo con Json
"""
"""$Json serializa objetos de tipo diccionario$"""
# import json

# Diccionario = {"Mateo":"15","Maria":"17"}
# with open('Archivos/Texto2.json','w+') as f:
#     json.dump(Diccionario,f, indent=2)

"""
Leer archivo con Json
"""
# import json

# with open('Archivos/Texto2.json','r') as f:
#     data = json.load(f)
#     print(data)
#     for i in data:
#         print(i)
#     print(data['Mateo'])

"""
Convertir objeto Json a Python
"""
# import json

# Json_object = """{"Alumnos":"15",
# "Estudiantes":{"Mateo":"15","Maria":"17","García":"18"}}"""
# data = json.loads(Json_object)
# print(Json_object)
# print(data)
"""
Ejempos Serializacion de pickle, json y os
"""
# import pickle
# import os
# posicion = [0,0]
# with open('Archivos/Texto_3.txt','wb') as f:
#     pickle.dump(posicion, f)

# import json

# with open('Archivos/Texto_4.json','w+') as f:
#     json.dump(posicion,f)

# with open('Archivos/Texto_4.txt','w+') as f:
#     f.write(str(posicion))

# with open('Archivos/Texto_3.txt', 'rb') as f:
#     Posicion_extraida = pickle.load(f)
#     tamaño = os.stat('Texto_3.txt').st_size
#     print(tamaño)
#     print(Posicion_extraida)

# with open('Archivos/Texto_4.json', 'r') as f:
#     Posicion_extraida = json.load(f)
#     tamaño = os.stat('Texto_4.json').st_size
#     print(tamaño)
#     print(Posicion_extraida)

# with open('Archivos/Texto_5.txt', 'r', encoding='utf=8') as f:
#     Posicion_extraida = f.read()
#     tamaño = os.stat('Texto_5.txt').st_size
#     print(tamaño)
#     print(Posicion_extraida)

import os
entries = os.scandir('Archivos')
# for entry in entries:
#     print(entry.name + ", es directorio: "
#     + str(entry.is_dir())+", size: "
#     + str(entry.stat().st_size)+", bytes.")

# import random
# opciones = ["","",""," "," "," ","a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
# for i in range (0,10):
#     Nombre = ""
#     for j in range (0,6):
#         Nombre += random.choice(opciones)
#     Nombre+="Tesis"
#     for j in range (0,6):
#         Nombre += random.choice(opciones)
#     print(Nombre)
#     f = open('Archivos/'+Nombre,'w+',encoding = 'utf=8')
#     f.close()


# for entry in entries:
#     Cadena = entry.name
#     Cadena = Cadena.lower()
#     Palabra = "tesis"
#     if Cadena.find(Palabra) != -1:
#         os.remove(entry)