from itertools import count



from Curso import Curso as Cursos
from Estudiante import Estudiante as Estudiantes
from Methods import Methods


class Inscrito(Methods):

    def __init__(self, cursos = None, estudiantes = None):
        if (cursos or estudiantes) is None:
            super().__init__()
            print("se heredo")
        elif estudiantes is not None and cursos is None:
            self.__curso = None
            self.__estudiantes = estudiantes
            print("obtuvo el estudiante")
        elif estudiantes is None and cursos is not None:
            self.__curso = cursos
            self.__estudiantes = None
            print("obtuvo el curso")
        else:
            self.__curso = cursos
            self.__estudiantes = estudiantes
            print("ambos")



    def insc_agregar(self, estu: Estudiantes):
        self.__estudiantes.append(estu)

    def insc_eliminar(self, index):
        if 0 <= index < len(self.__estudiantes):
            del self.__estudiantes[index]
        else:
            print(f"No existe el valor en la posicion: {index}")

    def insc_editar(self, index, nuevo_curso):
        if 0 <= index < len(self.__estudiantes):
            self.__estudiantes[index] = nuevo_curso
        else:
            print(f"No existe el valor en la posicion: {index}")

    def insc_mostrar(self):
        a = True
        for propiedades_estudiantes in self.__estudiantes:
            if a:
                print("Curso:")
                print("\n".join(
                    f"\t{key[8:]} : \033[35m{value}\033[0m"  # Eliminar el prefijo '__Curso__'
                    for key, value in self.__curso.__dict__.items()
                    if key.startswith(f"_{self.__curso.__class__.__name__}__")))
                print("\t--------")

                a = False
            print(propiedades_estudiantes)
            print("--------")




if __name__ == "__main__":
    superInscri = Inscrito(None,None)
    x = Cursos("matematicas", 5, "A", "salon 17", "se enseñan formulas basicas")
    xa = Estudiantes("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")
    xb = Estudiantes("juan", 7, "871677777", "saul@gmail.com", "vivo")
    xc = Estudiantes("dante", 9, "8714563345", "dante@gmail.com", "muerto")

    superInscri.agregar_a_Lista(Inscrito(x,xa))
    superInscri.agregar_a_Lista(Inscrito(x,xb))
    superInscri.agregar_a_Lista(Inscrito(x,xc))
    superInscri.mostrar_Lista()

    y = Cursos("español", 5, "A", "salon 14", "se enseña español ")
    yd = Estudiantes("Noa", 8, "8714563324", "noe@gmail.com", "posiblemente vivo")
    ye = Estudiantes("paolin", 18, "9990001111", "locopaolin@gmail.com", "muerto")
    superInscri.agregar_a_Lista(Inscrito(y, yd))
    superInscri.agregar_a_Lista(Inscrito(y, ye))


    yf = Estudiantes("sanFaldon", 67, "8777666555", "faldonsin123@gmail.com", "vivo")

    superInscri.editar_a_Lista(1, (Inscrito(y, yf)))
    superInscri.eliminar_a_Lista(0)
    superInscri.mostrar_Lista()