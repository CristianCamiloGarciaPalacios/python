import re
import copy
estados = []
triangulo = []


def leer():
    while(True):
        cadena = input()
        if cadena != "":
            fila = []
            for i in re.split(" ", cadena):
                try:
                    fila.append(int(i))
                except:
                    fila.append(i)
            estados.append(fila)
        else:
            break


def iniciar():
    for i in range(0, estados.__len__()):
        fila = []
        for j in range(0, i):
            if estados[i][0] == estados[j][0]:
                fila.append("  ")
            else:
                fila.append("><")
        triangulo.append(fila)


def hasta():
    triangulo_original = copy.deepcopy(triangulo)
    while True:
        for a in range(1, estados[0].__len__()):
            for i in range(1, triangulo.__len__()):
                for j in range(0, i):
                    comparar(i, j, a)
        if triangulo == triangulo_original:
            break
        else:
            triangulo_original = copy.deepcopy(triangulo)
    

def comparar(i, j, a):
    if triangulo[i][j] == "  ":
        if estados[i][a] > estados[j][a]:
            if triangulo[estados[i][a]][estados[j][a]] == "><":
                triangulo[i][j] = "><"
        elif estados[j][a] > estados[i][a]:
            if triangulo[estados[j][a]][estados[i][a]] == "><":
                triangulo[i][j] = "><"


def imprimir_triangulo(triangulo):
    for i in range(0, triangulo.__len__()):
        for j in triangulo[i]:
            print(f"{j}", end="")
        print(f"q{i}")


def estados_equivalentes():
    for i in range(0, triangulo.__len__()):
        for j in range(0, i):
            if triangulo[i][j] == "  ":
                print(f"Los estados q{j} y q{i} son equivalentes")


def main():
    leer()
    iniciar()
    hasta()
    imprimir_triangulo(triangulo)
    estados_equivalentes()


main()