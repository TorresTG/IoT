import os
from Inscrito import VERDE, AMARILLO, ROJO, RESET


class InputMaestro:
    def __init__(self, ciclo=True, name=None, campos=None, entidad_clase=None, json_path=None):
        self.__ciclo = ciclo
        self.nombre_entidad = name
        self.campos = campos if campos is not None else []
        self.json_path = json_path
        self.super_entidad = entidad_clase() if entidad_clase else None

        if not all([self.nombre_entidad, self.campos, entidad_clase, self.json_path]):
            raise ValueError("Faltan parámetros requeridos en el constructor")

        self.inicializacion()

    def inicializacion(self):
        if os.path.exists(self.json_path):
            print(f"\nCargando {self.nombre_entidad.lower()}s existentes...")
            if self.nombre_entidad == "Estudiante":
                self.super_entidad.obtencion(self.json_path, None, type(self.super_entidad), None)
            else:
                self.super_entidad.obtencion(self.json_path, type(self.super_entidad), None, None)
            print(self.super_entidad)
        else:
            print(f"\nInicializando nuevo registro de {self.nombre_entidad.lower()}s...")
            self.super_entidad.crear_json(self.json_path, [])

    @property
    def ciclo(self):
        return self.__ciclo

    def set_ciclo(self, value):
        self.__ciclo = value

    def recibir_inputs(self):
        datos = {}
        print(f"\n{'#' * 30}\nIngrese datos del {self.nombre_entidad.lower()}:")
        for campo in self.campos:
            datos[campo] = input(f"{campo.capitalize()}: ")
            print("-" * 30)
        return datos

    def verificacion(self):
        try:
            index = int(input(
                f"\nÍndice del {self.nombre_entidad.lower()} a modificar (0-{len(self.super_entidad.lista_clases) - 1}): "))
            if 0 <= index < len(self.super_entidad.lista_clases):
                print(f"\nDatos a modificar:\n{self.super_entidad.lista_clases[index]}")
                if input("¿Confirmar acción? (y/n): ").lower() == 'y':
                    return index
                return False
            print("Error: Índice fuera de rango")
        except ValueError:
            print("Error: Debe ingresar un número válido")
        return False

    def agregar_entidad(self):
        datos = self.recibir_inputs()
        nueva_entidad = type(self.super_entidad)(**datos)
        self.super_entidad.agregar_a_Lista(nueva_entidad)
        self.super_entidad.depositar_datos(self.json_path)
        print(f"\n {self.nombre_entidad} agregado exitosamente")

    def editar_entidad(self):
        if index := self.verificacion():
            nuevos_datos = self.recibir_inputs()
            entidad_actualizada = type(self.super_entidad)(**nuevos_datos)
            self.super_entidad.editar_a_Lista(index, entidad_actualizada)
            self.super_entidad.depositar_datos(self.json_path)
            print(f"\n️ {self.nombre_entidad} actualizado correctamente")

    def eliminar_entidad(self):
        if index := self.verificacion():
            self.super_entidad.eliminar_a_Lista(index)
            self.super_entidad.depositar_datos(self.json_path)
            print(f"\n {self.nombre_entidad} eliminado permanentemente")

    def mostrar_entidades(self):
        print(f"\n Listado completo de {self.nombre_entidad.lower()}s:")
        print(self.super_entidad)

    def mostrar_menu(self):
        print(f"\n{'#' * 30}")
        print(f"Gestión de {self.nombre_entidad}s".center(30))
        print(f"{VERDE}1. Agregar {self.nombre_entidad}{RESET}")
        print(f"{AMARILLO}2. Editar {self.nombre_entidad}{RESET}")
        print(f"{ROJO}3. Eliminar {self.nombre_entidad}{RESET}")
        print(f"{RESET}4. Ver todos")
        print(f"5. Salir")
        return input("\nOpción: ").strip()

    def empezar_la_matanga(self):
        while self.ciclo:
            opcion = self.mostrar_menu()
            if opcion == '1':
                self.agregar_entidad()
            elif opcion == '2':
                self.editar_entidad()
            elif opcion == '3':
                self.eliminar_entidad()
            elif opcion == '4':
                self.mostrar_entidades()
            elif opcion == '5':
                self.set_ciclo(False)
            else:
                print("\n Opción no válida")
        print(f"\nSistema de {self.nombre_entidad.lower()}s cerrado")