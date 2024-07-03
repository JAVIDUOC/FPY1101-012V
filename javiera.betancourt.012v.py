import os
import time
import csv
limpiarpantalla="cls"
catpremium={}
menu=True
rutas_lista ={'san bernardo':1,'el bosque':2,'buin':3}
def registrar_pedido():
    print("***REGISTRAR PEDIDO***")
    nropedido=input("ingrese el numero de pedido: ")
    cliente=input("ingrese su nombre: ")
    direccion=input("ingrese su direccion: ")
    sector=input("ingrese su comuna: ")
    saco5kg=input("¿cuantos sacos de 5KG necesita?: ")
    saco10kg=input("¿cuantos sacos de 10KG necesita?: ")
    saco20kg=input("¿cuantos sacos de 20KG necesita?: ")
    menu=True

    os.system(limpiarpantalla)
    catpremium=nropedido
    catpremium=cliente
    catpremium=direccion
    catpremium=sector
    catpremium=saco5kg
    catpremium=saco10kg
    catpremium=saco20kg
    catpremium=list(catpremium)

def listarpedido():
    if len (catpremium)==0:
        print("no hay datos para listar")
        menu=True
    else:
        print(catpremium)
        time.sleep(4)
        menu=True

def hojaderuta():
    print("estas son las rutas disponibles ")
    print(rutas_lista)
    resp=input("¿que sector desea su pedido?: ")
    menu=True

def salirdelprograma():
    print("usted esta saliendo del programa ")
    time.sleep(3)
    

while menu==True:
    print("BIENBENIDO A CAT PREMIUM")
    print("1.Registrar pedido ")
    print("2.Listar todos los pedidos ")
    print("3.Imprimir hoja de ruta ")
    print("4.Salir del programa ")
    menu=False  
    try:
        respmenu=int(input("¿que opcion desea? "))
    except ValueError:
        print("ingrese una opcion valida")
        os.system(limpiarpantalla)
        menu=True

if respmenu==1:
    registrar_pedido()
if respmenu==2:
    listarpedido()
elif respmenu==3:
    hojaderuta()
else:
    salirdelprograma()