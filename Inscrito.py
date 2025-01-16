from itertools import count
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"


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
    ClaseIncrito = Inscrito(x, [])
    ClaseIncrito.agregar_estudiante_inscrito_lista(xa)
    ClaseIncrito.agregar_estudiante_inscrito_lista(xb)
    ClaseIncrito.agregar_estudiante_inscrito_lista(xc)
    ClaseIncrito.mostrar_inscrito_lista()
    ClaseIncrito = Inscrito(x, [])

    y = Cursos("español", 5, "A", "salon 14", "se enseña español ")
    ya = Estudiantes("Pepo", 7, "871674998", "pepe123@gmail.com", "vivo")
    ClaseIncrito = Inscrito(y, [])
    ClaseIncrito.agregar_estudiante_inscrito_lista(ya)

    ClaseIncrito = Inscrito(x, [])

    print(f"{VERDE}----POST AGREGAR ESTUDIANTE----{RESET}")
    ClaseIncrito.agregar_a_Lista(x)
    ClaseIncrito.agregar_a_Lista(y)
    ClaseIncrito.mostrar_inscrito_lista()
    print("")


    print(f"{ROJO}----POST ELIMINAR ESTUDIANTE----{RESET}")
    ClaseIncrito.eliminar_a_Lista(0)
    ClaseIncrito.mostrar_inscrito_lista()
    print("")

    print(f"{AMARILLO}----POST EDITAR ESTUDIANTE----{RESET}")
    y = Cursos("Poesia", 1, "B", "salon 8", "se canta en versos")
    ya = Estudiantes("samu", 80, "8710000000", "samugod@gmail.com", "vivo por ahora")
    ClaseIncrito.agregar_estudiante_inscrito_lista(ya)
    a = Inscrito(y, [])

    ClaseIncrito.editar_a_Lista(0, y)
    ClaseIncrito.mostrar_inscrito_lista()

