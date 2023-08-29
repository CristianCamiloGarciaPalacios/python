m = int(input("Numero de filas: "))
n = int(input("Numero de columnas: "))
n_rectangulos = 0
for i in range (0, m+1):
    for j in range (0, n+1):
        n_rectangulos += (m-i)*(n-j)
print("numero de rectangulos (m-i)(n-j):", n_rectangulos)

sub_n = 0
sub_m = 0
n_rectangulos = 0
for i in range (0, m+1):
    sub_m += i
for j in range (0, n+1):
        sub_n += j
n_rectangulos = (sub_m)*(sub_n)
print("numero de rectangulos sumatorias:", n_rectangulos)

n_rectangulos = 0
n_rectangulos = ((m*(m+1))/2)*((n*(n+1))/2)
print("numero de rectangulos propiedad:", n_rectangulos)