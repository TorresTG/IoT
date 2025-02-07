import os

from Inscrito import Inscrito
from Estudiante import Estudiante

nombre_archivo = "EstudianteInput.json"
ruta_predeterEstu= "/Users/torres/Documents/pruebas_python/" + nombre_archivo

from Inscrito import VERDE, AMARILLO, ROJO, RESET
class InputEstudiante:

    def __init__(self, ciclo = True, superEstudiante = Estudiante()):
        self.__ciclo = ciclo
        self.superEstudiante = superEstudiante
        self.inicializacion()

    def inicializacion(self):
        if os.path.exists(ruta_predeterEstu):
            print("añadiendo estudiantes...")
            self.superEstudiante.prueba1(ruta_predeterEstu, Estudiante)
            print(self.superEstudiante)
        else:
            print("no se a encontrado ningun estudiante por el momento")

    @property
    def ciclo(self):
        return self.__ciclo

    def set_ciclo(self, value):
        self.__ciclo = value

    def empezarLaMatanga(self):
        while self.ciclo is True:
            print(f"--------Gestion De Estudiante--------")
            print(f"{VERDE}1). Agregar Estudiante{RESET}")
            print(f"{AMARILLO}2). Editar Estudiante{RESET}")
            print(f"{ROJO}3). Eliminar Estudiante{RESET}")
            print(f"4). Ver Todas los Estudiantes")
            print(f"5). Salir")
            print("")
            print("")
            print("eliga el numero deseado")
            eleccion = input()
            if eleccion.isdigit():
                eleccion = int(eleccion)
            else:
                print("ingrese un numero plz")
            if eleccion == 1:
                d = {"nombre": str, "edad": str, "telefono": str, "email": str, "estado": str}
                print("-------")
                for key in d.keys():
                    print(f"introducir: {key}")
                    d[key] = f"{input()}"
                    print("-------")
                x = Estudiante(**d)
                self.superEstudiante.agregar_a_Lista(x)
                self.superEstudiante.crear_json(ruta_predeterEstu, self.superEstudiante)
                print("Se ha añadido el estudiante")
                print("-------")
            elif eleccion == 2:
                pass
            elif eleccion == 3:
                pass
            elif eleccion == 4:
                print(self.superEstudiante)
            elif eleccion == 5:
                self.set_ciclo(False)
            else:
                print("ingrese un numero dentro del rango de 1 - 5")
        print("se cerro el programa")

inputs1 = InputEstudiante()
inputs1.empezarLaMatanga()

