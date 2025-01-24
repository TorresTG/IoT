import json
from itertools import count
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"


from Curso import Curso as Cursos
from Estudiante import Estudiante as Estudiantes
from Methods import Methods


class Inscrito(Methods):

    def __init__(self, cursos = None, estudiantes = None):
        if (cursos or estudiantes) is None:
            super().__init__()
        else:
            self.__curso = cursos
            self.__estudiantes = estudiantes if estudiantes is not None else []

    def agregar_estudiante(self, estudiante):
        if estudiante not in self.__estudiantes:
            self.__estudiantes.append(estudiante)
        else:
            print(f"ya existe el estudiante")

    def eliminar_estudiante(self, estudiante):
        if estudiante in self.__estudiantes:
            self.__estudiantes.remove(estudiante)
        else:
            print(f"no exite el estudiante: {estudiante}")

    def editar_inscripcion(self, index, nuevos_curso=None, nuevos_estudiantes=[]):
        if 0 <= index < len(self.lista_clases):
            clase_actual = self.lista_clases[index]
            if nuevos_curso is not None:
                clase_actual.__curso = nuevos_curso

            if nuevos_estudiantes != [None]:
                clase_actual.__estudiantes = nuevos_estudiantes

            self.lista_clases[index] = clase_actual
        else:
            print(f"No existe nada en la posision: {index}")


if __name__ == "__main__":
    superInscri = Inscrito()

    print(f"{VERDE}----AÑADIR INSCRIPCIONES----{RESET}")
    x = Cursos("matematicas", 5, "A", "salon 17", "se enseñan formulas basicas")
    xa = Estudiantes("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")
    xb = Estudiantes("juan", 7, "871677777", "saul@gmail.com", "vivo")
    xc = Estudiantes("dante", 9, "8714563345", "dante@gmail.com", "muerto")


    z = Cursos("manualidades", 9, "T", "salon 100", "se enseña a usar la mano")
    za = Estudiantes("Ana", 29, "6666666666", "anamaseter@gmail.com", "ascendiendo a dios")

    inscripcion1 = Inscrito(x, [xa, xb])
    superInscri.agregar_a_Lista(inscripcion1)


    inscripcion2 = Inscrito(z, [za])
    superInscri.agregar_a_Lista(inscripcion2)

    superInscri.mostrar_Lista()



    print("")
    print("se agrego estudiante dante")
    print("")
    inscripcion1.agregar_estudiante(xc)
    superInscri.mostrar_Lista()

    print(f"\n{ROJO}----ELIMINAR INSCRIPCIONES----{RESET}")

    superInscri.eliminar_a_Lista(1)
    superInscri.mostrar_Lista()

    print(f"\n{AMARILLO}----EDITAR INSCRIPCIONES----{RESET}")
    y = Cursos("español", 5, "A", "salon 14", "se enseña español")
    yd = Estudiantes("Noa", 8, "8714563324", "noe@gmail.com", "posiblemente vivo")
    ye = Estudiantes("paolin", 18, "9990001111", "locopaolin@gmail.com", "muerto")
    yf = Estudiantes("SanFaldon", 67, "8777666555", "faldonsin123@gmail.com", "Vivo")

    superInscri.editar_inscripcion(0, nuevos_curso=y, nuevos_estudiantes=[yd, ye, yf])
    superInscri.mostrar_Lista()
