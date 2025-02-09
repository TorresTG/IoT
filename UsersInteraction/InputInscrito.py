import os
from Inscrito import VERDE, AMARILLO, ROJO, RESET

from Inscrito import Inscrito
from Curso import Curso
from Estudiante import Estudiante
from UsersInteraction.InputMaestro import InputMaestro

json_path = "/Users/torres/Documents/pruebas_python/InscritoInput.json"

class InputInscrito:

    def __init__(self, ciclo=True):
        self.__ciclo = ciclo
        self.superClase = Inscrito()
        self.inicializacion()

    def inicializacion(self):
        if os.path.exists(json_path):
            print(f"Añadiendo Inscritos...")
            self.superClase.obtencion(json_path, Curso, Estudiante, Inscrito)
            print(self.superClase)
        else:
            print(f"No se encontró ningún Inscrito. Creando archivo...")
            self.superClase.crear_json(json_path, [])

    def agregado(self):
        pass

    def editado(self):
        pass

    def eliminado(self):
        pass

    @property
    def ciclo(self):
        return self.__ciclo

    def set_ciclo(self, value):
        self.__ciclo = value

    def ver_entidades(self):
        print(self.superClase)

    def empezar_la_matanga(self):
        while self.ciclo:
            print(f"\n-------- Gestión de Inscrito --------")
            print(f"1) Acceder a Cursos")
            print(f"2) Acceder a Estudiantes")
            print(f"3) Agregar Inscritos")
            print(f"4) Editar Inscrito")
            print(f"5) Eliminar Inscrito")
            print(f"6) Ver Inscrito")
            print(f"7) Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                Cur = InputMaestro(True, "Curso", ["nombre", "grado", "seccion", "salon", "descripcion"],
                                      Curso, "/Users/torres/Documents/pruebas_python/CursoInput.json")
                Cur.empezar_la_matanga()
            elif opcion == '2':
                Estu = InputMaestro(True, "Estudiante", ["nombre", "edad", "telefono", "email", "estado"],
                                   Estudiante, "/Users/torres/Documents/pruebas_python/EstudianteInput.json")
                Estu.empezar_la_matanga()
            elif opcion == '3':
                pass
            elif opcion == '4':
                pass
            elif opcion == '5':
                pass
            elif opcion == '6':
                pass
            elif opcion == '7':
                self.set_ciclo(False)
            else:
                print("Opción inválida")
        print("Saliendo del sistema...")

if __name__ == "__main__":
    gestor = InputInscrito(True)
    gestor.empezar_la_matanga()