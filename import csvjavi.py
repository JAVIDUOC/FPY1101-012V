import csv
import time
import os
trabajadores=[]
menu=True
limpiarpantalla="cls"

def registrartrabajador():
    print("***REGISTRAR UN NUEVO TRABAJADOR***")
    nombre=input("ingrese su nombre: ")
    apellido=input("ingrese su apellido: ")
    cargo=input("ingrese su cargo: ")
    while True:
        try:
            sueldo_bruto=float(input("ingrese su sueldo"))
            break
        except ValueError:
            print("error, ingrese un valor numerico para el saldo bruto")
    descuento_salud=sueldo_bruto*0.07
    descuentoafp=sueldo_bruto*0.12
    sueldo_liquido=sueldo_bruto-descuento_salud-descuentoafp

    trabajadores.append=({
        "nombre":nombre,
        "apellido":apellido,
        "cargo":cargo,
        "sueldo bruto":sueldo_bruto,
        "descuento afp":descuentoafp,
        "descuento_salud":descuento_salud,
        "sueldo liquido":sueldo_bruto-descuentoafp-descuento_salud
    })

    print("trabajador registrado exitosamente")
    time.sleep(5)

def listar_datos():
    os.system(limpiarpantalla)
    print("***DATOS INGRESADOS***")
    if len (trabajadores)==0:
        print("no hay datos para mostrar")
    else:
        for idx, trabajador in enumerate(trabajadores, start=1):
            print(f"Trabajador: {idx}")
            print(f"nombre: {trabajador[1]}")
            print(f"apellido: {trabajador[2]}")
            print(f"cargo: {trabajador[3]}")
            print(f"sueldo bruto: {trabajador[4]}")
            print(f"descuento afp: {trabajador[5]}")
            print(f"descuento salud: {trabajador[6]}")
            print(f"liquido a pagar: {trabajador[7]}")
            time.sleep(4)
            menu=True
def imprimir_planilla_desueldos():
    print("***imprimir plantilla de sueldos***")
    cargos_disponibles=["ceo","desarrollador","analista de datos"]
    print("cargos disponibles: ", cargos_disponibles)
    cargo_seleccionado=input("ingrese el cargo para imprimit pantalla (o 'todos' para imprimir todos): ").upper()
    
    if cargo_seleccionado=='TODOS':
        planilla_fil="plantilla.txt"
        with open(planilla_fil, 'w') as file:
            file.write(f"Planilla de Sueldos - Cargo: {cargo_seleccionado}\n")
            file.write("-------------------------------------------------\n")
            for trabajador in trabajadores:
                if trabajador['Cargo'] == cargo_seleccionado:
                    file.write(f"nombre: {trabajador[1]}\n")
                    file.write(f"apellido: {trabajador[2]}\n")
                    file.write(f"cargo: {trabajador[3]}\n")
                    file.write(f"sueldo bruto: {trabajador[4]}\n")
                    file.write(f"descuento afp: {trabajador[5]}\n")
                    file.write(f"descuento salud: {trabajador[6]}\n")
                    file.write(f"liquido a pagar: {trabajador[7]}\n")
        print(f"se ha generado el archivo '{planilla_fil}' con exito.")
    elif cargo_seleccionado in cargos_disponibles:
        planilla_filename=f"planilla_{cargo_seleccionado.lower().replace(' ', '_')}.txt"
        with open (planilla_filename,'w')as file:
            file.write(f"Planilla de Sueldos - Cargo: {cargo_seleccionado}\n")
            file.write("-------------------------------------------------\n")
            for trabajador in trabajadores:
                    file.write(f"nombre: {trabajador[1]}\n")
                    file.write(f"apellido: {trabajador[2]}\n")
                    file.write(f"cargo: {trabajador[3]}\n")
                    file.write(f"sueldo bruto: {trabajador[4]}\n")
                    file.write(f"descuento afp: {trabajador[5]}\n")
                    file.write(f"descuento salud: {trabajador[6]}\n")
                    file.write(f"liquido a pagar: {trabajador[7]}\n")
        print(f"\nSe ha generado el archivo '{planilla_filename}' con éxito.")
    else:
        print("Cargo no válido. Intente de nuevo.")

        time.sleep(2)          

    while menu==True:
        print("***MENU***")
        print("1. registrar trabajador")
        print("2.listar los datos de los trabajadores")
        print("3.imprimit planilla de sueldos ")
        print("4.salir del programa")
        try:
            respuestamenu=input("¿que opcion elige? ")
        except ValueError:
            print("la opcion ingresada no es correcta intentelo denuevo")

            if respuestamenu==1:
                registrartrabajador()
            elif respuestamenu==2:
                listar_datos()
            elif respuestamenu==3:
                imprimir_planilla_desueldos()
            elif respuestamenu==4:
                print("estas saliendo del programa...")
            else:
                print("opcion no valida. intente de nuevo.")
    menu=True