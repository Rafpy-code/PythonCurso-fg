'''
requirements.txt
tkinter
datetime
random
'''

import datetime
from tkinter import *
from tkinter import filedialog, messagebox
import random

# Variables globales y funciones
operador = ""

# Lista de productos y precios
lista_foods = ['ternera', 'cordero', 'pollo', 'coñejo', 'pescadífiri', 'pizza', 'mariscos', 'cuy']
precios_foods = [12.00, 15.00, 8.00, 14.00, 10.00, 7.00, 20.00, 18.00]
lista_drinks = ["Mate", "Sake", "Caipirinha", "Tequila", "Sangría", "Huarapo", "Chai", "Guinness"]
precios_drinks = [3.30, 6.75, 8.25, 7.00, 5.00, 4.00, 2.50, 6.50]
lista_desserts = ["Tarta de queso", "Tiramisu", "Baklava", "Mochi", "Pavlova", "Gulab Jamun", "Picarones", "Black Forest Cake"]
precios_desserts = [5.00, 6.50, 4.50, 3.50, 7.00, 4.00, 3.00, 6.00]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)

def total():
    global operador
    if operador != "":
        # Evaluar la expresión matemática
        try:
            # Evaluar la expresión matemática
            resultado = str(eval(operador))
        except ZeroDivisionError:
            resultado = "Error, división por cero"  # Mostrar "Error" en caso de división por cero
        visor_calculadora.delete(0, END)
        visor_calculadora.insert(0, resultado)
        operador = ""
    operador = ""

def revisar_check():
    x = 0
    for i in cuadros_food:
        if variables_food[x].get() == 1:
            cuadros_food[x].config(state=NORMAL)
            if cuadros_food[x].get() == "0":
                cuadros_food[x].delete(0, END)
            cuadros_food[x].focus()
        else:
            cuadros_food[x].config(state=DISABLED)
            texto_food[x].set("0")
        x += 1

    x = 0
    for i in cuadros_drink:
        if variables_drink[x].get() == 1:
            cuadros_drink[x].config(state=NORMAL)
            if cuadros_drink[x].get() == "0":
                cuadros_drink[x].delete(0, END)
            cuadros_drink[x].focus()
        else:
            cuadros_drink[x].config(state=DISABLED)
            texto_drink[x].set("0")
        x += 1

    x = 0
    for i in cuadros_dessert:
        if variables_dessert[x].get() == 1:
            cuadros_dessert[x].config(state=NORMAL)
            if cuadros_dessert[x].get() == "0":
                cuadros_dessert[x].delete(0, END)
            cuadros_dessert[x].focus()
        else:
            cuadros_dessert[x].config(state=DISABLED)
            texto_dessert[x].set("0")
        x += 1

def total_recibo():
    sub_total_food = 0
    x = 0
    for cantidad in texto_food:
        sub_total_food += (float(cantidad.get()) * precios_foods[x])
        x += 1
    print(sub_total_food)

    sub_total_drink = 0
    y = 0
    for cantidad in texto_drink:
        sub_total_drink += (float(cantidad.get()) * precios_drinks[y])
        y += 1
    print(sub_total_drink)

    sub_total_dessert = 0
    z = 0
    for cantidad in texto_dessert:
        sub_total_dessert += (float(cantidad.get()) * precios_desserts[z])
        z += 1
    print(sub_total_dessert)

    sub_total = sub_total_food + sub_total_drink + sub_total_dessert
    impuestos = sub_total * 0.07
    total = sub_total + impuestos

    variable_cost_food.set(f'€ {round(sub_total_food, 2)}')
    variable_cost_drink.set(f'€ {round(sub_total_drink, 2)}')
    variable_cost_dessert.set(f'€ {round(sub_total_dessert, 2)}')
    variable_subtotal.set(f'€ {round(sub_total, 2)}')
    variable_impuestos.set(f'€ {round(impuestos, 2)}')
    variable_total.set(f'€ {round(total, 2)}')

def imprimir_recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(1000, 9999)}'
    #fecha = f'{random.randint(1, 31)}/{random.randint(1, 12)}/{random.randint(2000, 2030)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}:{fecha.second}'
    
    texto_recibo.insert(END, f'''
==========================================
    Datos:       \t\t{num_recibo}
    Fecha:       \t\t{fecha_recibo}
==========================================
    Food:        \t\t{variable_cost_food.get():10}
    Drinks:      \t\t{variable_cost_drink.get():10}
    Desserts:    \t\t{variable_cost_dessert.get():10}
------------------------------------------
    Subtotal:    \t\t{variable_subtotal.get():10}
    Impuestos:   \t\t{variable_impuestos.get():10}
    Total:       \t\t{variable_total.get():10}
==========================================\n
    ''')

    texto_recibo.insert(END, 'Items\t\tCant.\tCosto/u\tCosto/t\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')

    c = 0
    for food in texto_food:
        if food.get() != "0":
            nombre_comida = lista_foods[c]
            cantidad_comida = food.get()
            precio_unidad = precios_foods[c]
            texto_recibo.insert(END, f'''
    {nombre_comida:.<30}X{cantidad_comida:>3}\t\t\t{precio_unidad:>6.2f}\t{(float(cantidad_comida)*precio_unidad):>6.2f}\n
            ''')
        c += 1

    c = 0
    for drink in texto_drink:
        if drink.get() != "0":
            nombre_bebida = lista_drinks[c]
            cantidad_bebida = drink.get()
            precio_unidad = precios_drinks[c]
            texto_recibo.insert(END, f'''
    {nombre_bebida:.<30}X{cantidad_bebida:>3}\t\t\t{precio_unidad:>6.2f}\t{(float(cantidad_bebida)*precio_unidad):>6.2f}\n
            ''')
        c += 1

    c = 0
    for dessert in texto_dessert:
        if dessert.get() != "0":
            nombre_postre = lista_desserts[c]
            cantidad_postre = dessert.get()
            precio_unidad = precios_desserts[c]
            texto_recibo.insert(END, f'''
    {nombre_postre:.<30}X{cantidad_postre:>3}\t\t\t{precio_unidad:>6.2f}\t{(float(cantidad_postre)*precio_unidad):>6.2f}
            ''')
        c += 1

    texto_recibo.insert(END, f'\n' + '-' * 75 + '\n')
    texto_recibo.insert(END, f'Costo de la comida: \t\t\t{variable_cost_food.get()}\n')
    texto_recibo.insert(END, f'Costo de las bebidas: \t\t\t{variable_cost_drink.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres: \t\t\t{variable_cost_dessert.get()}\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')
    texto_recibo.insert(END, f'Subtotal:  \t\t\t{variable_subtotal.get()}\n')
    texto_recibo.insert(END, f'Impuestos: \t\t\t{variable_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total: \t\t\t{variable_total.get()}\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')
    texto_recibo.insert(END, 'Gracias por su visita\n')
    texto_recibo.insert(END, f'-' * 75 + '\n')

def guardar_recibo():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Información', 'Recibo guardado correctamente')

def resetear():
    texto_recibo.delete(0.1, END)
    for text in texto_food:
        text.set('0')
    for text in texto_drink:
        text.set('0')
    for text in texto_dessert:
        text.set('0')

    for cuadro in cuadros_food:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_drink:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_dessert:
        cuadro.config(state=DISABLED)

    for check in variables_food:
        check.set(0)
    for check in variables_drink:
        check.set(0)
    for check in variables_dessert:
        check.set(0)

    variable_cost_food.set('')
    variable_cost_drink.set('')
    variable_cost_dessert.set('')
    variable_subtotal.set('')
    variable_impuestos.set('')
    variable_total.set('')
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, '')

# Iniciar tkinter
root = Tk()

# Tamaño de la ventana
root.geometry("1080x630+0+0")

# Evitar maximizar la ventana
root.resizable(False, False)

# Título de la ventana
root.title("Sistema de facturación - BarT Restaurant")

# Color de fondo
root.config(bg="orange")

# panel_top
panel_top = Frame(root, 
                  bg="orange", 
                  bd=5, 
                  relief=RIDGE)
panel_top.pack(side=TOP, 
               fill=X)

# Etiqueta título
label_title = Label(panel_top, 
                    text="Sistema de facturación", 
                    font=("Arial", 45, "bold"), 
                    bg="orange", 
                    fg="white", 
                    width=27)
label_title.grid(row=0, 
                 column=0)

# Panel izquierdo
panel_left = Frame(root, 
                   bd=1, 
                   relief=RIDGE)
panel_left.pack(side=LEFT)

# Panel costos
panel_cost = Frame(panel_left, 
                   bd=1, 
                   relief=RIDGE,
                   bg='black',
                   padx=55)
panel_cost.pack(side=BOTTOM)

# Panel comidas
panel_foods = LabelFrame(panel_left, 
                         text="Comidas", 
                         font=("Arial", 15, "bold"), 
                         bd=1, 
                         relief=RIDGE)
panel_foods.pack(side=LEFT)

# Panel bebidas
panel_drinks = LabelFrame(panel_left, 
                          text="Bebidas", 
                          font=("Arial", 15, "bold"), 
                          bd=1, 
                          relief=RIDGE)
panel_drinks.pack(side=LEFT)

# Panel postres
panel_desserts = LabelFrame(panel_left, 
                            text="Postres", 
                            font=("Arial", 15, "bold"), 
                            bd=1, 
                            relief=RIDGE)
panel_desserts.pack(side=LEFT)

# Panel derecho
panel_right = Frame(root, 
                    bd=1, 
                    relief=RIDGE)
panel_right.pack(side=RIGHT)

# Panel calculadora
panel_calc = Frame(panel_right, 
                   bd=1, 
                   relief=RIDGE)
panel_calc.pack()

# Panel recibo
panel_ticket = Frame(panel_right, 
                     bd=1, 
                     relief=RIDGE)
panel_ticket.pack()

# Panel botones
panel_buttons = Frame(panel_right, 
                      bd=1, 
                      relief=RIDGE)
panel_buttons.pack()


# Generar items de comidas
variables_food = []
cuadros_food = []
texto_food = []
contador = 0

# Podría usar enumerate
for food in lista_foods:
    # Crear checkbuttons
    variables_food.append('')
    variables_food[contador] = IntVar()
    food = Checkbutton(panel_foods, 
                       text=food.title(), 
                       font=("Arial", 12, "bold"), 
                       onvalue=1, 
                       offvalue=0, 
                       variable=variables_food[contador],
                       command=lambda: revisar_check())
    food.grid(row=contador, 
              column=0, 
              sticky=W) # sticky=W para alinear a la izquierda  

    # Crear cuadros de entrada
    cuadros_food.append('')
    texto_food.append('')
    texto_food[contador] = StringVar(value="0") # Valor por defecto
    
    cuadros_food[contador] = Entry(panel_foods, 
                                   font=("Arial", 12, "bold"), 
                                   bd=1, 
                                   width=6, 
                                   state=DISABLED, 
                                   textvariable=texto_food[contador])
    cuadros_food[contador].grid(row=contador,
                               column=1)  
    contador += 1

# Generar items de bebidas
variables_drink = []
cuadros_drink = []
texto_drink = []
contador = 0

for drink in lista_drinks:
    # Crear checkbuttons
    variables_drink.append('')
    variables_drink[contador] = IntVar()
    drink = Checkbutton(panel_drinks, 
                        text=drink.title(), 
                        font=("Arial", 12, "bold"), 
                        onvalue=1, 
                        offvalue=0, 
                        variable=variables_drink[contador],
                        command=lambda: revisar_check())
    drink.grid(row=contador, 
               column=0, 
               sticky=W) # sticky=W para alinear a la izquierda 

    # Crear cuadros de entrada
    cuadros_drink.append('')
    texto_drink.append('')
    texto_drink[contador] = StringVar(value="0") # Valor por defecto

    cuadros_drink[contador] = Entry(panel_drinks, 
                                   font=("Arial", 12, "bold"), 
                                   bd=1, 
                                   width=6, 
                                   state=DISABLED, 
                                   textvariable=texto_drink[contador])
    cuadros_drink[contador].grid(row=contador,
                               column=1)   
    contador += 1

# Generar items de postres
variables_dessert = []
cuadros_dessert = []
texto_dessert = []
contador = 0

for dessert in lista_desserts:
    # Crear checkbuttons
    variables_dessert.append('')
    variables_dessert[contador] = IntVar()
    dessert = Checkbutton(panel_desserts, 
                          text=dessert.title(), 
                          font=("Arial", 12, "bold"), 
                          onvalue=1, 
                          offvalue=0, 
                          variable=variables_dessert[contador],
                          command=lambda: revisar_check())
    dessert.grid(row=contador, 
                 column=0, 
                 sticky=W) # sticky=W para alinear a la izquierda  

    # Crear cuadros de entrada
    cuadros_dessert.append('')
    texto_dessert.append('')
    texto_dessert[contador] = StringVar(value="0") # Valor por defecto

    cuadros_dessert[contador] = Entry(panel_desserts, 
                                   font=("Arial", 12, "bold"), 
                                   bd=1, 
                                   width=6, 
                                   state=DISABLED, 
                                   textvariable=texto_dessert[contador])
    cuadros_dessert[contador].grid(row=contador,
                                   column=1)     
    contador += 1

# Lista de variables
variable_cost_food = StringVar()
variable_cost_drink = StringVar()
variable_cost_dessert = StringVar()
variable_subtotal = StringVar()
variable_impuestos = StringVar()
variable_total = StringVar()

# Etiquetas de costos y campos de entrada
# Etiquetas food
etiqueta_cost_food = Label(panel_cost,
                            text="Costo Comida",
                            font=("Arial", 12, "bold"),
                            bg="black",
                            fg="lawngreen")
etiqueta_cost_food.grid(row=0,
                        column=0,
                        padx=15)

texto_cost_food = Entry(panel_cost,
                        font=("Arial", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=variable_cost_food)
texto_cost_food.grid(row=0,
                     column=1,
                     padx=15)

# Etiquetas drink
etiqueta_cost_drink = Label(panel_cost,
                            text="Costo Bebidas",
                            font=("Arial", 12, "bold"),
                            bg="black",
                            fg="lawngreen")
etiqueta_cost_drink.grid(row=1,
                        column=0,
                        padx=15)

texto_cost_drink = Entry(panel_cost,
                        font=("Arial", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=variable_cost_drink)
texto_cost_drink.grid(row=1,
                     column=1,
                     padx=15)

# Etiquetas dessert
etiqueta_cost_dessert = Label(panel_cost,
                            text="Costo Postres",
                            font=("Arial", 12, "bold"),
                            bg="black",
                            fg="lawngreen")
etiqueta_cost_dessert.grid(row=2,
                        column=0,
                        padx=15)

texto_cost_dessert = Entry(panel_cost,
                        font=("Arial", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=variable_cost_dessert)
texto_cost_dessert.grid(row=2,
                     column=1,
                     padx=15)

# Etiquetas subtotal
etiqueta_cost_subtotal = Label(panel_cost,
                            text="Subtotal",
                            font=("Arial", 12, "bold"),
                            bg="black",
                            fg="lawngreen")
etiqueta_cost_subtotal.grid(row=0,
                        column=2,
                        padx=15)

texto_cost_subtotal = Entry(panel_cost,
                        font=("Arial", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=variable_subtotal)
texto_cost_subtotal.grid(row=0,
                     column=3,
                     padx=15)

# Etiquetas impuestos
etiqueta_cost_impuestos = Label(panel_cost,
                            text="Impuestos",
                            font=("Arial", 12, "bold"),
                            bg="black",
                            fg="lawngreen")
etiqueta_cost_impuestos.grid(row=1,
                        column=2,
                        padx=15)

texto_cost_impuestos = Entry(panel_cost,
                        font=("Arial", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=variable_impuestos)
texto_cost_impuestos.grid(row=1,
                     column=3,
                     padx=15)

# Etiquetas total
etiqueta_cost_total = Label(panel_cost,
                            text="TOTAL A PAGAR",
                            font=("Arial", 12, "bold"),
                            bg="black",
                            fg="lawngreen")
etiqueta_cost_total.grid(row=2,
                        column=2,
                        padx=15)

texto_cost_total = Entry(panel_cost,
                        font=("Arial", 12, "bold"),
                        bd=1,
                        width=10,
                        state="readonly",
                        textvariable=variable_total)
texto_cost_total.grid(row=2,
                     column=3,
                     padx=15)

# Botones ["Total", "Recibo", "Guardar", "Borrar"]
botones = ["Total", "Recibo", "Guardar", "Resetear"]
botones_creados = []
columna = 0

for boton in botones:
    boton = Button(panel_buttons,
           text=boton.title(),
           font=("Arial", 12, "bold"),
           fg="white",
           bg="black",
           bd=1,
           width=9)
    
    botones_creados.append(boton)

    boton.grid(row=0,
               column=columna)
    columna += 1

botones_creados[0].config(command=lambda: total_recibo())
botones_creados[1].config(command=lambda: imprimir_recibo())
botones_creados[2].config(command=lambda: guardar_recibo())
botones_creados[3].config(command=lambda: resetear())

# Área de recibo
texto_recibo = Text(panel_ticket,
                     font=("Arial", 12, "bold"),
                     bd=1,
                     width=42,
                     height=10)
texto_recibo.grid(row=0,
                  column=0,
                  columnspan=4)

# Calculadora
visor_calculadora = Entry(panel_calc,
                           font=("Arial", 16, "bold"),
                           bd=1,
                           width=32)

visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)

botones_calculadora = ["7", "8", "9", "+",
                        "4", "5", "6", "-",
                        "1", "2", "3", "*",
                        "CE", ".", "0", "/",
                        "Total"]

botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calc,
           text=boton.title(),
           font=("Arial", 12, "bold"),
           fg="white",
           bg="black",
           bd=1,
           width=8)
    if boton.cget("text") == "Total":
        boton = Button(panel_calc,
                       text="TOTAL",
                       font=("Arial", 12, "bold"),
                       fg="yellow",
                       bg="black",
                       bd=1,
                       width=30)
        boton.grid(row=5,
                   column=0,
                   columnspan=8)
    
    botones_guardados.append(boton)

    boton.grid(row=fila,
               column=columna)
    
    columna += 1
    if columna == 4:
        columna = 0
        fila += 1

# Dar funcionalidades a los botones
for i, texto in enumerate(botones_calculadora):
    if texto == "Total":
        botones_guardados[i].config(command=lambda: total())
    elif texto == "CE":
        botones_guardados[i].config(command=lambda: borrar())
    else:
        botones_guardados[i].config(command=lambda t=texto: click_boton(t))  # Configurar el comando del botón


# Evitar que se cierre la ventana (siempre al final)
root.mainloop()
