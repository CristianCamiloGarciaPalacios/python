def Comprovar_articulo(Matriz,Articulo):
    Comprovacion = True
    for i in range (0, Matriz.__len__()):
        if Matriz[i][0] == Articulo:
            Comprovacion = False
    return Comprovacion

def main():
    Matriz = []
    while True:
        Articulo = input("Digite el articulo: ")
        if Articulo == "":
            break
        elif Comprovar_articulo(Matriz, Articulo) == True:
            Precio = input("Digite el precio: ")
            Matriz.append([Articulo,Precio])
        else:
            print("El articulo ya a sido ingresado, intente otro.")
    for i in Matriz:
        print(f"El articulo {i[0]} tiene precio de {i[1]}")

if True:
    main()