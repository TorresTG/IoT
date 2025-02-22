import json
import os

nombre_archivo = "inscrito.json"
ruta_predeterminadaIns= "/Users/torres/Documents/pruebas_python/" + nombre_archivo

ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
MORADO = "\033[35m"
RESET = "\033[0m"

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



    def __str__(self):
        if hasattr(self, 'lista_clases') and self.lista_clases:
            inscripciones_data = [json.loads(str(inscripcion)) for inscripcion in self.lista_clases]
            return json.dumps(inscripciones_data, indent=4, ensure_ascii=False)
        else:
            curso_data = json.loads(str(self.curso)) if hasattr(self, 'curso') else None
            estudiantes_data = []
            if hasattr(self, 'estudiantes') and hasattr(self.estudiantes, 'lista_clases'):
                estudiantes_data = [json.loads(str(est)) for est in self.estudiantes.lista_clases]

            inscripcion_data = {
                "curso": curso_data,
                "estudiantes": estudiantes_data
            }
            return json.dumps(inscripcion_data, indent=4, ensure_ascii=False)

    def to_dict(self):
        return {
            "curso": self.curso.to_dict() if self.curso else {},
            "estudiantes": [estudiante.to_dict() for estudiante in self.estudiantes.lista_clases] if self.estudiantes else []
        }




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

    print(superInscri)
    superInscri.crear_json(ruta_predeterminadaIns, superInscri)

    print(f"Se guardaron los datos en {ruta_predeterminadaIns}")
    

    """ejemplo:
    
    x = Curso("matematicas", 5, "A", "salon 17", "se ensenan formulas basicas")
    xa = Estudiante("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")"""
    x = Curso("matematicas", 5, "A", "salon 17", "se ensenan formulas basicas")
    xa = Estudiante("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")

    inscripcion1 = Inscrito(x)
    inscripcion1.estudiantes.agregar_a_Lista(xa)
    superInscri.agregar_a_Lista(inscripcion1)
    print(superInscri)

    """print(f"\n{ROJO}----MOSTRAR DATOS DEL JSON----{RESET}")
    superInscri.leer_json(ruta_predeterminadaIns, Curso, Estudiante, Inscrito)

    print(superInscri)"""





