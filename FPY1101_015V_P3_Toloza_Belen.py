import time, os
import os
os.system('cls')

# lista para nif lista = []

certificado_nacimiento = 1500
certificado_estado_civil = 2000
certificado_union_europea = 2500

subtotal = 0
total = 0

lista = []
dic_persona=()

def grabar():
    os.system('cls')
    print('Grabar persona')
    
    # WHILE PARA NIF
    while True:
        nif = input('Ingrese NIF (ej: 12345678-RTX):\n> ').upper()
        if nif == '' or nif == ' ':
            print('Error: campo vacío')
        else: 
            if '-' not in nif :
                print('Error: debe contener "-".')
                continue
            break    
    #end while  
    
    #WHILE PARA NOMBRE
    while True:
        nombre = input('Ingrese nombre completo:\n> ').upper()
        while len(nombre) < 8 :
            print('Error: no se pueden ingresar menos de 8 caracteres')
            nombre= input('Ingrese nombre completo:\n> ').upper()
            return nombre
            continue
        break
        #end while
    # end while   
    
    # WHILE PARA EDAD
    while True:
        try: 
            edad = int(input('Ingrese su edad:\n> '))
            if edad < 0 or edad > 120:
                print('Error: valor inválido')
                continue
            break
        except ValueError:
            edad = 0
            print('Error: valor inválido')
    #END WHILE
    
    #WHILE PARA FECHA DE NACIMIENTO
    while True:
        fecha_nacimiento = input('Ingrese su fecha de nacimiento (ej 21/08/2003):\n> ')
        while len(fecha_nacimiento) < 10 :
            print('Error: fecha de nacimiento inválida')
            fecha_nacimiento = input('Ingrese su fecha de nacimiento (ej 21/08/2003):\n> ')
            return fecha_nacimiento
        #end while
        if '/' not in fecha_nacimiento:
            print('Error: la fecha de nacimiento debe contener "/".')
            continue
        break
    #end while
    
    #While para Estado conyugal
    while True:
        estado_conyugal = input('Ingrese estado conyugal (ej: Soltera, Casado):\n> ').upper()
        while estado_conyugal not in ['SOLTERA', 'SOLTERO', 'CASADO', 'CASADA', 'DIVORCIADO', 'DIVORCIADA', 'SEPARADO', 'SEPARADA', 'VIUDO', 'VIUDA']:
            print('Error: ingrese un estado conyugal válido')
            break
        #end while
        if estado_conyugal == '' or estado_conyugal == ' ':
            print('Error: campo vacío')
            continue
        break
    #end while
    
    persona = {'NIF': nif,
               'Nombre': nombre,
               'Edad': edad,
               'Fecha de nacimiento': fecha_nacimiento,
               'Estado conyugal': estado_conyugal
               }
    lista.append(persona)
    print('Persona ingresada con éxito!')
    linea()
    return
#end def

def buscar():
    
    while True:
        print('Buscar persona')
        persona_buscada = input('Ingrese NIF de la persona que busca (ej: 12345678-RTX):\n>').upper()
        for cosa in lista:
            if cosa['NIF'] == persona_buscada :
                print(cosa)
                return
            print('ERROR: persona no encontrada')
            
            if persona_buscada in dic_persona :
                print(dic_persona[persona_buscada])
                
            
                  
                continue
            break
    #end while
    
     
    
#end def


def imprimir():
    os.system('cls')
    while True:
        print('Imprimir certificado')
        print(''' 
            1. Nacimiento (1500)
            2. Estado Conyugal (2000)
            3. Pertenencia a la Unión Europea (2500)
            4. Salir al menú principal''')
        try:
            opcion_imprimir = int(input('Ingrese una opción:\n> '))
        except ValueError:
            opcion_imprimir = 0
            print('Error: opción inválida.')
        
        if opcion_imprimir < 1 or opcion_imprimir > 4 :
            print('Error: opción inválida. Ingrese una opción del 1 al 4')
        else:
            if opcion_imprimir == 1:
                os.system('cls')
                imprimir_persona_buscada = input('Ingrese NIF de la persona que busca (ej: 12345678-RTX):\n>').upper()
                for imprimir in lista:
                    if imprimir['NIF'] == imprimir_persona_buscada :
                            print(imprimir)         
                    else:
                        print('ERROR: persona no encontrada')
                
                    if imprimir_persona_buscada in dic_persona :
                        
                        print('Certificado de Nacimiento')
                        
                        print(f"Nombre: {lista[1]}")
                        print(f"NIF: {lista[0]}")
                        print(f"Edad: {lista[2]}")
                        print(f"Fecha de nacimiento: {lista[3]}")
                        
                        continue
                        
                    total = certificado_nacimiento
                    print(f'Total a pagar', total)
                
            elif opcion_imprimir == 2:
                
                imprimir_persona_buscada = input('Ingrese NIF de la persona que busca (ej: 12345678-RTX):\n>').upper()
                for imprimir in lista:
                    if imprimir['NIF'] == imprimir_persona_buscada :
                            print(imprimir)
                    else:        
                        print('ERROR: persona no encontrada')
                for imprimir in lista:
                    if imprimir_persona_buscada in dic_persona :
                        print('Certificado estado conyugal')
                        print(f"Nombre: {lista[1]}")
                        print(f"NIF: {lista[0]}")
                        print(f"Edad: {lista[2]}")
                        print(f"Fecha de nacimiento: {lista[3]}")
                        print(f"Estado conyugal: {lista[4]}")
                    
                        continue
                    
                       
                total = certificado_estado_civil
                print(f'Total a pagar', total)
           
           
           
            elif opcion_imprimir == 3:
                os.system('cls')
                imprimir_persona_buscada = input('Ingrese NIF de la persona que busca (ej: 12345678-RTX):\n>').upper()
                for imprimir in lista:
                    if imprimir['NIF'] == imprimir_persona_buscada :
                            print(imprimir)
                    else:        
                        print('ERROR: persona no encontrada')
                    
                    if "SP" not in imprimir_persona_buscada:
                                print('Pertenencia a la Unión Europea: Sí')
                    else:
                            print('Pertenencia a la Unión Europea: No')
                            continue
                
                    if imprimir_persona_buscada in dic_persona :
                       
                        print(f"Nombre: {lista[1]}")
                        print(f"NIF: {lista[0]}")
                        print(f"Edad: {lista[2]}")
                        print(f"Fecha de nacimiento: {lista[3]}")
                        print(f"Estado conyugal: {lista[4]}")
                        
                        total = certificado_union_europea
                        print(f'Total a pagar', total)      
    
            else:
                
                break

    # end while


def salir():
    
    print('Saliendo del programa :) ...')
    print('Prueba 3 Belén Toloza Concha')
    
#end def

def linea():
    print('--------------------------')
#end def
    
    
while True:
        
        print('Inscripción de personas')
        print(''' 
            1. Grabar persona
            2. Buscar persona
            3. Imprimir certificado
            4. Salir''')
        try:
            op = int(input('Ingrese una opción:\n> '))
        except ValueError:
            op = 0
            print('Error: opción inválida.')
        
        if op < 1 or op > 4 :
            print('Error: opción inválida. Ingrese una opción del 1 al 4')
        else:
            if op == 1:
                grabar()
            elif op == 2:
                buscar()
            elif op == 3:
                imprimir()
            else:
                salir()
                break

# end while