"""
Crear una ventana:
"""
# from tkinter import ttk
# import tkinter as tk

# Ventana = tk.Tk()
# Ventana.iconbitmap('')
# Ventana.title('Titulo que muestra la ventana')
# Ventana.config(width=400, height=300)

# Ventana.mainloop()

"""
Usar cuadriculas con una ventana:
"""
# from tkinter import *

# Ventana = Tk()
# Ventana.iconbitmap('')
# Ventana.title('Grid con TKInter')
# for r in range(0,4):
#     for c in range (0, 5):
#         cell = Entry(Ventana, width = 10) #Entry es como un jframe de java
#         cell.grid(row = r, column = c)
#         cell.grid(padx=10, pady=10, ipadx=5, ipady=5) #pad es la distancia en pixeles entre celdas, ipad distancia en pixeles dentro de la celda 
#         cell.insert(0, f"{r}, {c}")

# Ventana.mainloop()

"""
Uso de Labels y Entrys en cuadricula:
"""
# from tkinter import ttk
# import tkinter as tk

# Ventana = tk.Tk()
# Ventana.iconbitmap('')
# Ventana.title('witgets en cuadricula')
# ttk.Label(Ventana, text="Nombre:").grid(pady=5,row=0,column=0)
# ttk.Label(Ventana, text="Apellido:").grid(pady=5,row=1,column=0)

# ttk.Entry(Ventana, width=40).grid(padx=5, row=0,column=1)
# ttk.Entry(Ventana, width=40).grid(padx=5, row=1,column=1)

# ttk.Button(Ventana, text="Aceptar", width=10).grid(padx=10, pady=10,
#                                                    row=2,column=0,
#                                                    columnspan=2)

# Ventana.mainloop()

"""
Uso pack:
"""
# from tkinter import ttk
# import tkinter as tk
# from calendar import month_name

# Ventana = tk.Tk()
# Ventana.geometry("300x200")
# Ventana.iconbitmap('')
# Ventana.title('Empaquetar con TKInter')

# Botonw = ttk.Button(Ventana, text="West", width=15)
# Botonw.pack(side='left') #pack enpaqueta un witget en un lado de la ventana side="top/bottom/left/right"

# BotonE = ttk.Button(Ventana, text="East", width=15)
# BotonE.pack(side='right')

# Lista = tk.Listbox(Ventana, width=10)
# Lista.pack(fill="both", expand=True)

# for i in range(1, 13):
#     Lista.insert(tk.END, month_name[i])

# Ventana.mainloop()

"""
Metodo place:
"""
# from tkinter import Label, ttk
# import tkinter as tk

# Ventana = tk.Tk()
# Ventana.geometry("300x300")
# Ventana.iconbitmap('')
# Ventana.title('PLACE con TKInter')


# Etiqueta1 = tk.Label(Ventana, text="Label (0, 0)", fg="white", bg="red")
# Etiqueta2 = tk.Label(Ventana, text="Label (0, 20)", fg="green", bg="white")
# Etiqueta3 = tk.Label(Ventana, text="Label (40, 50)", fg="black", bg="yellow")
# Etiqueta4 = tk.Label(Ventana, text="Label (0.5, 0.5)", fg="black", bg="green")

# Etiqueta1.place(x=0, y=0) #Posicion absoluta
# Etiqueta2.place(x=10, y=20) #Posicion absoluta
# Etiqueta3.place(x=40, y=50) #Posicion absoluta
# Etiqueta4.place(relx=0.5, rely=0.5) #Posicion relativa

# Ventana.mainloop()

"""
Labels en TKInter:
"""
# from tkinter import ttk
# import tkinter as tk

# Ventana = tk.Tk()
# Ventana.geometry("300x200")
# Ventana.resizable(False, False) #(false: no varia en x, false: no varia en y)
# Ventana.iconbitmap('')
# Ventana.title('Widget Label')

# #label con fuente especifica
# Label = ttk.Label(Ventana,
#                   text="Una etiqueta con letra helvética",
#                   font=("Helvetica", 14)
#                   )
# Label.pack(ipadx=10, ipady=10)

# Ventana.mainloop()
"""
Importar una imagen a un label:
"""
# from tkinter import ttk
# import tkinter as tk

# Ventana = tk.Tk()
# Ventana.geometry("500x500")
# Ventana.title('Widget Label Image')

# #Desplegar una imagen en un label
# if(1==2):
#     foto = tk.PhotoImage(file='llamada.png')
#     Label = ttk.Label(Ventana,
#                     image = foto,
#                     padding=5,
#                     compound='left')
#     Label.pack()
# else:
#     foto = tk.PhotoImage(file='llamada.png')
#     Label = ttk.Label(Ventana,
#                     image = foto,
#                     text="Meme llamada",
#                     underline=5,
#                     compound='bottom') #compound prioriza ponerlo en una direccion
#     Label.pack()
# Ventana.mainloop()
"""
Desplegar un entry:
"""
# from cgitb import text
# import email
# from tkinter import ttk
# import tkinter as tk

# Ventana = tk.Tk()
# Ventana.config(width=300, height=200)
# Ventana.resizable(False, False)
# #Ventana.geometry("300x200")
# Ventana.title('Widget Entry')

# Label = ttk.Label(Ventana, text="Digite lo que quiera:")
# Label.place(x=106, y=60)

# Entry = ttk.Entry(Ventana)
# Entry.place(x=100, y=80)

# Ventana.mainloop()

"""
Usar un entry:
"""
# from tkinter import ttk
# import tkinter as tk
# from tkinter.messagebox import showinfo

# def centrar(win):
#     """Centrar la venta a la mitad de la pantalla"""
#     win.update_idletasks()
#     width = win.winfo_width()
#     frm_width = win.winfo_rootx() - win.winfo_x()
#     win_width = width + 2 * frm_width
#     height = win.winfo_height()
#     titlebar_height = win.winfo_rooty() - win.winfo_y()
#     win_height = height + titlebar_height + frm_width
#     x = win.winfo_screenwidth() // 2 - win_width // 2
#     y = win.winfo_screenheight() // 2 - win_height // 2
#     win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
#     win.deiconify()

# def clicked():
#     """Funcion que se llama cuando se hace click"""
#     msg = f"El email es: {Email.get()}, y el password: {Password.get()}"
#     showinfo(title='Informacion ingresada', message=msg)

# Ventana = tk.Tk()
# Ventana.config(width=300, height=150)
# Ventana.resizable(False, False)
# Ventana.title('Entry con password')
# centrar(Ventana)

# Email = tk.StringVar() #Variable que se asocia con el entry
# Password = tk.StringVar() #Variable que se asocia con el entry

# Ventana_in = ttk.Frame(Ventana)
# Ventana_in.pack(padx=10, pady=10, fill='x', expand=True)

# # Email
# Email_label = ttk.Label(Ventana_in, text="Email:")
# Email_label.pack(fill='x', expand=True)
#     # fill='x' permite que llene todo el espacio que tenga en el eje x

# Email_entry = ttk.Entry(Ventana_in, textvariable=Email)
# Email_entry.pack(fill='x', expand=True)
# Email_entry.focus()

# # Password
# Password_label = ttk.Label(Ventana_in, text="Password:")
# Password_label.pack(fill='x', expand=True)

# Password_entry = ttk.Entry(Ventana_in, textvariable=Password, show="*")
#     # show="*" replaza todo caracter escrito por *
# Password_entry.pack(fill='x', expand=True)
# Password_entry.focus()

# # boton para login
# Boton_login = ttk.Button(Ventana_in, text="login", command=clicked)
# Boton_login.pack(fill='x', expand=True, pady=10)

# Ventana.mainloop()

"""
Metodo insert:
"""
# import tkinter as tk

# root = tk.Tk()
# root.geometry("200x100")

# Entry = tk.Entry(root)
# Entry.insert(0, "Default Text") # El 0  enucia desde que caracter escribir
# Entry.pack()
# # Entry.insert(5, "??")
# # Entry.pack()

# root.mainloop()

"""
Caja de texto numerica:
"""
# from tkinter import ttk
# import tkinter as tk

# def Cambio_de_temperatura():
#     temp = float(Spinbox_temp.get()[:4])
#     if temp <= 17:
#         consumo = "Bajo"
#     elif temp<=24:
#         consumo = "Medio"
#     elif temp <=30:
#         consumo = "Alto"
#     Etiqueta_consumo["text"] = f"Consumo de energia: {consumo}"


# Ventana = tk.Tk()
# Ventana.config(width=300, height=200)
# Ventana.title("Ejemplo de Spinbox")

# Etiqueta_temp = ttk.Label(text="Temperatura:")
# Etiqueta_temp.place(x=20, y=30, width=100)
# Etiqueta_consumo = ttk.Label()
# Etiqueta_consumo.place(x=20, y=80)

# Spinbox_temp = ttk.Spinbox(from_=10, to=30, increment=0.5, format="%.1f °C",
#                            command = Cambio_de_temperatura, wrap=False)
#                            # Wrap, permite (o no) que el valor mas chico, valla al mas grande
# Spinbox_temp.insert(0, "10.0 °C")
# Spinbox_temp["state"] = "readoly"
# Spinbox_temp.place(x=105, y=30, width=70)
# Cambio_de_temperatura() # Se llama para determinar el texto de Etiqueta_consumo al inicializar la ventana

# Ventana.mainloop()

"""
ComboBox:
"""
# from tkinter import ttk
# import tkinter as tk
# from calendar import month_name
# from tkinter.messagebox import showinfo

# Ventana = tk.Tk()
# Ventana.geometry("300x200")
# Ventana.resizable(False, False)
# Ventana.title('Combobox widget')

# Label = ttk.Label(text="Selecciona un mes:")
# Label.pack(fill=tk.X, padx=5, pady=5)

# # crea un combobox
# Mes_seleccionado = tk.StringVar()
# Meses = ttk.Combobox(Ventana, textvariable=Mes_seleccionado, state="readonly")

# # Crea una lista de cada mes
# Meses['values'] = [month_name[m] for m in range(1, 13)]
# Meses.pack(fill=tk.X, padx=5, pady=5)

# def mes_escogido(event):
#     showinfo(title="Resultado:", message=f"Escogido: {Mes_seleccionado.get()[:3]}")

# # Tan pronto se selecciona un elemento del combobox (<<ComboboxSelected>>) se da paso al metodo mes_escogido()
# Meses.bind("<<ComboboxSelected>>", mes_escogido)

# Ventana.mainloop()

"""
Notebook:
"""
from tkinter import ttk
import tkinter as tk

class FrameSaludar(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Entry_nombre = ttk.Entry(self)
        self.Entry_nombre.pack(pady=10)

        self.Boton_saludo = ttk.Button(self, text="Saludar", command=self.Saludar)
        self.Boton_saludo.pack(pady=10)

        self.Label_saluda = ttk.Label(self)
        self.Label_saluda.pack()

    def Saludar(self):
        self.Label_saluda['text'] = f"Hola, {self.Entry_nombre.get()}"

class FrameAcerca(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.Label = ttk.Label(self, text="Visitanos en la pagina web, con más informacion")
        self.Label.pack()

        self.Boton_web = ttk.Button(self, text="Ir a la pagina web")
        self.Boton_web.pack(pady=11)

        self.Boton_blog = ttk.Button(self, text="Ir al blog")
        self.Boton_blog.pack()

class Aplication(ttk.Frame):
    def __init__(self, Ventana_principal):
        super().__init__(Ventana_principal)
        Ventana_principal.geometry("360x200")
        Ventana_principal.resizable(False, False)
        Ventana_principal.title("Frame con pantallas en TKInter")

        self.Notebook = ttk.Notebook(self)
        self.Saludo_frame = FrameSaludar(self.Notebook)
        self.Notebook.add(self.Saludo_frame, text="Saludar", padding=10)

        self.About_frame = FrameAcerca(self.Notebook)
        self.Notebook.add(self.About_frame, text="Acerca de...", padding=10)

        self.Notebook.pack(padx=10, pady=10)
        self.pack()

Ventana_principal = tk.Tk()
app = Aplication(Ventana_principal) # Crea el objeto a partir de la clase
app.mainloop()