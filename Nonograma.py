import random

def Random_boolean():
    return random.choice([True,True,True,False,False])

def Crear_matriz(Eleccion,Longitud):
    Matriz = []
    for i in range(0,Longitud):
        Sub_matriz = []
        for j in range(0,Longitud):
            if Eleccion == "Matriz":
                Sub_matriz.append(Random_boolean())
            elif Eleccion == "Nonograma":
                Sub_matriz.append("")
        Matriz.append(Sub_matriz)
    return Matriz    

def Imprimir_representacion_matriz(Matriz, Longitud):
    for i in range(0,Longitud):
        for j in range(0,Longitud):
            if Matriz[i][j] == True:
                print("\u2B1C ",end="")
            elif Matriz[i][j] == False:
                print("\u2B1B ",end="")
            else:
                print("   ",end="")
        print("")

def Representacion_numerica(Matriz,Longitud):
    Columnas = []
    Filas = []
    for i in range(0,Longitud):
        Sub_filas = []
        Contador_filas = 0
        Sub_columnas = []
        Contador_columnas = 0
        for j in range(0,Longitud):
            if Matriz[i][j] == True:
                Contador_filas += 1
                if j == Longitud-1:
                   Sub_filas.append(Contador_filas)
            elif Contador_filas > 0:
                Sub_filas.append(Contador_filas)
                Contador_filas = 0
            if Matriz[j][i] == True:
                Contador_columnas += 1
                if j == Longitud-1:
                   Sub_columnas.append(Contador_columnas)
            elif Contador_columnas > 0:
                Sub_columnas.append(Contador_columnas)
                Contador_columnas = 0
        Filas.append(Sub_filas)
        Columnas.append(Sub_columnas)
#    print(Filas)
#    print(Columnas)
    return Filas, Columnas

def Imprimir_filas(Filas, Longitud):
    for i in range(0,Longitud):
        String_filas = ""
        for j in range(0,(Filas[i].__len__())):
            String_filas += (str(Filas[i][j])+" ")
        print(f"{String_filas:>{Longitud+1}}")
        
def Imprimir_columnas(Columnas, Longitud):
    String_Columnas = []
    Mayor_longitud = 0
    for i in range(0,Longitud):
        if Columnas[i].__len__() > Mayor_longitud:
            Mayor_longitud = Columnas[i].__len__()
    for i in range(0,Mayor_longitud):
        String_Columnas.append("")
    for i in range(0,Longitud):
        Desde_string = (Mayor_longitud - Columnas[i].__len__())
        for j in range(0,Mayor_longitud):
            if j >= Desde_string:
                if str(Columnas[i][j-Desde_string]).__len__() > 1:
                    String_Columnas[j] += str(Columnas[i][j-Desde_string])+" "
                else:
                    String_Columnas[j] += str(Columnas[i][j-Desde_string])+"  "
            else:
                String_Columnas[j] += "   "
    for i in range (0, Mayor_longitud):
        a =""
        print(f"{a:{Longitud+1}} ",end="")
        print(String_Columnas[i])

def Imprimir_nonograma_entero(Matriz, Columnas, Filas, Longitud):
    Imprimir_columnas(Columnas,Longitud)
    
    for i in range(0,Longitud):
        String_matriz = ""
        for j in range(0,Longitud):
            if Matriz[i][j] == True:
                String_matriz +="\u2B1C "
            elif Matriz[i][j] == False:
                String_matriz +="\u2B1B "
            else:
                String_matriz +="   "
        String_filas = ""
        for j in range(0,(Filas[i].__len__())):
            String_filas += (str(Filas[i][j])+" ")
        print(f"{String_filas:>{Longitud+1}}{String_matriz}")

def Elegir(Matriz,Columnas,Filas,Longitud):
    while True:
        Seleccion = input("""Escoja lo que desee imprimir ingresando el numero correspondiente:
    (1): Imprimir únicamente la matriz.
    (2): Imprimir únicamente representación numérica de columnas y filas.
    (3): Imprimir todo.
Ingresa: """)
        if(Seleccion == "1"):
            Imprimir_representacion_matriz(Matriz,Longitud)
            break
        elif(Seleccion == "2"):
            Imprimir_columnas(Columnas, Longitud)
            Imprimir_filas(Filas,Longitud)
            break
        elif(Seleccion == "3"):
            Imprimir_nonograma_entero(Matriz,Columnas,Filas,Longitud)
            break
        else:
            print("Digitaste algo incorrecto, vuelve a escoger.")

def Comienzo(Matriz,Determinador,Longitud, Tipo):
    for i in range(0,Longitud):
        Numero_datos = Determinador[i].__len__()
        Tamaño = Numero_datos-1
        for j in range(0, Numero_datos):
            Tamaño += int(Determinador[i][j])
        Espacio = Longitud-Tamaño
        Contador = Espacio
        for j in range (0,Numero_datos):
            Mini_contador = 0
            for k in range (0,Determinador[i][j]+1):
                if Mini_contador<(Determinador[i][j]-Espacio):
                    if Tipo == "Filas":
                        Matriz[i][Contador+k] = True
                    elif Tipo == "Columnas":
                        Matriz[Contador+k][i] = True
                    Mini_contador += 1
                elif Tamaño == Longitud and j != Numero_datos-1:
                    if Tipo == "Filas":
                        Matriz[i][Contador+k] = False
                    elif Tipo == "Columnas":
                        Matriz[Contador+k][i] = False
                    Mini_contador += 1
            Contador += Determinador[i][j]+1
    return Matriz

def Main():
    Longitud = int(input("Ingrese la dimencion del nonograma: "))
    Matriz = Crear_matriz("Matriz",Longitud)
    Filas, Columnas = Representacion_numerica(Matriz,Longitud)
    Elegir(Matriz,Columnas,Filas,Longitud)
    Nonograma = Crear_matriz("Nonograma",Longitud)
    Nonograma = Comienzo(Nonograma,Filas,Longitud,"Filas")
    Nonograma = Comienzo(Nonograma,Columnas,Longitud,"Columnas")
    Imprimir_nonograma_entero(Nonograma,Columnas,Filas,Longitud)
  
if(True):
    Main()