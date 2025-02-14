import os
from Inscrito import VERDE, AMARILLO, ROJO, RESET

from Inscrito import Inscrito
from Curso import Curso
from Estudiante import Estudiante
from inputEstudiantes import InputEstudiante
from inputCurso import InputCurso

json_path = "/Users/torres/Documents/pruebas_python/InscritoInput.json"
json_estu = "/Users/torres/Documents/pruebas_python/cursoInscrito.json"
json_curs = "/Users/torres/Documents/pruebas_python/estudianteInscritot.json"

class InputInscrito:

    def __init__(self, ciclo=True, superCurso=None, superEstudiante=None, superInscrito=0):
        self.__ciclo = ciclo
        if superCurso is None:
            self.superCurso = Curso()
            if os.path.exists(json_curs):
                print("añadiendo curso...")
                self.superCurso.obtencion(json_curs, Curso, None, None)
            else:
                print("no se a encontrado ningun estudiante por el momento y se encuentra vacio a la espera de datos")
                self.superCurso.crear_json(json_curs, [])
        else:
            self.superCurso = superCurso
            self.superCurso.depositar_datos(json_curs)  # esto debe de ir?
        if superEstudiante is None:
            self.superEstudiante = Estudiante()
            if os.path.exists(json_estu):
                print("añadiendo Estudiante...")
                self.superEstudiante.obtencion(json_estu, None, Estudiante, None)
            else:
                print("no se a encontrado ningun estudiante por el momento y se encuentra vacio a la espera de datos")
                self.superEstudiante.crear_json(json_estu, [])
        else:
            self.superEstudiante = superEstudiante
            self.superEstudiante.depositar_datos(json_estu)  # esto debe de ir?

        if superInscrito is None:
            self.superInscrito = Inscrito()
            if os.path.exists(json_estu):
                print("añadiendo Estudiante...")
                self.superInscrito.obtencion(json_estu, None, Estudiante, None)
            else:
                print("no se a encontrado ningun estudiante por el momento y se encuentra vacio a la espera de datos")
                self.superInscrito.crear_json(json_estu, [])
        else:
            self.superInscrito = superEstudiante
            self.superInscrito.depositar_datos(json_estu)  # esto debe de ir?
        print(self.superInscrito)


    def inicializacion(self):
        if os.path.exists(json_path):
            print(f"Añadiendo Inscritos...")
            self.superInscrito.obtencion(json_path, Curso, Estudiante, Inscrito)
            print(self.superInscrito)
        else:
            print(f"No se encontró ningún Inscrito. Creando archivo...")
            self.superEstudiante.crear_json(json_path, [])

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
                Cur = InputCurso(True,Curso)
                x = Cur.empezarLaMatanga()
                print(x)
            elif opcion == '2':
                Estu = InputEstudiante(True, Estudiante)
                Estu.empezarLaMatanga()
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