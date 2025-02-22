import time

class Semaforo:
    def __init__(self):
        self.estado = "rojo"  # Estado inicial del semáforo
        self.duracion_verde = 10  # Duración base del estado verde
        self.duracion_amarillo = 3  # Duración fija del estado amarillo
        self.duracion_rojo = 10  # Duración base del estado rojo

    def cambiar_estado(self, vehiculos_direccion_actual, vehiculos_direccion_opuesta):
        # Ajustar la duración del estado verde según el número de vehículos
        self.duracion_verde = 10 + 2 * vehiculos_direccion_actual
        # Ajustar la duración del estado rojo según el número de vehículos en la dirección opuesta
        self.duracion_rojo = 10 + 2 * vehiculos_direccion_opuesta

        # Ciclo de estados del semáforo
        while True:
            # Estado verde
            self.estado = "verde"
            print(f"Semáforo en {self.estado} por {self.duracion_verde} segundos.")
            time.sleep(self.duracion_verde)

            # Estado amarillo
            self.estado = "amarillo"
            print(f"Semáforo en {self.estado} por {self.duracion_amarillo} segundos.")
            time.sleep(self.duracion_amarillo)

            # Estado rojo
            self.estado = "rojo"
            print(f"Semáforo en {self.estado} por {self.duracion_rojo} segundos.")
            time.sleep(self.duracion_rojo)

            # Volver a ajustar las duraciones en cada ciclo
            self.duracion_verde = 10 + 2 * vehiculos_direccion_actual
            self.duracion_rojo = 10 + 2 * vehiculos_direccion_opuesta

# Función principal
def main():
    semaforo = Semaforo()

    # Simulación de detección de vehículos
    vehiculos_direccion_actual = int(input("Ingrese el número de vehículos en la dirección actual: "))
    vehiculos_direccion_opuesta = int(input("Ingrese el número de vehículos en la dirección opuesta: "))

    # Iniciar el ciclo del semáforo
    semaforo.cambiar_estado(vehiculos_direccion_actual, vehiculos_direccion_opuesta)

if __name__ == "__main__":
    main()