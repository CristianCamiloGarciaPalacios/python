# Autor: Cristian Camilo García Palacios
#PIN: 1000796221
# Fecha: 10/11/2021
# El programa pregunta por una frase para verificar si es palindroma y cuantas vocales tiene
"""
Metodo principal para arrancar el programa:
"""
def main(): 
    Frase = input("Digite la frase que desee: ")
    Frase_guardada = Frase
    Frase = Quitar_espacios(Frase)
    Frase = Paso_a_minuscula(Frase)
    Frase = Quitar_tildes(Frase)
    Numero_vocales = Conteo_vocales(Frase)
    if Comparar(Frase) == True:
        print(f"La frase \"{Frase_guardada}\" es Palindroma y tiene {Numero_vocales} vocales")
    else:
        print(f"La frase \"{Frase_guardada}\" NO es Palindroma y tiene {Numero_vocales} vocales")
"""
Metodo para contar las vocales en la cadena de caracteres:
"""
def Conteo_vocales(Frase_ingresada):
    Numero_vocales = 0
    for i in Frase_ingresada:
        if( i == "a" or i == "e" or i == "i"or i == "o"or i == "u"):
            Numero_vocales = Numero_vocales + 1
    return Numero_vocales

"""
Metodo para reempazar mayusculas por minusculas en la cadena de caracteres:
"""
def Paso_a_minuscula(Frase_ingresada):
    Frase_nueva = Frase_ingresada.lower()
    
    return Frase_nueva
"""
Metodo para reempazar vocales con tilde por vocales sin tilde en la cadena de caracteres:
"""
def Quitar_tildes(Frase_sin_tilde):
    Frase_sin_tilde = Frase_sin_tilde.replace("á", "a")
    Frase_sin_tilde = Frase_sin_tilde.replace("é", "e")
    Frase_sin_tilde = Frase_sin_tilde.replace("í", "i")
    Frase_sin_tilde = Frase_sin_tilde.replace("ó", "o")
    Frase_sin_tilde = Frase_sin_tilde.replace("ú", "u")
    Frase_sin_tilde = Frase_sin_tilde.replace("ñ", "n")
    return Frase_sin_tilde
"""
Metodo para comparar si la frase es palindroma:
"""
def Comparar(Frase_a_comparar):
    if Frase_a_comparar[::1] == Frase_a_comparar[::-1]:
        return True
    else:
        return False
"""
Metodo para quitar cualquier espacio en la frase ingresada:
"""
def Quitar_espacios(Frase_ingrasada):
    return Frase_ingrasada.replace(" ", "")
"""
Inicio del programa:
"""
if(True):
    main()