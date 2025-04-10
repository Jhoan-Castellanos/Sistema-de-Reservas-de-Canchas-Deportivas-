from cancha import CanchaSintetica, CanchaVoleyPlaya
from reserva import Reserva

"""
Esto importa otras clases desde archivos externos
"""

class SistemaReservas:
    """
    Clase principal que maneja todo el sistema de reservas. Hacer, Cancelar o Mostrar
    """

    def __init__(self): #----Constructor
        self.canchas = [CanchaSintetica(), CanchaVoleyPlaya()]
        self.reservas = []
    """
    Crea una lista self.canchas con 2 objetos: una cancha sintética y una de vóley playa.
    Crea una lista vacía self.reservas para almacenar todas las reservas del sistema.
    """

    def hacer_reserva(self, cliente, cancha_index: int, fecha: str, hora: int):
        """
        Este método intenta hacer una reserva nueva.
        """
        if hora < 10 or hora > 21: #--Valida horario permitido
            print("⛔ Horario fuera del rango permitido (10 a 21).") 
            return 

        cancha = self.canchas[cancha_index] #--Esta línea obtiene la cancha que el cliente quiere reservar
        for reserva in self.reservas: #Bucle que recorre todas las reservas actuales almacenadas en self.reservas
            if reserva.fecha == fecha and reserva.hora == hora and reserva.cancha == cancha: 
                """
                Esta línea verifica si ya hay una reserva existente en la misma cancha, misma fecha y misma hora
                """
                print("⛔ Ya existe una reserva para esa cancha en ese horario.") #--Mensaje de Error
                return
            
        nueva_reserva = Reserva(cliente, cancha, fecha, hora)
        self.reservas.append(nueva_reserva)
        print("✅ Reserva realizada con éxito.")
        """
        Si todo está bien, se crea un nuevo objeto reserva y se guarda en la lista
        """

    def cancelar_reserva(self, cedula: str, fecha: str, hora: int):
        """
        Esta función busca una reserva específica para cancelarla.
        """
        for reserva in self.reservas:
            if reserva.coincide(cedula, fecha, hora):
                self.reservas.remove(reserva) #--------Si encuentra una reserva que coincide, la elimina.
                print("✅ Reserva cancelada.")
                return
        #print("⛔ Reserva no encontrada.")

    def mostrar_reservas(self):
        """
        Este método muestra todas las reservas existentes.
        """
        if not self.reservas:
            print("📭 No hay reservas registradas.") #----Si la lista está vacía, informa que no hay nada guardado
        for reserva in self.reservas: #-------------------Recorre y muestra una por una todas las reserva
            print(reserva)

    def mostrar_disponibilidad(self, fecha: str):
        """
        Este método muestra todas las horas disponibles y ocupadas para una fecha específica.
        """
        print(f"📅 Disponibilidad para {fecha}")
        for i, cancha in enumerate(self.canchas): #---Recorre las dos canchas (fútbol y vóley)
            print(f"\n{cancha.nombre}:")
            for hora in range(10, 22): #--------Recorre las horas válidas (de 10 a 21)
                ocupado = any(r.fecha == fecha and r.hora == hora and r.cancha == cancha #-any() para verificar si alguien ya reservó esa hora en esa cancha
                              for r in self.reservas)
                estado = "⛔ Reservada" if ocupado else "✅ Disponible" #--Muestra si la hora está reservada o no.
                print(f"{hora}:00 - {estado}")
