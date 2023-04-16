import tkinter as tk
from PIL import Image, ImageTk

# Crear una nueva ventana
ventana = tk.Tk()
ventana.geometry("250x250")

# Crear un Canvas del mismo tamaño que la ventana
canvas = tk.Canvas(ventana, width=250, height=250)
canvas.pack()


imagen_fondo = Image.open('C:/Users/Sumir/Documents/XoQ2Mx0.png')

imagen_fondo = ImageTk.PhotoImage(imagen_fondo)

canvas.create_image(0, 0, anchor='nw', image=imagen_fondo)

def suma():
    resultado = float(num1.get()) + float(num2.get())
    texto.config(text=f"El resultado es {resultado}")

def resta():
    resultado = float(num1.get()) - float(num2.get())
    texto.config(text=f"El resultado es {resultado}")

def division():
    resultado = float(num1.get()) / float(num2.get())
    texto.config(text=f"El resultado es {resultado}")

def multiplicación():
    resultado = float(num1.get()) * float(num2.get())
    texto.config(text=f"El resultado es {resultado}")

def potencia():
    resultado = float(num1.get()) ** float(num2.get())
    texto.config(text=f"El resultado es {resultado}")

marco1 = tk.Frame(ventana)
marco1.place(x=170, y=100)

operaciones = ["Suma", "Resta", "División", "Multiplicación", "Potencia"]
opcion_seleccionada = tk.StringVar(ventana)
opcion_seleccionada.set(operaciones[0])

menu = tk.OptionMenu(marco1, opcion_seleccionada, *operaciones)
menu.pack()

num1 = tk.Entry(ventana)
num1.pack()
num1.place(x=30, y=100)

num2 = tk.Entry(ventana)
num2.pack()
num2.place(x=30, y=120)

titulo =tk.Label(text="Bienvenid@ a la calculadora\nepica de Anette")
titulo.pack()
titulo.place(x=50, y=30)


texto = tk.Label(ventana, text="")
texto.pack()
texto.place(x=70, y=150)

boton = tk.Button(ventana, text="Calcular")
boton.pack()
boton.place(x=100, y=180)

boton.config(command=suma)

def cambiar_funcion(*args):
    if opcion_seleccionada.get() == "Suma":
        boton.config(command=suma)
    elif opcion_seleccionada.get() == "Resta":
        boton.config(command=resta)
    elif opcion_seleccionada.get() == "División":
        boton.config(command=division)
    elif opcion_seleccionada.get() == "Multiplicación":
        boton.config(command=multiplicación)
    elif opcion_seleccionada.get() == "Potencia":
        boton.config(command=potencia)

opcion_seleccionada.trace("w", cambiar_funcion)

ventana.mainloop()
