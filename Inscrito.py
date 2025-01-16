from itertools import count



from Curso import Curso as Cursos
from Estudiante import Estudiante as Estudiantes
from Methods import Methods


class Inscrito(Cursos, Estudiantes, Methods):

    def __init__(self, cursos: Cursos, estudiantes: []):
        super().__init__()
        self.__curso = cursos
        self.__estudiantes = estudiantes


    def agregar_estudiante_inscrito_lista(self, estu: Estudiantes):
        self.__estudiantes.append(estu)

    def eliminar_estudiante_inscrito_lista(self, index):
        if 0 <= index < len(self.__estudiantes):
            del self.__estudiantes[index]
        else:
            print(f"No existe el valor en la posicion: {index}")

    def editar_estudiante_inscrito_lista(self, index, nuevo_curso):
        if 0 <= index < len(self.__estudiantes):
            self.__estudiantes[index] = nuevo_curso
        else:
            print(f"No existe el valor en la posicion: {index}")

    def mostrar_inscrito_lista(self):
        a = True
        for propiedades_estudiantes in self.__estudiantes:
            if a:
                print("Curso:")
                print(f"    {self.__curso.nombre}")
                print(f"    {self.__curso.grado}")
                print(f"    {self.__curso.seccion}")
                print(f"    {self.__curso.salon}")
                print(f"    {self.__curso.descripcion}")
                print("")
                a = False
            print(propiedades_estudiantes)
            print("--------")






if __name__ == "__main__":
    x = Cursos("matematicas", 5, "A", "salon 17", "se enseñan formulas basicas")
    xa = Estudiantes("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")
    xb = Estudiantes("juan", 7, "871677777", "saul@gmail.com", "vivo")
    xc = Estudiantes("dante", 9, "8714563345", "dante@gmail.com", "muerto")
    inscripcion = Inscrito(x, [])
    inscripcion.agregar_estudiante_inscrito_lista(xa)
    inscripcion.agregar_estudiante_inscrito_lista(xb)
    inscripcion.agregar_estudiante_inscrito_lista(xc)

    y = Cursos("español", 5, "A", "salon 14", "se enseña español ")
    yd = Estudiantes("Pepo", 7, "871674998", "pepe123@gmail.com", "vivo")
    inscripcion.editar_estudiante_inscrito_lista(0, yd)
    inscripcion.eliminar_estudiante_inscrito_lista(1)
    inscripcion.mostrar_inscrito_lista()


