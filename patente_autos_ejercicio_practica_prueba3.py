import time, os
import os
os.system('cls')

lista = []

dic_autos={} # se usa una clave y valor

def ingresar():
    os.system('cls')
    print("Ingresar nuevo auto")
    
    # PATENTE 
    
    while True:
        patente = input('Ingrese la patente del auto (XXYY11):\n> ').upper()
        if patente == '' or patente == ' ':
            print('Error: campo no puede ir vacío')
            continue
        break    
    #end while
    
    # AÑO
    while True: 
        try: 
            anio = int(input('Ingrese año del vehículo (ej: 2010):\n> '))
            if anio < 1990 or anio > 2024 :
                print('Error: valor ingresado inválido') 
                continue
            break         
        except ValueError:
            anio = 0
            print('Error: valor inválido')
    #end while
        
    # MOTOR
    while True:
        try:
            motor = float(input('Ingrese motor del vehículo (ej: 1.2):\n> '))
            if motor < 0.8 or motor > 6.5:
                print('Error: valor inválido')
                continue
            break
        except ValueError:
            motor = 0 
            print('Error: valor inválido')
            
    # end while
    
    
    auto = {'Patente' : patente,
            'Año': anio,
            'Motor': motor
                    }
            
    lista.append(auto)
    print('Auto ingresado con éxito')
    linea()
    return
    
def mostrar():
    
    print("Mostrar todos los autos registrados")
    for cosa in lista :
        print(cosa)
        linea()
      
def buscar_uno():
    print("Buscar un auto")
    patente_buscada = input('Ingrese patente del auto:\n> ').upper()
    for cosa in lista :
        if cosa['Patente'] == patente_buscada :
            print(cosa)
            return
    print('Error: patente no encontrada')  
    
    if patente_buscada in dic_autos :
        print(dic_autos[patente_buscada])  
      
def salir():
    print("Saliendo...")  
    
def linea():
    print('------------------------------------------')        
         
    
    
    
while True:
    
    print('Inscripción de vehículos')
    print(''' 
            1.- Ingresar nuevo auto
            2.- Mostrar todos los autos ingresados
            3.- Buscar un auto
            4.- Salir  
          ''')   
    
    try:
       op = int(input("Seleccione una opción: \n> "))
    except ValueError:
        op = 0
        print("Error: opción inválida.")
        
    if op < 1 or op > 4 :
            print("Error: opción inválida. Ingrese un número del 1 al 4")
    else:
        if op == 1 :
                ingresar()
                
        elif op == 2 : 
                mostrar()
                
        elif op == 3 :
                buscar_uno()
            
        else:
                salir()
                break      