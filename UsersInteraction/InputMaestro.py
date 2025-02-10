import os

from Curso import Curso
from Inscrito import VERDE, AMARILLO, ROJO, RESET


class InputMaestro:
    def __init__(self, ciclo=True, name=None, campos=None, laClaseARecibir=None, json_path=None):
        self.__ciclo = ciclo
        self.nombreDeLaClase = name
        self.campos = campos
        self.json_path = json_path
        self.superClase = laClaseARecibir()

        self.inicializacion()

    def inicializacion(self):
        if os.path.exists(self.json_path):
            print(f"\nCargando {self.nombreDeLaClase.lower()}s existentes...")
            if self.nombreDeLaClase == "Estudiante":
                self.superClase.obtencion(self.json_path, None, type(self.superClase), None)
            else:
                self.superClase.obtencion(self.json_path, type(self.superClase), None, None)
            print(self.superClase)
        else:
            print(f"\nInicializando nuevo registro de {self.nombreDeLaClase.lower()}s...")
            self.superClase.crear_json(self.json_path, [])

    @property
    def ciclo(self):
        return self.__ciclo

    def set_ciclo(self, value):
        self.__ciclo = value

    def recibir_inputs(self):
        datos = {}
        print(f"\n{'#' * 30}\nIngrese datos del {self.nombreDeLaClase.lower()}:")
        for campo in self.campos:
            datos[campo] = input(f"{campo.capitalize()}: ")
            print("-" * 10)
        return datos

    def verificacion(self):
        print(f"\nÍndice del {self.nombreDeLaClase.lower()} a modificar (0-{len(self.superClase.lista_clases) - 1}): ")
        index = input()

        if index.isdigit():
            index = int(index)

            if 0 <= index < len(self.superClase.lista_clases):
                print(f"\nDatos a modificar:\n{self.superClase.lista_clases[index]}")
                print("¿Confirmar acción? (y/n): ")
                confirmacion = input().lower()
                if confirmacion == "y":
                    return index
                elif confirmacion == "n":
                    print("Se canceló la edición")
                    return False
                else:
                    print("Por favor, ingrese una opción válida")
                    return False
            else:
                print("Error: Índice fuera de rango")
                return False
        else:
            print("Error: Debe ingresar un número válido")
            return False




    def agregar_Clase(self):
        datos = self.recibir_inputs()
        nueva_entidad = type(self.superClase)(**datos)
        self.superClase.agregar_a_Lista(nueva_entidad)
        self.superClase.depositar_datos(self.json_path)
        print(f"\n {self.nombreDeLaClase} agregado exitosamente")

    def editar_Clase(self):
        index = self.verificacion()
        if index is not False:
            nuevos_datos = self.recibir_inputs()
            entidad_actualizada = type(self.superClase)(**nuevos_datos)
            self.superClase.editar_a_Lista(index, entidad_actualizada)
            self.superClase.depositar_datos(self.json_path)
            print(f"\n️ {self.nombreDeLaClase} actualizado correctamente")

    def eliminar_Clase(self):
        index = self.verificacion()
        if index is not False:
            self.superClase.eliminar_a_Lista(index)
            self.superClase.depositar_datos(self.json_path)
            print(f"\n {self.nombreDeLaClase} eliminado permanentemente")

    def mostrar_entidades(self):
        print(f"\n Listado completo de {self.nombreDeLaClase.lower()}s:")
        print(self.superClase)

    def mostrar_menu(self):
        print(f"\n{'#' * 30}")
        print(f"Gestión de {self.nombreDeLaClase}s".center(30))
        print(f"{VERDE}1. Agregar {self.nombreDeLaClase}{RESET}")
        print(f"{AMARILLO}2. Editar {self.nombreDeLaClase}{RESET}")
        print(f"{ROJO}3. Eliminar {self.nombreDeLaClase}{RESET}")
        print(f"{RESET}4. Ver todos")
        print(f"5. Salir")
        return input("\nOpción: ").strip()

    def empezar_la_matanga(self):
        while self.ciclo:
            opcion = self.mostrar_menu()
            if opcion == '1':
                self.agregar_Clase()
            elif opcion == '2':
                self.editar_Clase()
            elif opcion == '3':
                self.eliminar_Clase()
            elif opcion == '4':
                self.mostrar_entidades()
            elif opcion == '5':
                self.set_ciclo(False)
            else:
                print("\n Opción no válida")
        print(f"\nSistema de {self.nombreDeLaClase.lower()}s cerrado ,volviendo a Inscripciones...")
        return self.superClase

if __name__ == "__main__":

    gestor = InputMaestro(True, "Curso", ["nombre", "grado", "seccion", "salon", "descripcion"],
                        Curso, "/Users/torres/Documents/pruebas_python/CursoInput.json")
    gestor.empezar_la_matanga()