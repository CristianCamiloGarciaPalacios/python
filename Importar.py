"""
Importar un modulo de un paquete:
"""
##Solo con importar el modulo Parcial1, del paquete Parciales, este se ejecuta inmediatamente
#import Parciales.Parcial1 
##No encontrara un modulo que se encuentre en un paquete exterior al del programa
##Cuando importas, se creara un paquete llamado __pycavhe__ automaticamente, en donde este el modulo del que importas
"""
Otra manera de importar un modulo de un paquete:
"""
#from Parciales import Parcial1
"""
Importar un metodo de un modulo:
"""
from Parciales.Parcial1 import Conteo_vocales