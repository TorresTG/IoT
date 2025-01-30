import json
import os

from itertools import count

ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"
documents_path = os.path.expanduser("~/Documents")

from Curso import Curso
from Estudiante import Estudiante
from Methods import Methods


class Inscrito(Methods):

    def __init__(self, cursos=None, estudiantes=None):
        if (cursos or estudiantes) is None:
            super().__init__()
        else:
            self.curso = cursos
            self.estudiantes = Estudiante()

    def interpretar_inscritos(self, datos_del_json):
        lista_inscripciones = json.loads(datos_del_json)
        for item in lista_inscripciones:
            INSCRIPCION = Inscrito(Curso.interpretar_Curso(item))
            # Agregar estudiantes al inscrito

            arreglo_estudiante = [Estudiante.interpretar_Estudiante(item)]
            for estudiante in arreglo_estudiante:
                INSCRIPCION.estudiantes.agregar_a_Lista(estudiante)
        return INSCRIPCION


if __name__ == "__main__":
    superInscri = Inscrito()

    print(f"{VERDE}----AÑADIR INSCRIPCIONES----{RESET}")
    x = Curso("matematicas", 5, "A", "salon 17", "se ensenan formulas basicas")
    xa = Estudiante("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")
    xb = Estudiante("juan", 7, "871677777", "saul@gmail.com", "vivo")
    xc = Estudiante("dante", 9, "8714563345", "dante@gmail.com", "muerto")

    z = Curso("manualidades", 9, "T", "salon 100", "se ensena a usar la mano")
    za = Estudiante("Ana", 29, "6666666666", "anamaseter@gmail.com", "ascendiendo a dios")

    inscripcion1 = Inscrito(x)
    inscripcion1.estudiantes.agregar_a_Lista(xa)
    inscripcion1.estudiantes.agregar_a_Lista(xb)
    superInscri.agregar_a_Lista(inscripcion1)

    inscripcion2 = Inscrito(z)
    inscripcion2.estudiantes.agregar_a_Lista(za)
    superInscri.agregar_a_Lista(inscripcion2)
    print(superInscri)
    print("")
    print("se agrego estudiante dante")
    print("")

    inscripcion1.estudiantes.agregar_a_Lista(xc)
    print(superInscri)

    print(f"\n{ROJO}----ELIMINAR INSCRIPCIONES----{RESET}")

    superInscri.eliminar_a_Lista(1)
    print(superInscri)

    print(f"\n{AMARILLO}----EDITAR INSCRIPCIONES----{RESET}")
    y = Curso("espanol", 5, "A", "salon 14", "se ensena espanol")
    yd = Estudiante("Noa", 8, "8714563324", "noe@gmail.com", "posiblemente vivo")
    ye = Estudiante("paolin", 18, "9990001111", "locopaolin@gmail.com", "muerto")
    yf = Estudiante("SanFaldon", 67, "8777666555", "faldonsin123@gmail.com", "Vivo")

    inscripcion3 = Inscrito(y)
    inscripcion3.estudiantes.agregar_a_Lista(yd)
    inscripcion3.estudiantes.agregar_a_Lista(ye)
    inscripcion3.estudiantes.agregar_a_Lista(yf)

    superInscri.editar_a_Lista(0, inscripcion3)
    # superInscri.mostrar_Lista()
    print(superInscri)

    base_name = "inscrito"
    extension = ".json"
    counter = 1
    file_path = os.path.join(documents_path, f"{base_name}{extension}")

    while os.path.exists(file_path):
        file_path = os.path.join(documents_path, f"{base_name}_{counter}{extension}")
        counter += 1

    #with open(file_path, "w") as file:
        #file.write(str(superInscri))

    #print(f"Archivo guardado en: {file_path}")

    #print(f"mos: {file_path}")

    print(f"\n{ROJO}----MOSTRAR DATOS DEL JSON----{RESET}")

    ruta_json = "/Users/torres/Documents/inscrito.json"

    # Leer el archivo y guardar su contenido en datos_json
    with open(ruta_json, "r", encoding="utf-8") as archivo:
        datos_json = archivo.read()

    superInscri.agregar_a_Lista(inscripcion1.interpretar_inscritos(datos_json))

    print(superInscri)





