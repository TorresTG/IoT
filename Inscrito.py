from Curso import Curso as Cursos
from Estudiante import Estudiante as Estudiantes


class Inscrito(Cursos, Estudiantes):

    def __init__(self, cursos: Cursos, estudiantes: []):
        self.__curso = cursos
        self.__estudiantes = estudiantes

    def agregar_inscrito(self, estu: Estudiantes):
        self.__estudiantes.append(estu)

    def mostrar_inscrito(self):
        print(self.__curso.nombre)
        print(self.__curso.grado)
        print(self.__curso.seccion)
        print("---Estudiantes---")
        for x in self.__estudiantes:
            print(x.nombre)
            print(x.telefono)
            print("--------")


if __name__ == "__main__":
    x = Cursos("matematicas", 5, "A", "salon 17", "se enseñan formulas basicas")

    inscripcion = Inscrito(x, [])
    inscripcion.agregar_inscrito(Estudiantes("pepo", 5, "871674998", "pepe123@gmail.com", "muerto"))
    inscripcion.agregar_inscrito(Estudiantes("juan", 7, "871677777", "saul@gmail.com", "vivo"))
    inscripcion.mostrar_inscrito()