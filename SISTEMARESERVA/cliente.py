class Cliente: #----Definimos la clase (Cliente) que representa una persona que va reservar una cancha.
    
    def __init__(self, nombre: str, cedula: str, telefono: str, email: str):
        """
        Constructor de la clase Cliente.
        """
        self.nombre = nombre
        self.cedula = cedula #-------------Valores que el Usuario Ingresa.
        self.telefono = telefono
        self.email = email

    def __str__(self): #---Metodo especial que sirve para mostrar la informacion del cliente de forma clara.
        
        return f"{self.nombre} | CEDULA: {self.cedula} | Tel: {self.telefono} | Email: {self.email}"
        
        #Usamos una f-string para mostrar los datos del cliente de manera ordenada.
        
