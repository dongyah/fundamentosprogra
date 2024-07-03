import time, os
os.system("cls")

# Definir funciones

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    
# Crear un sistema para gestionar las reservas de un hotel llamado Hotel Tranquilidad

reservas = []

def registrar_reserva():
   nombre = input('Nombre del huesped:\n')
   numero_habitacion = int(input('Numero de habitacion:\n'))
   
   tipo_habitacion = input('Tipo de habitacion (Individual, Doble, Suite): \n')
   while tipo_habitacion not in ['individual', 'doble', 'suite']:
       print('Error: tipo de habitacion invalido, por favor ingrese una de las opciones dadas')
   
   fecha_entrada = input('Ingrese fecha de entrada (dd/mm/aaaa):\n')
   fecha_salida = input('Ingrese fecha de salida (dd/mm/aaaa):\n')
   
   reserva = {
       'huesped': nombre,
       'numero_habitacion': numero_habitacion, 
       'tipo_habitacion': tipo_habitacion,
       'fecha_entrada': fecha_entrada,
       'fecha_salida': fecha_salida
   }
   
   reservas.append(reserva)
   print('Reserva registrada con exito!')
    
def listar_reservas():
    if not reservas:
        print('No hay reservas registradas.')
        return
    
    for reserva in reservas:
        print(f"Huesped: {reserva['huesped']}, "
              f"Numero de habitacion: {reserva['numero_habitacion']}, "
              f"Tipo de habitacion: {reserva['tipo_habitacion']}, "
              f"Fecha de entrada: {reserva['fecha_entrada']}, "
              f"Fecha de saldida: {reserva['fecha_salida']}")
    
    
def buscar_reserva(nombre_huesped):
    resultados = [reserva for reserva in reservas if reserva["huesped"] == nombre_huesped]
    if not resultados:
        print(f"No se encontraron reservas para el huésped: {nombre_huesped}")
    else:
        for reserva in resultados:
            print(f"Huesped: {reserva['huesped']}, "
              f"Numero de habitacion: {reserva['numero_habitacion']}, "
              f"Tipo de habitacion: {reserva['tipo_habitacion']}, "
              f"Fecha de entrada: {reserva['fecha_entrada']}, "
              f"Fecha de saldida: {reserva['fecha_salida']}")
    
def reporte_ocupacion():
    tipo_habitacion = input('Ingrese el tipo de habitación para generar el reporte (Individual, Doble, Suite): ')
    while tipo_habitacion not in ['Individual', 'Doble', 'Suite']:
        print('Tipo de habitacion invalido. Por favor elijauno de los tipos definidos.')
    
    reservas_tipo = [reserva for reserva in reservas if reserva['tipo_habitacion'] == tipo_habitacion]

    if not reservas_tipo:
        print(f"No hay reservas para el tipo de habitacion {tipo_habitacion}.")
        return
    
    with open(f"reporte_ocupacion_{tipo_habitacion}.txt", "w") as file:
        for reserva in reservas_tipo:
            file.write(f"Huésped: {reserva['huesped']}, Número de Habitación: {reserva['numero_habitacion']}, "
                       f"Tipo de Habitación: {reserva['tipo_habitacion']}, Fecha de Entrada: {reserva['fecha_entrada']}, "
                       f"Fecha de Salida: {reserva['fecha_salida']}\n")


    print(f'Reporte de ocupacion para el tipo de habitacion {tipo_habitacion} generado con exito.')

def salir():
    print('Saliendo del programa...')
    exit()


def main():
    while True:
        limpiar_pantalla()
        
        #mostrar opciones del menu
        print('Bienvenido a Hotel Tranquilidad')
        print('1. Registrar reserva') 
        print('2. Listar todas las reservas') 
        print('3. Buscar reserva por nombre de huesped') 
        print('4. Generar reporte de ocupacion por tipo de habitacion') 
        print('5. Salir del programa')
        
        try:
            op = int(input('Ingrese una opcion: \n'))
        except ValueError:
            op = 0
            
        if  op < 1 or op > 5:
            print('Error: opcion invalida') 
        elif op == 1: 
            registrar_reserva()
        elif op == 2:
            listar_reservas()
        elif op == 3:
            buscar_reserva()
        elif op == 4:
            reporte_ocupacion()  
        elif op == 5:
           salir()                    
            
        time.sleep(2)
     
if __name__ == "__main__":
    main()        
               
                         