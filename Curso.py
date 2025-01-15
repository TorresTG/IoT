from symtable import Class
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"


class Curso:

    def __init__(self, nombre = None, grado= None, seccion=None, salon=None, descripcion=None):
        if all(arg is None for arg in [nombre, grado, seccion, salon, descripcion]):
            self.__mc = []
        else:
            self.__nombre = nombre
            self.__grado = grado
            self.__seccion = seccion
            self.__salon = salon
            self.__descripcion = descripcion


    def __str__(self):
        return f"{self.__nombre}\n{self.__grado}\n{self.__seccion}\n{self.__salon}\n{self.__descripcion}"

    @property
    def nombre(self):
        return self.__nombre

    @property
    def grado(self):
        return self.__grado

    @property
    def seccion(self):
        return self.__seccion

    @property
    def salon(self):
        return self.__salon

    @property
    def descripcion(self):
        return self.__descripcion

    def set_nombre(self, value):
        self.__nombre = value

    def set_grado(self, value):
        self.__grado = value

    def set_seccion(self, value):
        self.__seccion = value

    def set_salon(self, value):
        self.__salon = value

    def set_descripcion(self, value):
        self.__descripcion = value

# ----------------------------------------- parte nueva -------

    def agregar_a_ListaCursos(self, curso):
        self.__mc.append(curso)

    def eliminar_a_ListaCursos(self, index):
        if 0 <= index < len(self.__mc):
            del self.__mc[index]
        else:
            print(f"No existe el valor en la posicion: {index}")

    def editar_a_ListaCursos(self, index, nuevo_curso):
        if 0 <= index < len(self.__mc):
            self.__mc[index] = nuevo_curso
        else:
            print(f"No existe el valor en la posicion: {index}")

    def mostrar_ListaCursos(self):
        for x in self.__mc:
            print(x)
            print("--------")




if __name__ =="__main__":


    varios_cursos = Curso()
    x = Curso("matematicas", 5,
              "A", "salon 17", "se enseñan formulas basicas")

    y = Curso("geologia", 6,
              "B", "salon 22", "se miran las gemas")

    z = Curso("español", 3,
              "A", "salon 4", "se estudia el lenguaje")

    print(f"{VERDE}----POST AGREGAR CURSOS----{RESET}")
    varios_cursos.agregar_a_ListaCursos(x)
    varios_cursos.agregar_a_ListaCursos(y)
    varios_cursos.agregar_a_ListaCursos(z)
    varios_cursos.mostrar_ListaCursos()
    print("")

    print(f"{ROJO}----POST ELIMINAR CURSOS----{RESET}")
    varios_cursos.eliminar_a_ListaCursos(1)
    varios_cursos.mostrar_ListaCursos()
    print("")

    print(f"{AMARILLO}----POST EDITAR CURSOS----{RESET}")
    a = Curso("cartografia", 1, "C",
              "salon 10", "se estudia la forma de los paisajes")
    b = Curso("poesia", 2, "D",
              "salon 3", "se estudia la voz a traves de las palabras")

    varios_cursos.editar_a_ListaCursos(0, a)
    varios_cursos.editar_a_ListaCursos(1, b)
    varios_cursos.mostrar_ListaCursos()




