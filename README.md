# 🏟️ Sistema de Reservas de Canchas Deportivas

Este proyecto es una aplicación de consola desarrollada en **Python**, que permite gestionar la reserva de canchas deportivas como fútbol y vóley playa. A través de un menú interactivo, los usuarios pueden hacer, cancelar y visualizar reservas, además de consultar la disponibilidad de las canchas por hora y fecha.

---

## 📁 Estructura del Proyecto

📦 sistema-reservas
├── main.py                 # Punto de entrada del sistema
├── cancha.py               # Clases abstractas y concretas para tipos de canchas
├── cliente.py              # Clase Cliente
├── reserva.py              # Clase Reserva que vincula cancha, cliente y horario
├── sistema_reservas.py     # Lógica principal del sistema de reservas

⚙️ Cómo ejecutar el proyecto
Asegúrate de tener Python 3.8 o superior instalado en tu sistema.
Ejecutar:
python main.py

📌 Funcionalidades
Gestión de clientes
Reservas por fecha y hora
Validación de horarios (10:00 a 21:00)
Consulta de disponibilidad
Cancelación y listado de reservas

🧠 Archivos clave
main.py: archivo principal que ejecuta el programa y contiene el menú
cancha.py: define clases abstractas y concretas de canchas (Cancha, CanchaSintetica, CanchaVoleyPlaya)
cliente.py: define la clase Cliente
reserva.py: define la clase Reserva
sistema_reservas.py: lógica del sistema de reservas (SistemaReservas)

✅ Requisitos
Python 3.8+
No requiere paquetes externos

👨‍💻 Autores
Desarrollado por: Diego Gordillo, Jhoan Castellanos y Jose Aguirre
Estudiantes de: Ingenieria en ciencia de Datos e Inteligencia Artificial
Proyecto académico UAO — Sistema de Reservas de Canchas Deportivas

