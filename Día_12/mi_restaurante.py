from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador = ''


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0, END)


def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ''


def revisar_check():
    x = 0
    for c in cuadro_comidas:
        if variables_comida[x].get() == 1:
            cuadro_comidas[x].config(state=NORMAL)
            if cuadro_comidas[x].get == '0':
                cuadro_comidas[x].delete(0, END)
            cuadro_comidas[x].focus()
        else:
            cuadro_comidas[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1

    x = 0
    for b in cuadro_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadro_bebidas[x].config(state=NORMAL)
            if cuadro_bebidas[x].get() == '0':
                cuadro_bebidas[x].delete(0, END)
            cuadro_bebidas[x].focus()
        else:
            cuadro_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set('0')
        x += 1

    x = 0
    for p in cuadro_postres:
        if variables_postres[x].get() == 1:
            cuadro_postres[x].config(state=NORMAL)
            if cuadro_postres[x].get() == '0':
                cuadro_postres[x].delete(0, END)
            cuadro_postres[x].focus()
        else:
            cuadro_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1


precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def total():
    sub_total_comida = 0
    p = 0
    for cantidad in texto_comida:
        sub_total_comida = sub_total_comida + (float(cantidad.get()) * precios_comida[p])
        p += 1

    sub_total_bebida = 0
    p = 0
    for cantidad in texto_bebidas:
        sub_total_bebida = sub_total_bebida + (float(cantidad.get()) * precios_bebida[p])
        p += 1

    sub_total_postres = 0
    p = 0
    for cantidad in texto_postres:
        sub_total_postres = sub_total_postres + (float(cantidad.get()) * precios_postres[p])
        p += 1

    impuestos = (sub_total_comida + sub_total_bebida + sub_total_postres) * 0.21
    var_costo_comida.set(f'${round((sub_total_comida),2)}')
    var_costo_bebidas.set(f'${round((sub_total_bebida),2)}')
    var_costo_postres.set(f'${round((sub_total_postres),2)}')
    var_subtotal.set(f'${round((sub_total_comida + sub_total_bebida + sub_total_postres),2)}')
    var_impuestos.set(f'${round(impuestos, 2)}')
    var_total.set(f'${round(((sub_total_comida + sub_total_bebida + sub_total_postres) + impuestos), 2)}')


def recibo():
    texto_recibo.delete(1.0, END)
    num_recibo = f'N# - {random.randint(100, 999)}'
    fecha = datetime.datetime.now()
    fecha_recibo = f'{fecha.day}/{fecha.month}/{fecha.year}  -  {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos: {num_recibo}\t\t {fecha_recibo}\n')
    texto_recibo.insert(END, f'*' * 50 + '\n')
    texto_recibo.insert(END, f'Items\t\tCant.\tCosto\n')
    texto_recibo.insert(END, f'-' * 63 + '\n')

    x = 0
    for comida in texto_comida:
        if comida.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_comidas[x]}\t\t{comida.get()}\t${round((precios_comida[x] * int(comida.get())),2)}''\n')
        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_bebidas[x]}\t\t{bebida.get()}\t${round((precios_bebida[x] * int(bebida.get())),2)}''\n')
        x += 1

    x = 0
    for postre in texto_postres:
        if postre.get() != '0':
            texto_recibo.insert(END,
                                f'{lista_postres[x]}\t\t{postre.get()}\t${round((precios_postres[x] * int(postre.get())),2)}''\n')
        x += 1
    texto_recibo.insert(END, f'-' * 63 + '\n')
    texto_recibo.insert(END, f'consumo comida\t\t\t{var_costo_comida.get()}\n')
    texto_recibo.insert(END, f'consumo bebida\t\t\t{var_costo_bebidas.get()}\n')
    texto_recibo.insert(END, f'consumo postres\t\t\t{var_costo_postres.get()}\n')
    texto_recibo.insert(END, f'-' * 63 + '\n')
    texto_recibo.insert(END, f'subtotal\t\t\t{var_subtotal.get()}\n')
    texto_recibo.insert(END, f'impuestos\t\t\t{var_impuestos.get()}\n')
    texto_recibo.insert(END, f'Total\t\t\t{var_total.get()}\n')


def guardar():
    info_recibo= texto_recibo.get(1.0,END)
    archivo=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Informacion','Recibo creado')

def reset():
    texto_recibo.delete(0.1,END)

    for texto in texto_comida:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set('0')
    for texto in texto_postres:
        texto.set('0')

    for cuadro in cuadro_comidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadro_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set(0)
    for v in variables_bebidas:
        v.set(0)
    for v in variables_postres:
        v.set(0)

    var_costo_comida.set('')
    var_costo_bebidas.set('')
    var_costo_postres.set('')
    var_subtotal.set('')
    var_impuestos.set('')
    var_total.set('')

# iniciar tkinter


aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1020x630+0+0')

# evitar maximizar

aplicacion.resizable(False, False)

# titulo de la ventana
aplicacion.title('Mi Restaurante - Sistema de Facturacion')

# color de fondo de la ventanda
aplicacion.config(bg='burlywood')

# panel superior
panel_superior = Frame(aplicacion, bd=1, relief=FLAT)
panel_superior.pack(side=TOP)

# etiqueta titulo
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturacion', fg='azure4',
                        font=('Dosis', 50), bg='burlywood', width=27, justify='center')

etiqueta_titulo.grid(row=0, column=0)

# panel izq

panel_izq = Frame(aplicacion, bd=1, relief=FLAT)
panel_izq.pack(side=LEFT)

# panel derecha

panel_der = Frame(aplicacion, bd=1, relief=FLAT, )
panel_der.pack(side=RIGHT)

# panel calculadora
panel_calculadora = Frame(panel_der, bd=1, relief=FLAT, bg='burlywood')
panel_calculadora.pack()

# panel recibo
panel_recibo = Frame(panel_der, bd=1, relief=FLAT, bg='burlywood')
panel_recibo.pack()

# panel botones
panel_botones = Frame(panel_der, bd=1, relief=FLAT, bg='burlywood')
panel_botones.pack()

# panel costos

panel_costos = Frame(panel_izq, bd=1, relief=FLAT, bg='azure4', padx=100)
panel_costos.pack(side=BOTTOM)

# panel comidas
panel_comidas = LabelFrame(panel_izq, text='Comida', font=('Dosis', 17, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_comidas.pack(side=LEFT)

# panel bebidas
panel_bebidas = LabelFrame(panel_izq, text='Bebidas', font=('Dosis', 17, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_bebidas.pack(side=LEFT)

# panel postres
panel_postres = LabelFrame(panel_izq, text='Postres', font=('Dosis', 17, 'bold'),
                           bd=1, relief=FLAT, fg='azure4')
panel_postres.pack(side=LEFT)

# lista de productos
lista_comidas = ['Pollo', 'Cordero', 'Kebab', 'Pizza', 'Atun', 'Hamburguesa', 'Empanadas', 'Milanesa']
lista_bebidas = ['Agua', 'Fanta', 'Coca-Cola', 'Pepsi', 'Jugo', 'Soda', 'Cerveza', 'Vodka']
lista_postres = ['Helado', 'Fruta', 'Brownies', 'Flan', 'Alfajor', 'Torta', 'Gomitas', 'Chocolates']

# generar items comida, bebida, postres
variables_comida = []
cuadro_comidas = []
texto_comida: list = []
contador = 0

for comida in lista_comidas:
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         font=('Dosis', 13, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de comida
    cuadro_comidas.append('')
    texto_comida.append('')
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')

    cuadro_comidas[contador] = Entry(panel_comidas,
                                     font=('Dosis', 13, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadro_comidas[contador].grid(row=contador,
                                  column=1)
    contador += 1

variables_bebidas = []
cuadro_bebidas = []
texto_bebidas: list = []
contador = 0
for bebida in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         font=('Dosis', 13, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebidas[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de bebidas
    cuadro_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')

    cuadro_bebidas[contador] = Entry(panel_bebidas,
                                     font=('Dosis', 13, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[contador])
    cuadro_bebidas[contador].grid(row=contador,
                                  column=1)
    contador += 1

variables_postres = []
cuadro_postres = []
texto_postres: list = []
contador = 0
for postre in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         font=('Dosis', 13, 'bold'),
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postres[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de postrees
    cuadro_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')

    cuadro_postres[contador] = Entry(panel_postres,
                                     font=('Dosis', 13, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadro_postres[contador].grid(row=contador,
                                  column=1)

    contador += 1

# etiquetas de costo y campos de entrada COMIDAS
# variables de costos
var_subtotal = StringVar()
var_subtotal.set('0')
var_impuestos = StringVar()
var_impuestos.set('0')
var_total = StringVar()
var_total.set('0')

# variables COMIDA
var_costo_comida = StringVar()
var_costo_comida.set('0')

etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Dosis', 12, 'bold'),
                              bg='azure4',
                              fg='white')

etiqueta_costo_comida.grid(row=0, column=0)

texto_costo_comida = Entry(panel_costos,
                           font=('Dosis', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
texto_costo_comida.grid(row=0, column=1, padx=41)

# etiquetas de costo y campos de entrada BEBIDAS

# variables costo bebidas
var_costo_bebidas = StringVar()
var_costo_bebidas.set('0')

etiqueta_costo_bebidas = Label(panel_costos,
                               text='Costo Bebidas',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_costo_bebidas.grid(row=1, column=0)

texto_costo_bebidas = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_bebidas)
texto_costo_bebidas.grid(row=1, column=1, padx=41)

# etiquetas de costo y campos de entrada POSTRES

# variables POSTRES
var_costo_postres = StringVar()
var_costo_postres.set('0')

etiqueta_costo_postres = Label(panel_costos,
                               text='Costo postres',
                               font=('Dosis', 12, 'bold'),
                               bg='azure4',
                               fg='white')

etiqueta_costo_postres.grid(row=2, column=0)

texto_costo_postres = Entry(panel_costos,
                            font=('Dosis', 12, 'bold'),
                            bd=1,
                            width=10,
                            state='readonly',
                            textvariable=var_costo_postres)
texto_costo_postres.grid(row=2, column=1, padx=41)

# estiqueta subtotal
etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Dosis', 12, 'bold'),
                          bg='azure4',
                          fg='white')

etiqueta_subtotal.grid(row=0, column=2)

texto_subtotal = Entry(panel_costos,
                       font=('Dosis', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
texto_subtotal.grid(row=0, column=3, padx=41)

# etiqueta impuestos
etiqueta_impuestos = Label(panel_costos,
                           text='Impuestos',
                           font=('Dosis', 12, 'bold'),
                           bg='azure4',
                           fg='white')

etiqueta_impuestos.grid(row=1, column=2)

texto_impuestos = Entry(panel_costos,
                        font=('Dosis', 12, 'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=var_impuestos)
texto_impuestos.grid(row=1, column=3, padx=41)

# etiqueta TOTAL
etiqueta_total = Label(panel_costos,
                       text='Total',
                       font=('Dosis', 12, 'bold'),
                       bg='azure4',
                       fg='white')

etiqueta_total.grid(row=2, column=2)

texto_total = Entry(panel_costos,
                    font=('Dosis', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
texto_total.grid(row=2, column=3, padx=41)

# BOTONES

lista_botones = ['Total', 'Recibo', 'Guardar', 'Resetear']
botones_creados = []
columnas = 0

for boton in lista_botones:
    botones = Button(panel_botones,
                     text=boton.title(),
                     font=('Dosis', 9, 'bold'),
                     fg='white',
                     bg='azure4',
                     bd=1,
                     width=8
                     )
    botones_creados.append(botones)
    botones.grid(row=0, column=columnas)
    columnas += 1
botones_creados[0].config(command=total)

botones_creados[1].config(command=recibo)

botones_creados[2].config(command=guardar)

botones_creados[3].config(command=reset)
# ubicar el panel de RECIBO
texto_recibo = Text(panel_recibo,
                    font=('Dosis', 9, 'bold'),
                    bd=1,
                    width=36,
                    height=10
                    )

texto_recibo.grid(row=0, column=0)

# area calculadora
# visor calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Dosis', 9, 'bold'),
                          bd=1,
                          width=36

                          )
visor_calculadora.grid(row=0, column=0, columnspan=4)

# botones de la  calculadora
botones_calculadora = ['7', '8', '9', '+', '4', '5',
                       '6', '-', '1', '2', '3',
                       'x', '=', 'Del', '0', '/']

# botones guardados
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton_calculadora = Button(panel_calculadora,
                               text=boton.title(),
                               font=('Dosis', 9, 'bold'),
                               bd=1,
                               fg='white',
                               bg='RoyalBlue3',
                               width=8
                               )
    botones_guardados.append(boton_calculadora)
    boton_calculadora.grid(row=fila,
                           column=columna,

                           )

    if columna == 3:
        fila += 1

    columna += 1

    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda: click_boton('7'))
botones_guardados[1].config(command=lambda: click_boton('8'))
botones_guardados[2].config(command=lambda: click_boton('9'))
botones_guardados[3].config(command=lambda: click_boton('+'))
botones_guardados[4].config(command=lambda: click_boton('4'))
botones_guardados[5].config(command=lambda: click_boton('5'))
botones_guardados[6].config(command=lambda: click_boton('6'))
botones_guardados[7].config(command=lambda: click_boton('-'))
botones_guardados[8].config(command=lambda: click_boton('1'))
botones_guardados[9].config(command=lambda: click_boton('2'))
botones_guardados[10].config(command=lambda: click_boton('3'))
botones_guardados[11].config(command=lambda: click_boton('*'))
botones_guardados[12].config(command=obtener_resultado)
botones_guardados[13].config(command=borrar)
botones_guardados[14].config(command=lambda: click_boton('0'))
botones_guardados[15].config(command=lambda: click_boton('/'))

# evitar que la pantalla se cierre

aplicacion.mainloop()
