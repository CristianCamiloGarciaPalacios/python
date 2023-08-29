from itertools import count
from pickle import TRUE
import openpyxl

excel_document = openpyxl.load_workbook('python\Archivos/Tablas proyecto.xlsx')

sheet = excel_document['Tabla']
# PERSONA:
def datos_personas():
    multiple_cells = sheet['A3':'F88']
    for row in multiple_cells:
        i=0
        print("INSERT INTO persona Values(",end="")
        for cell in row:
            if(i==1 or i==2):
                print(f"\'{cell.value}\', ",end="")
            elif(i==5):
                print(f"\'{cell.value}\'",end="")
            else:
                print(cell.value,", ",end="")
            i = i+1
        print(");")

# CLIENTE:
def datos_clientes():
    multiple_cells = sheet['H3':'H72']
    for row in multiple_cells:
        print("INSERT INTO cliente Values(",end="")
        for cell in row:
            print(cell.value,end="")
        print(");")

# EMPLEADO:
def datos_empleados():
    multiple_cells = sheet['J3':'J18']
    for row in multiple_cells:
        print("INSERT INTO empleado Values(",end="")
        for cell in row:
            print(cell.value,end="")
        print(");")

# MOTO:
def datos_motos():
    multiple_cells = sheet['L3':'O72']
    for row in multiple_cells:
        i=0
        print("INSERT INTO moto Values(",end="")
        for cell in row:
            if(i==0 or i==1):
                print(f"\'{cell.value}\', ",end="")
            elif(i==3):
                print(cell.value,end="")
            else:
                print(cell.value,", ",end="")
            i = i+1
        print(");")

# SERVICIO:
def datos_servicios():
    multiple_cells = sheet['Q3':'T8']
    for row in multiple_cells:
        i=0
        print("INSERT INTO servicio Values(",end="")
        for cell in row:
            if(i==0 or i==1):
                print(f"\'{cell.value}\', ",end="")
            elif(i==3):
                print(cell.value,end="")
            else:
                print(cell.value,", ",end="")
            i = i+1
        print(");")

# CITA:
def datos_citas():
    multiple_cells = sheet['V3':'Y72']
    for row in multiple_cells:
        i=0
        print("INSERT INTO cita Values(",end="")
        for cell in row:
            if(i==0 or i==1 or i==2):
                print(f"\'{cell.value}\', ",end="")
            else:
                print(f"\'{cell.value}\'",end="")
            i = i+1
        print(");")

# CITA_HAS_SERVICIO:
def datos_cita_has_servicio():
    multiple_cells = sheet['AB3':'AC163']
    for row in multiple_cells:
        i=0
        print("INSERT INTO cita_has_servicio Values(",end="")
        for cell in row:
            if(i==0):
                print(f"\'{cell.value}\', ",end="")
            else:
                print(f"\'{cell.value}\'",end="")
            i = i+1
        print(");")

# EMPLEADOS_HAS_CITA:
def datos_empleado_has_cita():
    multiple_cells = sheet['AE3':'AF153']
    for row in multiple_cells:
        i=0
        print("INSERT INTO empleado_has_cita Values(",end="")
        for cell in row:
            if(i==0):
                print(f"\'{cell.value}\', ",end="")
            else:
                print(cell.value,end="")
            i = i+1
        print(");")

# PRODUCTO:
def datos_productos():
    multiple_cells = sheet['AH3':'AK19']
    for row in multiple_cells:
        i=0
        print("INSERT INTO producto Values(",end="")
        for cell in row:
            if(i==3):
                print(cell.value,end="")
            elif(i==0, i==1, i==2):
                print(f"\'{cell.value}\', ",end="")

            i = i+1
        print(");")

# VENTA:
def datos_ventas():
    multiple_cells = sheet['AM3':'AO53']
    for row in multiple_cells:
        i=0
        print("INSERT INTO venta Values(",end="")
        for cell in row:
            if(i==2):
                print(cell.value,end="")
            elif(i==1):
                print(cell.value,", ",end="")
            else:
                print(f"\'{cell.value}\', ",end="")
            i = i+1
        print(");")

# PRODUCTO_HAS_VENTA:
def datos_producto_has_venta():
    multiple_cells = sheet['AQ3':'AT116']
    for row in multiple_cells:
        i=0
        print("INSERT INTO producto_has_venta Values(",end="")
        for cell in row:
            if(i==3):
                print(cell.value,end="")
            elif(i==2):
                print(cell.value,", ",end="")
            else:
                print(f"\'{cell.value}\', ",end="")
            i = i+1
        print(");")
def main():
    while (TRUE):
        seleccion_datos = input("""Ingrese:
    1. persona
    2. cliente
    3. empleado
    4. moto
    5. servicio
    6. cita
    7. cita_has_servicio
    8. empleado_has_cita
    9. producto
    10. venta
    11. producto_has_venta
        """)
        if(seleccion_datos == "1"):
            datos_personas()
        elif(seleccion_datos == "2"):
            datos_clientes()
        elif(seleccion_datos == "3"):
            datos_empleados()
        elif(seleccion_datos == "4"):
            datos_motos()
        elif(seleccion_datos == "5"):
            datos_servicios()
        elif(seleccion_datos == "6"):
            datos_citas()
        elif(seleccion_datos == "7"):
            datos_cita_has_servicio()
        elif(seleccion_datos == "8"):
            datos_empleado_has_cita()
        elif(seleccion_datos == "9"):
            datos_productos()
        elif(seleccion_datos == "10"):
            datos_ventas()
        elif(seleccion_datos == "11"):
            datos_producto_has_venta()
        else:
            print("WTF MEN ._.")
            break

main()