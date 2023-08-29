import re

Filas_matriz_uno = int(input("Ingrese el numero de filas de la primera matriz: "))
Columnas_matriz_uno = int(input("Ingrese el numero de columnas de la primera matriz: "))
Filas_matriz_dos = int(input("Ingrese el numero de filas de la segunda matriz: "))
Columnas_matriz_dos = int(input("Ingrese el numero de columnas de la segunda matriz: "))
if Columnas_matriz_uno != Filas_matriz_dos:
    print("Las matrices no son multiplicables, intente con otras")
else:
    Matriz_uno = []
    Matriz_dos = []
    print("Ingrese la fila separando terminos por comas: 1,2,3,4")
    for i in range (0, Filas_matriz_uno):
        Matriz_uno.append([])
        Fila_matriz = input(f"Ingrese la fila {i+1}: ")
        Cadena_fila_matriz = re.split(",", Fila_matriz)
        for j in range (0, Columnas_matriz_uno):
            if re.search('/', Cadena_fila_matriz[j]):
                Divicion = re.findall('-\d+|\d+', Cadena_fila_matriz[j])
                Matriz_uno[i].append(float(int(Divicion[0])/int(Divicion[1])))
            else:
                Matriz_uno[i].append(float(Cadena_fila_matriz[j]))
    print("Ingrese la fila separando terminos por comas: 1,2,3,4")
    for i in range (0, Filas_matriz_dos):
        Matriz_dos.append([])
        Fila_matriz = input(f"Ingrese la fila {i+1}: ")
        Cadena_fila_matriz = re.split(",", Fila_matriz)
        for j in range (0, Columnas_matriz_dos):
            if re.search('/', Cadena_fila_matriz[j]):
                Divicion = re.findall('-\d+|\d+', Cadena_fila_matriz[j])
                Matriz_dos[i].append(float(int(Divicion[0])/int(Divicion[1])))
            else:
                Matriz_dos[i].append(float(Cadena_fila_matriz[j]))
    Matriz_resultado = []
    for i in range (0, Filas_matriz_uno):
        Matriz_resultado.append([])
        for j in range (0, Columnas_matriz_dos):
            Numero_a_ingresar = 0
            for k in range (0, Filas_matriz_dos):
                Numero_a_ingresar += Matriz_uno[i][k]*Matriz_dos[k][j]
            Matriz_resultado[i].append(Numero_a_ingresar)
    for i in Matriz_resultado:
        print(i)
