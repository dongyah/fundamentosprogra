

# Codigo antierrores

import os
import time

# Limpiar pantalla según el sistema operativo
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Lista para almacenar las reservas
reservas = []

# Definir funciones
def registrar_reserva():
    try:
        nombre = input("Ingrese el nombre del huésped: ").strip()
        if not nombre:
            raise ValueError("El nombre del huésped no puede estar vacío.")
        
        numero_habitacion = input("Ingrese el número de habitación: ").strip()
        if not numero_habitacion:
            raise ValueError("El número de habitación no puede estar vacío.")
        
        tipo_habitacion = input("Ingrese el tipo de habitación (Individual, Doble, Suite): ").strip()
        while tipo_habitacion not in ["Individual", "Doble", "Suite"]:
            print("Tipo de habitación inválido. Por favor, elija uno de los tipos definidos.")
            tipo_habitacion = input("Ingrese el tipo de habitación (Individual, Doble, Suite): ").strip()
        
        fecha_entrada = input("Ingrese la fecha de entrada (dd/mm/yyyy): ").strip()
        if not fecha_entrada:
            raise ValueError("La fecha de entrada no puede estar vacía.")
        
        fecha_salida = input("Ingrese la fecha de salida (dd/mm/yyyy): ").strip()
        if not fecha_salida:
            raise ValueError("La fecha de salida no puede estar vacía.")
        
        # Validar formato de fecha
        try:
            day, month, year = map(int, fecha_entrada.split('/'))
            day, month, year = map(int, fecha_salida.split('/'))
        except ValueError:
            print("Formato de fecha inválido. Use el formato dd/mm/yyyy.")
            return
        
        reserva = {
            "huesped": nombre,
            "numero_habitacion": numero_habitacion,
            "tipo_habitacion": tipo_habitacion,
            "fecha_entrada": fecha_entrada,
            "fecha_salida": fecha_salida
        }
        
        reservas.append(reserva)
        print("Reserva registrada con éxito!")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error al registrar la reserva: {e}")

def listar_reservas():
    if not reservas:
        print("No hay reservas registradas.")
        return
    
    for reserva in reservas:
        print(f"Huésped: {reserva['huesped']}, Número de Habitación: {reserva['numero_habitacion']}, "
              f"Tipo de Habitación: {reserva['tipo_habitacion']}, Fecha de Entrada: {reserva['fecha_entrada']}, "
              f"Fecha de Salida: {reserva['fecha_salida']}")

def buscar_reserva_por_huesped(nombre_huesped):
    if not nombre_huesped.strip():
        print("El nombre del huésped no puede estar vacío.")
        return

    resultados = [reserva for reserva in reservas if reserva["huesped"] == nombre_huesped]
    if not resultados:
        print(f"No se encontraron reservas para el huésped: {nombre_huesped}")
    else:
        for reserva in resultados:
            print(f"Huésped: {reserva['huesped']}, Número de Habitación: {reserva['numero_habitacion']}, "
                  f"Tipo de Habitación: {reserva['tipo_habitacion']}, Fecha de Entrada: {reserva['fecha_entrada']}, "
                  f"Fecha de Salida: {reserva['fecha_salida']}")

def generar_reporte_ocupacion():
    try:
        tipo_habitacion = input("Ingrese el tipo de habitación para generar el reporte (Individual, Doble, Suite): ").strip()
        while tipo_habitacion not in ["Individual", "Doble", "Suite"]:
            print("Tipo de habitación inválido. Por favor, elija uno de los tipos definidos.")
            tipo_habitacion = input("Ingrese el tipo de habitación para generar el reporte (Individual, Doble, Suite): ").strip()
        
        reservas_tipo = [reserva for reserva in reservas if reserva["tipo_habitacion"] == tipo_habitacion]
        
        if not reservas_tipo:
            print(f"No hay reservas para el tipo de habitación {tipo_habitacion}.")
            return
        
        with open(f"reporte_ocupacion_{tipo_habitacion}.txt", "w") as file:
            for reserva in reservas_tipo:
                file.write(f"Huésped: {reserva['huesped']}, Número de Habitación: {reserva['numero_habitacion']}, "
                           f"Tipo de Habitación: {reserva['tipo_habitacion']}, Fecha de Entrada: {reserva['fecha_entrada']}, "
                           f"Fecha de Salida: {reserva['fecha_salida']}\n")
        
        print(f"Reporte de ocupación para el tipo de habitación {tipo_habitacion} generado con éxito!")
    except Exception as e:
        print(f"Ocurrió un error al generar el reporte: {e}")

def salir():
    print("Saliendo del programa...")
    exit()

# Programa principal
def main():
    while True:
        limpiar_pantalla()
        
        # Mostrar opciones de menú
        print("1. Registrar reserva")
        print("2. Listar todas las reservas")
        print("3. Buscar reserva por nombre de huésped")
        print("4. Generar reporte de ocupación por tipo de habitación")
        print("5. Salir del programa")
        
        # Ingrese una opción
        try:
            op = int(input('Ingrese opción: '))  
        except ValueError:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 5.")
            time.sleep(2)
            continue
        
        # Validar opción
        if op < 1 or op > 5:
            print('Opción inválida')
        elif op == 1:
            registrar_reserva()
        elif op == 2:
            listar_reservas()
        elif op == 3:
            nombre_huesped = input("Ingrese el nombre del huésped: ").strip()
            buscar_reserva_por_huesped(nombre_huesped)
        elif op == 4:
            generar_reporte_ocupacion()
        elif op == 5:
            salir()
        
        # Esperar antes de limpiar la pantalla
        time.sleep(2)

if __name__ == "__main__":
    main()

