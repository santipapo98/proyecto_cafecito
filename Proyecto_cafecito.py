import tkinter as tk
from tkinter.ttk import *
import psycopg2
root= tk.Tk()

# HACER EL ELIMINAR Y EL UPDATE

canvas1 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
canvas1.pack()
label1 = tk.Label(root, text='Login Tienda')
label1.config(font=('helvetica', 14))
canvas1.create_window(200, 25, window=label1)

label3 = tk.Label(root, text='Usuario :')
label3.config(font=('helvetica', 8))
canvas1.create_window(110, 70, window=label3)

label4 = tk.Label(root, text='Contrasena :')
label4.config(font=('helvetica', 8))
canvas1.create_window(100, 140, window=label4)  

entry1 = tk.Entry(root) 
canvas1.create_window(200, 70, window=entry1)

entry2 = tk.Entry (root) 
canvas1.create_window(200, 140, window=entry2)
entry2.config(show="*")

def reporte():
    con = psycopg2.connect(
        host = 'localhost',
        database = 'prueba_python',
        user = 'postgres',
        password = 'santipapo98'
        )
    cur= con.cursor()
    consultar_datos="Select * from productos"
    cur.execute(consultar_datos)
    datos= cur.fetchall()
    print(datos)
    contador_cafe=0
    acom_ventas=0
    for dato in datos:
        if 'Cafe' in dato:
            contador_cafe+=1
            acom_ventas +=dato[1]
    print(acom_ventas)    
    print(contador_cafe)
    contador_cafe=0
    acom_ventas=0
    cur.close()
    con.close()

def agregar_cafe():
    con = psycopg2.connect(
        host = 'localhost',
        database = 'prueba_python',
        user = 'postgres',
        password = 'santipapo98'
        )
    cur= con.cursor()
    insertar_producto="Insert into productos(nombre_producto,precio_producto) values ((%s),(%s))"
    datos_producto=('Cafe',700)
    cur.execute(insertar_producto,datos_producto)
    con.commit()
    cur.close()
    con.close()

def agregar_aromatica():
    con = psycopg2.connect(
        host = 'localhost',
        database = 'prueba_python',
        user = 'postgres',
        password = 'santipapo98'
        )
    cur= con.cursor()
    insertar_producto="Insert into productos(nombre_producto,precio_producto) values ((%s),(%s))"
    datos_producto=('Aromatica',700)
    cur.execute(insertar_producto,datos_producto)
    con.commit()
    cur.close()
    con.close()

def agregar_poker():
    con = psycopg2.connect(
        host = 'localhost',
        database = 'prueba_python',
        user = 'postgres',
        password = 'santipapo98'
        )
    cur= con.cursor()
    insertar_producto="Insert into productos(nombre_producto,precio_producto) values ((%s),(%s))"
    datos_producto=('Poker',2000)
    cur.execute(insertar_producto,datos_producto)
    con.commit()
    cur.close()
    con.close()

def pagina_principal():
    principal = tk.Canvas(root, width = 1360, height = 720,  relief = 'raised')
    principal.pack()
    nombre_tienda = tk.Label(root, text='Tienda Chingona que vende Cafes y Weas')
    nombre_tienda.config(font=('helvetica', 22))
    principal.create_window(650, 25, window=nombre_tienda)

    boton_cafe = tk.Button(text='Cafe!',image='/Imagenes/cafe.png',command=agregar_cafe)
    principal.create_window(200, 220, window=boton_cafe, width=200, height=200)

    boton_aromatica = tk.Button(text='Aromatica!', bg='#EDCC98',command=agregar_aromatica)
    principal.create_window(700, 220, window=boton_aromatica, width=200, height=200)

    boton_poker = tk.Button(text='Poker!', bg='#EDCC98',command=agregar_poker)
    principal.create_window(1200, 220, window=boton_poker, width=200, height=200)

    boton_reporte = tk.Button(text='Reporte!', bg='#EDCC98',command=reporte)
    principal.create_window(700, 500, window=boton_reporte, width=200, height=200)

pagina_principal()

def verificar_datos():
    con = psycopg2.connect(
        host = 'localhost',
        database = 'prueba_python',
        user = 'postgres',
        password = 'santipapo98'
        )
    cur= con.cursor()
    consulta_datos="Select contrasena from login where login.nombre = (%s);"
    nombre=(entry1.get(),)
    cur.execute(consulta_datos,nombre)
    contrasena=cur.fetchone()
    if(contrasena):
        contra=contrasena[0]
        if(entry2.get()==contra):
            canvas1.pack_forget()
            pagina_principal()
        else:
            print("La contrasena es incorrecta !")
    else:
        print("El usuario No existe") 
    cur.close()
    con.close()
    

def registro():
    canvas1.pack_forget()
    canvas2 = tk.Canvas(root, width = 400, height = 300,  relief = 'raised')
    canvas2.pack()
    label2 = tk.Label(root, text='El Registro mas Sapo Perro')
    label2.config(font=('helvetica', 14))
    canvas2.create_window(200, 25, window=label2)
    label5 = tk.Label(root, text='Usuario :')
    label5.config(font=('helvetica', 8))
    canvas2.create_window(110, 70, window=label5)
    label6 = tk.Label(root, text='Contrasena :')
    label6.config(font=('helvetica', 8))
    canvas2.create_window(100, 140, window=label6)
    label7 = tk.Label(root, text='Confirmar Contrasena :')
    label7.config(font=('helvetica', 8))
    canvas2.create_window(75, 210, window=label7)
    entry3 = tk.Entry (root) 
    canvas2.create_window(200, 70, window=entry3)
    entry4 = tk.Entry (root) 
    canvas2.create_window(200, 140, window=entry4)
    entry4.config(show="*")
    entry5 = tk.Entry (root) 
    canvas2.create_window(200, 210, window=entry5)
    entry5.config(show="*")
    def registrar():
        if(entry4.get()!=entry5.get()):
            print("Las constrasenas no son iguales !")
            return
        con = psycopg2.connect(
        host = 'localhost',
        database = 'prueba_python',
        user = 'postgres',
        password = 'santipapo98'
        )
        cur= con.cursor()
        consulta_nombres="Select nombre from login;"
        cur.execute(consulta_nombres)
        nombres=cur.fetchall()
        if(entry3.get()=='' or entry4.get()==''):
            print('Se deben llenar ambos campos !')
            cur.close()
            con.close()
            return
        for nombre in nombres:
            if(entry3.get() in nombre):
                print("Usuario no disponible (Se complica a lo marica)")
                cur.close()
                con.close()
                return  
        ingresar_usuario="Insert into login(nombre,contrasena) values ((%s),(%s))"
        nombre_contra=(entry3.get(),entry4.get())
        cur.execute(ingresar_usuario,nombre_contra)
        con.commit()
        print('Usuario Registrado con Exito')
        cur.close()
        con.close()
        canvas2.pack_forget()
        canvas1.pack()
    button3 = tk.Button(text='Registrarse', command=registrar)
    canvas2.create_window(200, 260, window=button3)
    
        
button1 = tk.Button(text='Login', command=verificar_datos)
canvas1.create_window(200, 180, window=button1)

button2 = tk.Button(text='Aun no tienes Usuario ?', command=registro)
canvas1.create_window(200, 220, window=button2)


root.mainloop()