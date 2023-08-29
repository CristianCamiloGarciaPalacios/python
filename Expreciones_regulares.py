"""
Para mas informacion:
https://relopezbriega.github.io/blog/2015/07/19/expresiones-regulares-con-python/
"""
# Las expreciones regulares son secuencias de caracteres, para hacer busquedas sobre cadenas de texto
import re # libreria de expreciones regulares

"""
"r" antes de las comillas elimina el uso de las secuencias de escape (\\),
por que se considera un texto sin procesar 
"""
# cadena1 = "Hola \nmundo"
# cadena2 = r"Hola \nmundo"
# print("Cadena sin r: "+cadena1)
# print("Cadena con r: "+cadena2)

"""
EXPRECIONES REGULARES:
"""
"""
Recopilacion de datos:
    flags de recopilacion de datos (re.flag):
        IGNORECASE, I: realiza busquedas sin tener en cuenta minusculas o mayusculas.
        VERBOSE, X: Que habilita la modo verborrágico.
        ASCII, A: Que hace que las secuencias de escape \w, \b, \s y \d funciones para coincidencias con los caracteres ASCII.
        DOTALL, S: Hace que el metacaracter funcione para cualquier caracter.
        LOCALE, L: Hace que \w, \W, \b, \B, \s, y \S dependientes de la localización actual.
        MULTILINE: M: Habilita la coincidencia en múltiples líneas, afectando el funcionamiento de los metacaracteres ^ and $.
"""

# Metodo match() busca coincidencias en el comienzo del texto:
# txt = ["en las expresiones regulares",
# "En las expresiones regulares",
# "én las expresiones regulares",
# "las en expresiones regulares",
# "enlas expresiones regulares",
# " en las expreciones regulares"]

# def Uso_match(txt):
#     respuesta = re.match("en", txt, re.I) # match(Condicion a buscar, Texto en el que buscar, flag)
#     if(respuesta):
#         print("LO ENCONTRE")
#         print(respuesta) # Imprime los parametros de la concordancia que encuentre el match()
#         print(respuesta.group()) # Imprime la concordancia que encuentre el match()
#     else:
#         print("NO LO ENCONTRE")
#     print("")

# for i in txt:
#     Uso_match(i)

# Cadena = r"\Holapython \hola programing"
# respuesta = re.match(r"\\Hola", Cadena, re.I)
# print(respuesta)
# print(respuesta.group())

# Metodo search() busca coincidencias en todo el texto
# txt = "Las palabras de los que somos estudiantes con pala"
# txt1 = "pala"
# txt2 = "somos estudiar"
# def Uso_search(txtx):
#     respuesta = re.search(txtx,txt) #search(Condicion a buscar, Texto en el que buscar, flag)
#     if respuesta:
#         print("LO ENCONTRE")
#         print(respuesta)
#         print(respuesta.group())
#         print(respuesta.start(),respuesta.end())
#         print(respuesta.span())
#     else:
#         print("NO LO ENCONTRE")
# Uso_search(txt1)
# Uso_search(txt2)
"""Metacaracteres: Son caracteres especiales que nos ayudan a
especificar condiciones de busqueda, como "^" que busca al inicio de linea
y "$" que busca a final de linea"""
# Metodo findall() busca todas las coincidencias en todo el texto
Lista = ["astro","planta","arbol",
"decimo","hogar","leña","oso","ojo",
"Carta","Nombre","señal","pereza","abismo"]
# for dato in Lista:
#     # con la condicion "^[a-z]" buscara que al inicio del texto tenga cualquier letra entre a y z
#     if re.findall("^[a-z]", dato, re.I): #findall(Condicion a buscar, Texto en el que buscar, flag)
#         print(dato)
# # otro ejemplo:
# for dato in Lista:
#     # con la condicion "[a-z]|ñ" buscara en todo el texto cualquie letra entre la a y la z, o la ñ
#     # no tiene re.I, por lo que no ignora minusculas y mayusculas
#     respuesta = re.findall("[a-z]|ñ", dato) 
#     if respuesta:
#         print(dato, respuesta)
# Un ejemplo más:
# for dato in Lista:
#     # con la condicion "[ao]$" busca al final del texto si tiene "a" u "o"
#     if re.findall("[ao]$", dato, re.I): #findall(Condicion a buscar, Texto en el que buscar, flag)
#         print(dato)

"""
En una condicion, cuando se pone algo entre comillas "", buscara cualquier parte del texto 
que coincida la condicion,cuando se pone con parentesis cuadrados [], buscara cualquier 
parte del texto que coincida con uno de los caracteres de la condicion.
"""
# txt = "Estudiarentodolado"
# sin_parentesis = re.findall("Estudiar", txt)
# con_parentesis = re.findall("[ot]", txt)
# # if sin_parentesis:
# #     print(sin_parentesis)
# if con_parentesis:
#     print(con_parentesis)
#     print(len(con_parentesis))
"""
Otros metacaracteres:
\w:	un caracter alfanumérico (incluye "_").
\W:	un caracter no alfanumérico.
\d:	un caracter numérico.
\D:	un caracter no numérico.
\s:	cualquier espacio (lo mismo que [ \t\n\r\f]).
\S: un no espacio.
"""
# txt = """Manzanas: 1
# Peras: 20
# Zanahoria: 14
# Lechuga: 101"""
# # "\d\d" buca cualquier cadena de dos o más caracteres numericos
# respuesta = re.findall("\d\d", txt)
# print(respuesta)
# # ".*" separa el texto en cada parte donde se da enter
# respuesta = re.findall(".*", txt, re.I)
# print(respuesta)

# print(re.search("[0-6]", "Número: 5").group())
# print(re.search("Número: [^5]", "Número: 0").group()) #"[^5]" busca cualquier numero diferente a 5

# txt = """Manzanas1;Peras20;Zanahoria;14,Lechuga;101"""

# respuesta = re.findall("\w+",txt,re.I)
# print(respuesta)