class Reserva:
    """
    Clase que representa una reserva de cancha.
    """

    def __init__(self, cliente, cancha, fecha: str, hora: int):
        """
        Constructor de la reserva, recibe cliente, cancha, fecha y hora al crear el objeto
        """
        self.cliente = cliente
        self.cancha = cancha
        self.fecha = fecha
        self.hora = hora

    def __str__(self): #---Metodo para imprimir "Bonito"
        return (f"[{self.fecha} - {self.hora}:00] {self.cancha.nombre} | "
                f"Cliente: {self.cliente.nombre} ({self.cliente.cedula})")
    """
    Muestra en pantalla los datos de la reserva de forma ordenada.
    """

    def coincide(self, cedula: str, fecha: str, hora: int):
        return self.cliente.cedula == cedula and self.fecha == fecha and self.hora == hora
    """
    Metodo Coincide, este método verifica si una reserva coincide con ciertos datos.
    """
