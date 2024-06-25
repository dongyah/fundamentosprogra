# Ejercicio de Gaxplosive

import time, os
os.system("cls")


# Declarar variables

cilindro_5kg = 10000
cilindro_15kg = 17000
cilindro_45kg = 60000

pedidos = []

# Definir funciones

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def registra_pedido():
    print('Eligió opción 1')
    nombre = input("Ingrese nombre del cliente:\n")
    direccion = input("Ingrese dirección del cliente:\n")
    sector = input("Ingrese sector:\n")
    cil_5kg = int(input('Ingrese la cantidad de cilindros de 5kg: '))
    cil_15kg = int(input('Ingrese la cantidad de cilindros de 15kg: '))
    cil_45kg = int(input('Ingrese la cantidad de cilindros de 45kg: '))
    
    pedido = {
        'cliente': nombre,
        'direccion': direccion, 
        'sector': sector,
        'cil_5kg': cil_5kg,
        'cil_15kg': cil_15kg,
        'cil_45kg': cil_45kg
    }
    
    '''agrega al diccionario 'pedido' a la lista 'pedidos.' Esto significa que cada vez que se registra un nuevo pedido, se anade al 
    final de la lista, permitiendo que se almacenen multiples pedidos en la misma lista'''
    pedidos.append(pedido)
    print('Pedido registrado con exito!')
            
def listar_pedido():
    print("Eligió opción 2") 
    if not pedidos:
        print('No hay pedidos registrados.')
        return
    
    for pedido in pedidos:
        print(f"Cliente: {pedido['cliente']}, Dirección: {pedido['direccion']}, Sector: {pedido['sector']}, "
              f"5kg: {pedido['cil_5kg']}, 15kg: {pedido['cil_15kg']}, 45kg: {pedido['cil_45kg']}")
    
    
def imprime_hoja_de_ruta():
    print('Eligió opción 3')
    sector = input('Ingrese el sector para imprimir la hoja de ruta:\n')
    
    pedidos_sector = [pedido for pedido in pedidos if pedido["sector"] == sector]  
    
    if not pedidos_sector:
        print(f"No hay pedidos para el sector {sector}.")
        return
    
    with open(f"hoja_de_ruta_{sector}.txt", "w") as file:
        for pedido in pedidos_sector:
            file.write(f"Cliente: {pedido['cliente']}, Dirección: {pedido['direccion']}, Sector: {pedido['sector']}, "
                       f"5kg: {pedido['cil_5kg']}, 15kg: {pedido['cil_15kg']}, 45kg: {pedido['cil_45kg']}\n")
    
    print(f"Hoja de ruta para el sector {sector} impresa con éxito!")




# programa principal
def main():
    while True:
        limpiar_pantalla
        
        #mostrar opciones de menu
        print("1. Registrar pedido") 
        print("2. Listar todos los pedidos")
        print("3. Imprimir hoja de ruta") 
        print('4. Salir del programa')
        
        # Ingrese una opción
        try:
            op = int(input('Ingrese opción:\n'))  
        except ValueError:
            op = 0
            
        # validar opción
        if op < 1 or op > 4 :
            print('Opción inválida') 
        # ejecutar acción   
        elif op == 1 :
            registra_pedido()
        elif op == 2 :
            listar_pedido()
        elif op == 3 :
            imprime_hoja_de_ruta()
        elif op == 4 :
            print('Saliendo del programa...')    
            break
        
        # Esperar antes de limpiar la pantalla
        time.sleep(2)

    print("bye bye") 
    
if __name__ == '__main__':
    main()      
 
            