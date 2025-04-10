from cliente import Cliente
from sistema_reservas import SistemaReservas
"""
☝️ importamos las clases necesarias para ejecutar el sistema, incluyendo el cliente y el administrador de reservas.
"""

def menu():
    print("\n" + "="*50)
    print("🏟️  SISTEMA DE RESERVAS DE CANCHAS DEPORTIVAS 🏐⚽")
    print("="*50)
    print("📌  Menú Principal:")
    print("1️⃣  Hacer una reserva")
    print("2️⃣  Cancelar una reserva")
    print("3️⃣  Mostrar todas las reservas")
    print("4️⃣  Ver disponibilidad de canchas")
    print("0️⃣  Salir del sistema")
    print("="*50)
    """
    ☝️ Imprime todas las opciones disponibles que el usuario puede realizar en el sistema.
    """

sistema = SistemaReservas()
"""
☝️ crea el objeto principal del sistema que contiene, ambas canchas y las reservas que se vayan haciendo
"""

while True: 
    menu()
    opcion = input("👉🏼 Elige una opción: ").strip()
    """
    ☝️ Usamos este bucle while para que el sistema no se cierre hasta que el usuario lo decida.
    """

    if opcion == '1':
        print("\n📝 *Formulario de Reserva*")
        nombre = input("🧑‍💼 Nombre del cliente: ").strip()
        cedula = input("🆔 Cédula: ").strip()
        telefono = input("📞 Teléfono: ").strip()#----------El sistema le pide al usuario los datos personales.
        email = input("📧 Correo electrónico: ").strip()
        cliente = Cliente(nombre, cedula, telefono, email)
        """
        ☝️ Esta parte del código se activa cuando el usuario elige la opción 1 para hacer una reserva.
        Se le pide su nombre, cédula, teléfono y correo. Luego, se crea un objeto cliente con esa información,
        para que podamos guardar esa persona junto con la reserva que hará.
        """

        print("\n🏟️ Selecciona la cancha:")
        print("0️⃣  Cancha Sintética (Fútbol) ⚽") #---El usuario elige si quiere fútbol (0) o vóley (1)
        print("1️⃣  Cancha de Vóley Playa 🏐")
        try:
            cancha_index = int(input("➡️  Ingresa el número de la cancha (0 o 1): ").strip())
            if cancha_index not in [0, 1]:
                raise ValueError
        except ValueError:
            print("🚫 Opción inválida. Solo 0 o 1.")
            continue 
        """
        ☝️ Este bloque usa try y except para validar que el usuario escriba una opción correcta al elegir la cancha.
        Si escribe algo incorrecto, como letras o un número inválido, el sistema no se rompe.
        Muestra un mensaje de error y vuelve al menú para que lo intente otra vez.
        """

        # 💲 Mostrar el valor de la cancha seleccionada antes de continuar
        cancha = sistema.canchas[cancha_index]
        print(f"\n📣 Seleccionaste: {cancha.nombre}")
        print(f"💵 Costo por hora: ${cancha.get_precio():.3f}") #--.get_precio() accede al precio de esa cancha


        # ✅ Confirmación del usuario antes de continuar
        confirmacion = input("❓¿Deseas continuar con la reserva? (s/n): ").strip().lower()
        if confirmacion != 's': 
            print("❌ Reserva cancelada por el usuario.")
            continue

        fecha = input("📅 Fecha de reserva (YYYY-MM-DD): ").strip()
        """
        ☝️ Esta parte del código le pregunta al usuario si desea confirmar la reserva antes de continuar.
        Si responde 's', el sistema le pide la fecha y sigue el proceso. Si responde cualquier otra cosa,
        el sistema muestra un mensaje indicando que la reserva fue cancelada por el usuario y lo devuelve al menú.
        """

        # 🔁 Repetir hasta obtener una hora válida entre 10 y 21
        while True:
            hora_input = input("⏰ Horario Disponible (De 10:00 am - 21:00 pm): ").strip()
            try:
                hora = int(hora_input.split(':')[0])
                if 10 <= hora <= 21:
                    break
                else:
                    print("🚫 Hora fuera del rango permitido (10 a 21). Por favor, intenta nuevamente.")
            except ValueError:
                print("🚫 Formato inválido. Asegúrate de ingresar la hora como número (ej. 10 o 10:00)")

        sistema.hacer_reserva(cliente, cancha_index, fecha, hora)
        """
        ☝️ Este bloque pide al usuario la hora de su reserva y se asegura de que esté entre las 10 y las 21.
        Si la hora está fuera de ese rango o si escribe texto, el sistema muestra un mensaje de error y
        le vuelve a pedir la hora.
        """

    elif opcion == '2':
        print("\n🗑️ *Cancelar Reserva*")
        cedula = input("🆔 Cédula del cliente: ").strip()
        fecha = input("📅 Fecha (YYYY-MM-DD): ").strip()

        print("🔎 Buscando reservas del cliente...")

        reserva_encontrada = None
        for r in sistema.reservas:
            if r.cliente.cedula == cedula and r.fecha == fecha:
                reserva_encontrada = r
                break

        if reserva_encontrada:
            print(f"📌 Se encontró una reserva:")
            print(f"🏟️ {reserva_encontrada.cancha.nombre}")
            print(f"🕐 Hora reservada: {reserva_encontrada.hora}:00h")

            confirmacion = input("❓¿Deseas cancelar esta reserva? (s/n): ").strip().lower()
            if confirmacion == 's':
                sistema.cancelar_reserva(cedula, fecha, reserva_encontrada.hora)
            else:
                print("✅ No se canceló la reserva.")
        else:
            print("⚠️ No se encontró ninguna reserva para esa cédula en esa fecha.")
        """
        ☝️ Cuando el usuario elige cancelar una reserva, se le pide su cédula y la fecha de la reserva.
        El sistema busca si existe una reserva con esos datos. Si la encuentra, le muestra la cancha y la hora, y
        le pregunta si quiere cancelarla. Si confirma, la elimina. Si no hay coincidencias, el sistema le informa que
        no hay reservas registradas con esa información
        """

    elif opcion == '3':
        print("\n📄 *Listado de Reservas*")
        sistema.mostrar_reservas()
        """
        ☝️ Este bloque se ejecuta cuando el usuario escribe 3 en el menú principal.
        Su propósito es mostrar en pantalla todas las reservas realizadas hasta ese momento
        """
    
    elif opcion == '4':
        print("\n🔍 *Consulta de Disponibilidad*")
        fecha = input("📅 Fecha (YYYY-MM-DD): ").strip()
        sistema.mostrar_disponibilidad(fecha)
        """
        ☝️ Esta parte del programa permite consultar la disponibilidad de horarios por cancha para una fecha específica.
        El usuario escribe la fecha, y el sistema le muestra todas las horas del día —desde las 10 a.m. hasta las 9 p.m.
        indicando si están ocupadas o libres. Esto se logra revisando las reservas existentes y comparándolas con cada hora
        posible
        """

    elif opcion == '0':
        print("\n👋🏼 Gracias por usar nuestro sistema de reservas. ¡Hasta pronto!")
        break

    else:
        print("⚠️ Opción no válida. Intenta nuevamente.")

