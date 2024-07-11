import time, os, csv
import random
os.system('cls')

sueldo_minimo = 300000
sueldo_maximo = 2500000
trabajadores = ["Juan Pérez”,”María García”,”Carlos López”,”Ana Martínez”,”Pedro Rodríguez”,”Laura Hernández”,”Miguel Sánchez”,”Isabel Gómez”,”Francisco Díaz”,”Elena Fernández"]
sueldos = []
empleados = []



# funciones

def asignar_sueldos_aleatorios():
    print('Asignando sueldos aleatoriamente...')
    sueldos = [random.randint(300000,2500000) for _ in range(len(trabajadores))] # un rango de 10 ya que es la cantidd de trabajadores
    return sueldos
        

def clasificar_sueldos():
    menores = []
    entre = []
    mayores = []
    
    for i, sueldo in sueldos:
        if sueldo < sueldo_minimo:
            menores.append((trabajadores[i], sueldo))
        elif sueldo <= sueldo_maximo:
            entre.append((trabajadores[i], sueldo))
        else:
            mayores.append((trabajadores[i], sueldo))
            print(sueldo)
            return sueldo
    
def ver_estadisticas():
    print('Ver estadisticas')
    
def reporte_de_sueldos():
    print('Reporte de sueldos')    
    
def salir():
    print('Saliendo del programa...')
    print('Desarrollado por Belén Toloza Concha')
    print('RUT 21.374.678-2')
 
    
# MENU
while True:
    print('Menú de opciones')
    print('''
          1. Asignar sueldos aleatorios
          2. Clasificar sueldos
          3. Ver estadísticas
          4. Reporte de sueldos
          5. Salir del programa
          ''')
    try:
        op = int(input('Ingrese una opción:\n> '))
    except ValueError:
        op = 0
        print('Error: valor inválido')
    if op < 1 or op > 5 :
            print('Error: valor inválido.')
    else:
        if op == 1:
                asignar_sueldos_aleatorios()
        elif op == 2:
                print('opcion 2')
        elif op == 3:
                print('Opcion 3')
        elif op == 4:
                print('opcion 4')
        else:
            salir()
            break
        
#GENERAR NUMEROS RANDOM, HAY QUE GENERARLOS NO PEDIRSELOS AL USUARIO

# definir variable valor = random.randint, dos parametros, valor (min, max), o sea (300000, 2500000)
