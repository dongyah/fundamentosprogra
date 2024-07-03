import time
import os
os.system('cls')

lista = []
dic_persona = {}
estados_civiles_validos = ['SOLTERO', 'SOLTERA', 'CASADO', 'CASADA', 'SEPARADO', 'SEPARADA', 'DIVORCIADO', 'DIVORCIADA', 'VIUDO', 'VIUDA']

def ingresar_persona():
    while True: 
        print('Ingresar persona')
        nombre = input('Ingrese nombre completo:\n> ').upper()
        if nombre == "" or nombre == " ":
            print('Error: campo vacío')
            continue
        break
    # end while
    
    while True:
        try:
            rut = int(input('Ingrese RUT sin puntos ni guión, si su rut termina en k reemplácelo por 0:\n> '))
        except:
            rut = 0
            print('Error: RUT inválido')
            continue
        break
             
        
    #end while    
    
    while True:
        nacimiento = input("Ingrese fecha de nacimiento (ej 21/08/2003):\n> ")
        if nacimiento == '' or nacimiento == " ":
            print('Error: campo vacío')
            continue
        if '/' not in nacimiento:
            print('Error: debe contener "/"')
            continue
        break           
    # end while 
    
    while True:
        nacionalidad = input("Ingrese nacionalidad:\n> ").upper()
        if nacionalidad == '' or nacionalidad == ' ':
            print('Error: campo vacío')
            continue
        break
    #end while       
    
    while True:
        estado_civil = input('Ingrese estado civil:\n> ').upper()
        if estado_civil == '' or estado_civil == ' ':
            print('Error: campo vacío')
        else:
            if estado_civil in estados_civiles_validos:
                break
            else:
                print('Error: ingrese un estado civil válido')
    #end while    
    
    persona = {'Nombre': nombre,
               'Fecha de nacimiento': nacimiento,
               'Nacionalidad': nacionalidad,
               'Estado civil': estado_civil
               }
    lista.append(persona)
    print('Persona ingresada con éxito')
    return
    
def mostrar():
    for cosa in lista:
        print(cosa)
        
def buscar_persona():
    while True:
        try:
            persona_buscada = int(input('Ingrese RUT de la persona (sin puntos ni guión):\n> '))
        except:
            persona_buscada = 0
            print('Error: RUT inválido')
            continue
        break
            
    for cosa in lista:
        if cosa['RUT'] == persona_buscada:
            print(cosa)
            return
        print('Error: persona no encontrada')
        
        if persona_buscada in dic_persona:
            print(dic_persona[persona_buscada])
    #end while        
def editar():
    print('opcion 1')
def imprimir():   
    print('opcion 1')
def salir():   
    print('opcion 1')  



while True:
    print(''' Registro civil
          1. Ingresar pesona
          2. Mostrar todas las personas
          3. Buscar persona
          4. Editar persona
          5. Imprimir certificado
          6. Salir''')
    try: 
        op = int(input('Ingrese una opción:\n> '))
    except ValueError:
        op = 0
        print('Error: valor inválido')
    # fin try
    
    if op < 1 or op > 6 :
        print('Error: opción inválida. Ingrese un valor del 1 al 6')
    else:
        if op == 1 :
            ingresar_persona()
        elif op == 2 :    
            print('opcion 2')
        elif op == 3 :
            print('opcion 3')
        elif op == 4 :
            print('opcion 4')
        elif op == 5 :
            print('opcion 5')
        else:
            print('opcion 6')  
            break      
        