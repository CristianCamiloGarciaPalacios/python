import random

Numero_random = random.randrange(1, 10, 1)
# print(Numero_random)
"""
Metodo para verificar si el usuario ingresa el numero correcto:
"""
def Adivinar(Intentos):
    Numero_Ingresado = input("Adivine el numero que el programa genero aleatoriamente entre el 1 y el 10: ")
    if(Numero_Ingresado == str(Numero_random)):
        print(
            f"El numero {Numero_Ingresado} es el numero correcto, ¡FELICIDADES!")
        return True
    else:
        if(Intentos != 0):
            print(
                f"El numero {Numero_Ingresado} no es el numero correcto, te quedan {Intentos} intentos")
        else:
            print(
                f"El numero {Numero_Ingresado} no es el numero correcto, te quedaste sin intentos")

"""
While para iniciar y retomar el metodo Adivinar() hasta tres veces:
"""
def main():
    Intentos = 3
    while(Intentos != 0):
        Intentos = Intentos - 1
        if(Adivinar(Intentos) == True):
            break

if True:
    main()
