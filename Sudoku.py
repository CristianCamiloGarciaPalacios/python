import random as ra

Ejem_sudoku = [
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]],[[4, 5, 6], [7, 8, 9], [1, 2, 3]],[[7, 8, 9], [1, 2, 3], [4, 5, 6]],
    [[2, 3, 4], [5, 6, 7], [8, 9, 1]],[[5, 6, 7], [8, 9, 1], [2, 3, 4]],[[8, 9, 1], [2, 3, 4], [5, 6, 7]],
    [[3, 4, 5], [6, 7, 8], [9, 1, 2]],[[6, 7, 8], [9, 1, 2], [3, 4, 5]],[[9, 1, 2], [3, 4, 5], [6, 7, 8]]
]

def Molde_sudoku():
    Sudoku = []
    for i in range(0, 9):
        Bloque = []
        for j in range(0,3):
            # Bloque.append(["", "", ""])
            Bloque.append([f"{i}:{j}:0", f"{i}:{j}:1",f"{i}:{j}:2"])
        Sudoku.append(Bloque)
    return Sudoku

def Construir_sudoku(Sudoku):
    for i in range(0, Sudoku.__len__()):
        Lista = [1 ,2 ,3 ,4 ,5 ,6 ,7 ,8 ,9]
        if i == 0 or i == 3 or i == 6:
            Bloque_columna = 0
        elif i == 1 or i == 4 or i == 7:
            Bloque_columna = 1
        elif i == 2 or i == 5 or i == 8:
            Bloque_columna = 2
        if i in range(0, 3):
            Bloque_fila = 0
        elif i in range(3, 6):
            Bloque_fila = 3
        elif i in range(6, 9):
            Bloque_fila = 6
        for j in range(0, 3):
            for k in range (0, 3):
                Aprovar_numero = False
                while Aprovar_numero == False:
                    Numero = ra.choice(Lista)
                    Aprovar_numero = True
                    for l in range(0, 3):
                        # print(f"{Numero}: {Sudoku[Bloque_columna][l][k]}, {Sudoku[Bloque_columna+3][l][k]}, {Sudoku[Bloque_columna+6][l][k]}")
                        if Numero == Sudoku[Bloque_columna][l][k] or Numero == Sudoku[Bloque_columna+3][l][k] or Numero == Sudoku[Bloque_columna+6][l][k]:
                            Aprovar_numero = False
                        # print(f"{Numero}: {Sudoku[Bloque_fila][j][l]}, {Sudoku[Bloque_fila+1][j][l]}, {Sudoku[Bloque_fila+2][j][l]}")
                        if Numero == Sudoku[Bloque_fila][j][l] or Numero == Sudoku[Bloque_fila+1][j][l] or Numero == Sudoku[Bloque_fila+2][j][l]:
                            Aprovar_numero = False
                    if Aprovar_numero == True:
                        Sudoku[i][j][k] = Numero
                        Lista.remove(Numero)
                    # Imprimir_sudoku(Sudoku)
                    # s = input("")

    return Sudoku

def Imprimir_sudoku(Sudoku):
    for j in range(0,3):
        for i in range(0,3):
            print("| ", end="")
            for s in range(0,3):
                print(f"{Sudoku[j*3][i][s]} ", end="")
            print("| ", end="")
            for s in range(0,3):
                print(f"{Sudoku[j*3+1][i][s]} ", end="")
            print("| ", end="")
            for s in range(0,3):
                print(f"{Sudoku[j*3+2][i][s]} ", end="")
            print("| ")
        if j != 2:
            print("-------------------------")

def main():
    Sudoku = Molde_sudoku()
    # Imprimir_sudoku(Sudoku)
    # Sudoku = Ejem_sudoku
    # Imprimir_sudoku(Sudoku)
    Sudoku = Construir_sudoku(Sudoku)
    Imprimir_sudoku(Sudoku)
main()