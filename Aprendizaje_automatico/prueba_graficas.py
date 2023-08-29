import matplotlib.pyplot as plt
datos = []
for i in range(0, 100):
    datos.append(i*i%40)
plt.plot(datos)
plt.xlabel('x')
plt.ylabel('x al cuadrado')
plt.show()