Filas_matriz_uno = int(input("Ingrese el numero de filas de la primera matriz: "))
Columnas_matriz_uno = int(input("Ingrese el numero de columnas de la primera matriz: "))
Matriz_uno = []
for i in range (1,Filas_matriz_uno+1):
    Matriz_uno.append([])
    for j in range (1,Columnas_matriz_uno+1):
        if i == j:
            Matriz_uno[i-1].append(1)
        else:
            Numero_a_ingresar = i
            for k in range(1,j):
                Numero_a_ingresar = Numero_a_ingresar*i
            Matriz_uno[i-1].append(Numero_a_ingresar)

for i in range (0,Filas_matriz_uno):
    print(Matriz_uno[i])