from os import system
system("cls")
import numpy as np
import datetime
contador = 1
asientos = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30", "31","32","33","34","35","36","37","38","39","40", "41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60", "61","62","63","64","65","66","67","68","69","70", "71","72","73","74","75","76","77","78","79","80", "81","82","83","84","85","86","87","88","89","90", "91","92","93","94","95","96","97","98","99","100"]
contTotal = 0
asientoPlatinum = 0
asientoGold = 0
asientoSilver = 0
cantidadPlatinum = 0
cantidadGold = 0
cantidadSilver = 0
reserva = [None]*100
cantTotal = 0

def verAsistente():
    for i in range(100):
        if asientos[i] == "X":
            print(f"{i+1}-{reserva[i]}")





def validar(dato):
    if len(dato) > 1:
        return True
    else:
        print("Campo obligatorio...")
        return False

def mostrarUbicacion():
    print(asientos)

def ReservarAsiento(rut:str,asiento:int):
    if asientos[int(asiento)-1] != "X":
        asientos[int(asiento)-1] = "X"
        reserva[int(asiento)-1] = rut
       
        return True
    else:
        return False


def verUbicaciones():
    print("|", end="")
    for i in range(100):
        print(asientos[i], end="|")
    print()
    
    for i in range(100):
        if asientos[i]=="X":
            print(f"{i+1}-{reserva[i]}")

while True:
    print("""
        ########## Creativos.cl ##########
        1. Comprar entradas
        2. Mostrar ubicaciones disponibles
        3. Ver listado de asistentes
        4. Mostrar ganancias totales
        5. Salir
    """)

    opcion = input("Ingrese una opcion: ")

    if opcion == "1":
        while True:
            cantidadEntradas = int(input("Ingrese cantidad de entradas que desea: "))

            if cantidadEntradas >= 0 and cantidadEntradas <=3:
                print("Ingresado con exito....")
                input("Presione enter para continuar...")
                break
            else:
                print("Solo puede comprar entre 1 y 3 entradas...")
                input("Presione enter para continuar...")
        
        mostrarUbicacion()

        while contador <= cantidadEntradas:
            print("""
                ########## PRECIOS ENTRADAS ##########
                1. Platinum $120.000.(Asientos del 1 al 20)
                2. Gold $80.000.(Asientos del 21 al 50)
                1. Silver $50.000.(Asientos del 51 al 100)
            
            """)
            try:
                asiento = input("Ingrese ubicacion: ")
            
                if int(asiento) >=1 and int(asiento) <=20:
                    asientoPlatinum = 120000
                    contTotal = contTotal + asientoPlatinum
                    cantidadPlatinum = cantidadPlatinum + 1
                    cantTotal = cantTotal + cantidadPlatinum
                    
                elif int(asiento) >=21 and int(asiento) <=50:

                    asientoGold = 80000
                    contTotal = contTotal + asientoGold
                    cantidadGold = cantidadGold + 1
                    cantTotal = cantTotal + cantidadGold 
                elif int(asiento) >=51 and int(asiento) <=100:
                    asientoSilver = 50000
                    contTotal = contTotal + asientoSilver
                    cantidadSilver = cantidadSilver + 1
                    cantTotal = cantTotal + cantidadSilver
            
                
                rut = input("Ingrese su rut: ")

                if validar(rut):
                    print("rut ingresado correctamente")
                    input("Presione enter para continuar...")
                
                if ReservarAsiento(rut, asiento):
                    print("Asiento reservado con exito")
                    contador +=1
                    
                else:
                    print("No es posible reservar")
            except IndexError:
                print("Solo aientos del 1 al 100...")
                input("Presione enter para continuar...")


    elif opcion == "2":
        verUbicaciones()
        input("Presione enter para continuar...")

    elif opcion == "3":
        print("ASISTENTES")
        verAsistente()
        input("Presione enter para continuar...")

    elif opcion == "4":
        print(f"""
        |Tipo Entrada  | cantidad  |  Total    |
        Platinum $120.000   {cantidadPlatinum}           ${asientoPlatinum}
        Gold     $80.000    {cantidadGold}               ${asientoGold}
        Silver   $50.000    {cantidadSilver}             ${asientoSilver}
        TOTAL:              {cantTotal}                  ${contTotal}
        """)
        input("Presione enter para continuar...")
    elif opcion == "5":
        print("Saliendo del sistema...")
        fechaActual = datetime.datetime.now()
        print(fechaActual)
        break
            
        




    