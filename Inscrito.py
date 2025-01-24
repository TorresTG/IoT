from itertools import count



from Curso import Curso as Cursos
from Estudiante import Estudiante as Estudiantes
from Methods import Methods


class Inscrito(Cursos, Estudiantes, Methods):

    def __init__(self, cursos: Cursos, estudiantes: []):
        if Cursos is None:
            super().__init__()
        else:
            self.__curso = cursos
            self.__estudiantes = estudiantes


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
    superInscri = Inscrito(None,[])
    x = Cursos("matematicas", 5, "A", "salon 17", "se enseñan formulas basicas")
    inscripcion1 = Inscrito(x, [])
    xa = Estudiantes("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")
    xb = Estudiantes("juan", 7, "871677777", "saul@gmail.com", "vivo")
    xc = Estudiantes("dante", 9, "8714563345", "dante@gmail.com", "muerto")

    inscripcion1.insc_agregar(xa)
    inscripcion1.insc_agregar(xb)
    inscripcion1.insc_agregar(xc)
    inscripcion1.insc_mostrar()

    superInscri.agregar_a_Lista(inscripcion1)
    y = Cursos("español", 5, "A", "salon 14", "se enseña español ")
    inscripcion2 = Inscrito(y, [])
    yd = Estudiantes("Noa", 8, "8714563324", "noe@gmail.com", "posiblemente vivo")
    ye = Estudiantes("paolin", 18, "9990001111", "locopaolin@gmail.com", "muerto")
    inscripcion2.insc_agregar(yd)
    inscripcion2.insc_agregar(ye)

    yf = Estudiantes("sanFaldon", 67, "8777666555", "faldonsin123@gmail.com", "vivo")

    inscripcion2.insc_editar(1, yf)
    inscripcion2.insc_eliminar(0)
    inscripcion2.insc_mostrar()





