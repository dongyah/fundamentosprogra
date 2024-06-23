# En un delivery de sushi se vende 4 tipos ded sushi:

# Menú
precio_roll_1 = 4500
precio_roll_2 = 5000
precio_roll_3 = 5200
precio_roll_4 = 4800

# Nombre de los Rolls:

nombre_roll_1 = "Pikachu Roll"
nombre_roll_2 = "Otaku Roll"
nombre_roll_3 = "Pulpo Roll"
nombre_roll_4 = "Anguila eléctrica Roll"

# Descuento de un 10% si se ingresa el codigo soyotaku
codigo_actual = "soyotaku"
descuento10 = 0.1

linea = "------------------------------------"

#Contador

cantidad_de_pedidos = 0
monto_total_vendido = 0
total_roll1 = 0
total_roll2 = 0
total_roll3 = 0
total_roll4 = 0
nombre_roll_popular = '' # nos piden que mostremos en el informe cual es el roll mas popular 
total_roll_popular = 0

while True:
    
    #cada nuevo pedido
    cantidad = 0
    subtotal = 0
    total = 0
    descuento = 0
    cant_roll1 = 0
    cant_roll2 = 0
    cant_roll3 = 0
    cant_roll4 = 0
    
    while True:
        print('Bienvenido a Otaku Sushirolls')
        print('Menu')
        print('1.', nombre_roll_1, '$', precio_roll_1)
        print('2.', nombre_roll_2, '$', precio_roll_2)
        print('3.', nombre_roll_3, '$', precio_roll_3)
        print('4.', nombre_roll_4, '$', precio_roll_4)
        print('5. Salir')
        
        try:
            opcion = int(input('Seleccione el sushi que desea agregar al pedido: \n'))
        except:
            ValueError 
            print('Error: Opcion no valida')
        # end try    
    
        if opcion==1:
            print(nombre_roll_1, 'ha sido agregado a su pedido')
            cant_roll1 = cant_roll1 + 1
            cantidad = cantidad + 1
            subtotal = subtotal + precio_roll_1
            print('Subtotal:', subtotal)
            
        elif opcion== 2:     
            print(nombre_roll_2, 'ha sido agregado a su pedido')
            cant_roll2 = cant_roll2 + 1
            cantidad = cantidad + 1
            subtotal = subtotal + precio_roll_2
            print('Subtotal:', subtotal)      
            
        elif opcion== 3:     
            print(nombre_roll_3, 'ha sido agregado a su pedido')
            cant_roll3 = cant_roll3 + 1
            cantidad = cantidad + 1
            subtotal = subtotal + precio_roll_3
            print('Subtotal:', subtotal)      

        elif opcion== 4:     
            print(nombre_roll_4, 'ha sido agregado a su pedido')
            cant_roll4 = cant_roll4 + 1
            cantidad = cantidad + 1
            subtotal = subtotal + precio_roll_4
            print('Subtotal:', subtotal)      
            
        elif opcion==5:
            codigo_descuento = input('Ingrese codigo de descuento: \n')
            if codigo_descuento == codigo_actual :
                descuento = descuento10
            else:
                descuento = 0
            #end if 
          
          
          
          # aplicando el descuento del 10% al subtotal  
            monto_descontado = int(round(subtotal * descuento10))
            total = subtotal - monto_descontado     
          # fin descuento
          
            print(linea)
            print('Productos Totales:', cantidad)
            print(linea)
            print(nombre_roll_1,':',cant_roll1)
            print(nombre_roll_2,':',cant_roll2)
            print(nombre_roll_3,':',cant_roll3)
            print(nombre_roll_4,':',cant_roll4)
            print(linea)
            
            print('Subtotal:', subtotal)
            print('Descuento por codigo:', monto_descontado)
            print('Total: $', total)
            print(linea)
            print("Gracias por visitarnos")
            print(linea)
            
            cantidad_de_pedidos = cantidad_de_pedidos + 1
            monto_total_vendido = monto_total_vendido + total
            total_roll1 = total_roll1 + cant_roll1
            total_roll2 = total_roll2 + cant_roll2
            total_roll3 = total_roll3 + cant_roll3
            total_roll4 = total_roll4 + cant_roll4
            
            break
        else:
            print("Error: Opción inválida, por favor seleccione del 1 al 5")
        # end if
        print()
        
    # end while, fin del pedido
    
    try:
        continuar = int(input('¿Desea realizar otro pedido?\n1.- Si (opcion por defecto)\n2.- No (salir del programa)\n>'))        
    except:
        continuar=1
    #end try
    
    if continuar != 1:
        break
    #end if
    
#end while

total_roll_popular = total_roll1
nombre_producto_mas_popular = nombre_roll_1

if total_roll2 > total_roll_popular :
    total_roll_popular = total_roll2
    nombre_producto_mas_popular = nombre_roll_2
#end if

if total_roll3 > total_roll_popular :
    total_roll_popular = total_roll3
    nombre_producto_mas_popular = nombre_roll_3
#end if     

if total_roll4 > total_roll_popular :
    total_roll_popular = total_roll4
    nombre_producto_mas_popular = nombre_roll_4
#end if   

print('Resumen')   
print('Pedidos realizados:', cantidad_de_pedidos)
print('Total vendido     : $', monto_total_vendido)  
print('Rollo más popular :',nombre_producto_mas_popular, total_roll_popular) 

print('Sayonara!')
