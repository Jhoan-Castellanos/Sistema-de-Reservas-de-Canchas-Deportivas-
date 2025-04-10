from abc import ABC, abstractmethod #--- Importa herramientas de python para usar clases abstractas


class Cancha(ABC): #--- Creamos la clase base (Madre) que sera abstracta
    
    def __init__(self, nombre: str, tipo: str, precio_por_hora: float): #-- Constructor de la clase
        self.nombre = nombre 
        self.tipo = tipo #-------Datos que almacenara cada cancha.
        self.__precio_por_hora = precio_por_hora  #-- Lo dejamos privado para proteger ese dato.

    @abstractmethod #--- Sirve para garantizar que una función exista en todas las clases hijas
    def calcular_precio(self, horas: int = 1) -> float: #---función que va a calcular el precio total de la reserva.
        pass #-- usamos pass como marcador para evitar errores cuando una función aún no tiene código

    def get_precio(self): #--Usamos get_precio() para acceder al precio de la cancha de manera segura.
        return self.__precio_por_hora #----Devuelve el valor del atributo privado __precio_por_hora

    def __str__(self): #--- función especial que define cómo se ve un objeto cuando lo imprimes.
        return f"{self.nombre} ({self.tipo}) - S/.{self.__precio_por_hora:.4f} por hora"


class CanchaSintetica(Cancha): #---Subclase de Cancha que representa una cancha sintética.
    
    """
    Constructor, función que se ejecuta cuando se crea una cancha nueva

    super(), reutiliza el constructor de la clase padre (Cancha) y le pasa los datos:
    Nombre, Tipo y Precio x hora
    """
    def __init__(self): 
        super().__init__("Cancha Sintética", "Fútbol", 80.000)

    def calcular_precio(self, horas: int = 1) -> float: #-Este método calcula el precio total según cuántas horas va a durar la reserva
        return self.get_precio() * horas #--Toma el precio por hora con el get y lo multiplica por la cantidad de horas


class CanchaVoleyPlaya(Cancha): #---Subclase de Cancha que representa una cancha de vóley playa.
   
    def __init__(self):
        super().__init__("Cancha Vóley Playa", "Vóley", 60.000)

    """
    Aquí se crea una cancha con:
    Nombre: "Cancha Vóley Playa"
    Tipo: "Vóley"
    Precio por hora: 60.000
    """

    def calcular_precio(self, horas: int = 1) -> float: #- Igual que la otra cancha, solo cambia el precio.
        return self.get_precio() * horas
