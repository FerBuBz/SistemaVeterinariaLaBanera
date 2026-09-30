# Taller 8: Sistema básico de Veterinaria "La Bañera"


class Cliente:
    def __init__(self, nombre, documento, telefono):
        self.nombre = nombre
        self.documento = documento
        self.telefono = telefono


class Mascota:
    def __init__(self, nombre, raza, edad, peso, dueno):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.dueno = dueno
        self.historial = []

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad} años")
        print(f"Peso: {self.peso} kg")
        print(f"Dueño: {self.dueno.nombre}")


def pedir_numero(mensaje):
    """Pide un número mayor que cero."""
    while True:
        try:
            numero = float(input(mensaje))
            if numero > 0:
                return numero
            print("El valor debe ser mayor que cero.")
        except ValueError:
            print("Debe escribir un número válido.")


def buscar_cliente(clientes, documento):
    for cliente in clientes:
        if cliente.documento == documento:
            return cliente
    return None


def buscar_mascota(mascotas, nombre):
    for mascota in mascotas:
        if mascota.nombre.lower() == nombre.lower():
            return mascota
    return None


def registrar_cliente(clientes):
    print("\n--- Registrar cliente ---")
    nombre = input("Nombre: ").strip()
    documento = input("Documento: ").strip()
    telefono = input("Teléfono: ").strip()

    if not nombre or not documento or not telefono:
        print("Todos los datos son obligatorios.")
    elif buscar_cliente(clientes, documento):
        print("Ya existe un cliente con ese documento.")
    else:
        clientes.append(Cliente(nombre, documento, telefono))
        print("Cliente registrado correctamente.")


def registrar_mascota(mascotas, clientes):
    print("\n--- Registrar mascota ---")
    documento = input("Documento del dueño: ").strip()
    dueno = buscar_cliente(clientes, documento)

    if dueno is None:
        print("Primero debe registrar al dueño.")
        return

    nombre = input("Nombre de la mascota: ").strip()
    raza = input("Raza: ").strip()
    if not nombre or not raza:
        print("El nombre y la raza son obligatorios.")
        return

    edad = pedir_numero("Edad en años: ")
    peso = pedir_numero("Peso en kg: ")
    mascotas.append(Mascota(nombre, raza, edad, peso, dueno))
    print("Mascota registrada correctamente.")


def listar_mascotas(mascotas):
    print("\n--- Mascotas registradas ---")
    if not mascotas:
        print("No hay mascotas registradas.")
        return

    for numero, mascota in enumerate(mascotas, 1):
        print(f"\nMascota {numero}")
        mascota.mostrar()


def registrar_peso(mascotas):
    print("\n--- Control de peso ---")
    mascota = buscar_mascota(mascotas, input("Nombre de la mascota: "))
    if mascota is None:
        print("Mascota no encontrada.")
        return

    mascota.peso = pedir_numero("Nuevo peso en kg: ")
    print("Peso actualizado correctamente.")


def registrar_atencion(mascotas):
    print("\n--- Atención clínica ---")
    mascota = buscar_mascota(mascotas, input("Nombre de la mascota: "))
    if mascota is None:
        print("Mascota no encontrada.")
        return

    motivo = input("Motivo de la consulta: ")
    diagnostico = input("Diagnóstico: ")
    mascota.historial.append((motivo, diagnostico))
    print("Atención registrada correctamente.")


def ver_historial(mascotas):
    print("\n--- Historial clínico ---")
    mascota = buscar_mascota(mascotas, input("Nombre de la mascota: "))
    if mascota is None:
        print("Mascota no encontrada.")
    elif not mascota.historial:
        print("La mascota no tiene atenciones registradas.")
    else:
        for numero, atencion in enumerate(mascota.historial, 1):
            print(f"{numero}. Motivo: {atencion[0]} | Diagnóstico: {atencion[1]}")


def agendar_cita(mascotas, citas):
    print("\n--- Agendar cita ---")
    mascota = buscar_mascota(mascotas, input("Nombre de la mascota: "))
    if mascota is None:
        print("Mascota no encontrada.")
        return

    fecha = input("Fecha de la cita: ")
    hora = input("Hora de la cita: ")
    citas.append((mascota, fecha, hora))
    print("Cita agendada correctamente.")


def listar_citas(citas):
    print("\n--- Citas agendadas ---")
    if not citas:
        print("No hay citas agendadas.")
        return

    for numero, cita in enumerate(citas, 1):
        mascota, fecha, hora = cita
        print(f"{numero}. {mascota.nombre} - {fecha} a las {hora}")


def main():
    clientes = []
    mascotas = []
    citas = []

    while True:
        print("\n=== VETERINARIA LA BAÑERRA ===")
        print("1. Registrar cliente")
        print("2. Registrar mascota")
        print("3. Listar mascotas")
        print("4. Registrar control de peso")
        print("5. Registrar atención clínica")
        print("6. Ver historial clínico")
        print("7. Agendar cita")
        print("8. Listar citas")
        print("0. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_cliente(clientes)
        elif opcion == "2":
            registrar_mascota(mascotas, clientes)
        elif opcion == "3":
            listar_mascotas(mascotas)
        elif opcion == "4":
            registrar_peso(mascotas)
        elif opcion == "5":
            registrar_atencion(mascotas)
        elif opcion == "6":
            ver_historial(mascotas)
        elif opcion == "7":
            agendar_cita(mascotas, citas)
        elif opcion == "8":
            listar_citas(citas)
        elif opcion == "0":
            print("Gracias por usar el sistema.")
            break
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
