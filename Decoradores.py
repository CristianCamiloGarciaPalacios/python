"""Decorador sin usar @"""
# def funcion_b(a,b):
#     print(a+b)

# def funcion_a(funcion,a,b):
#     print("antes de b")
#     funcion(a,b)
#     print("despues de b")

# ejecuta = funcion_b

# funcion_a(ejecuta,5,10)

"""Decorador usando @"""
# def funcion_a(funcion):
#     def funcion_c():
#         print("antes de b")
#         funcion()
#         print("despues de b")
#     return funcion_c

# @funcion_a
# def funcion_b(): #funcion a decorar
#     print("Soy la funcion b")

# if True:
#     funcion_b()

"""Decorador usando @ y transfiriendo valores de variables"""
def funcion_a(funcion):
    def funcion_c(a,b):
        print("antes de")
        funcion(a,b)
        print("despues de")
    return funcion_c

@funcion_a
def funcion_b(a,b): #funcion a decorar
    print(a+b)

@funcion_a
def funcion_d(a,b): #funcion a decorar
    print(a-b)

if True:
    funcion_b(10,5)
    funcion_d(10,5)