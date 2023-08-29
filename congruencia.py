m = 12
a = 1
b = 5
soluciones_menores_a_m = []
soluciones_en_Z = []
for i in range(0, m):
    if (a*i-b)%m == 0:
        soluciones_menores_a_m.append(i)
print(soluciones_menores_a_m)
for i in soluciones_menores_a_m:
    soluciones_en_Z.append(f"{m}k+{i}")
print(soluciones_en_Z)