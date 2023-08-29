# u^e mod(m)
m = 2591  # p sin cola
u = 1044  # texto plano o p con cola ES
e = 471  # e
cadena = (str(bin(e))[2:])[::-1]
cuadrado = (u*u) % m
for bit in cadena[1:]:
    if bit == "1":
        u = (u*cuadrado) % m
    cuadrado = (cuadrado*cuadrado) % m

print(u)
