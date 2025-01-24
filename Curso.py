import json
from symtable import Class
from Methods import Methods
ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"





class Curso(Methods):

    def __init__(self, nombre = None, grado= None, seccion=None, salon=None, descripcion=None):
        if (nombre or grado or seccion or salon or descripcion) is None:
            super().__init__()
        else:
            self.__nombre = nombre
            self.__grado = grado
            self.__seccion = seccion
            self.__salon = salon
            self.__descripcion = descripcion

    def to_dict(self):
        return {
            "nombre": self.__nombre,
            "grado": self.__grado,
            "seccion": self.__seccion,
            "salon": self.__salon,
            "descripcion": self.__descripcion
        }


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

if __name__ =="__main__":
    ClaseCurso = Curso()
    x = Curso("matematicas", 5,
              "A", "salon 17", "se ensenan formulas basicas")

    y = Curso("geologia", 6,
              "B", "salon 22", "se miran las gemas")

    z = Curso("espanol", 3,
              "A", "salon 4", "se estudia el lenguaje")

    print(f"{VERDE}----POST AGREGAR CURSOS----{RESET}")
    ClaseCurso.agregar_a_Lista(x)
    ClaseCurso.agregar_a_Lista(y)
    ClaseCurso.agregar_a_Lista(z)
    ClaseCurso.mostrar_Lista()
    print("")

    print(f"{ROJO}----POST ELIMINAR CURSOS----{RESET}")
    ClaseCurso.eliminar_a_Lista(1)
    ClaseCurso.mostrar_Lista()
    print("")

    print(f"{AMARILLO}----POST EDITAR CURSOS----{RESET}")
    a = Curso("cartografia", 1, "C",
              "salon 10", "se estudia la forma de los paisajes")
    b = Curso("poesia", 2, "D",
              "salon 3", "se estudia la voz a traves de las palabras")

    ClaseCurso.editar_a_Lista(0, a)
    ClaseCurso.editar_a_Lista(1, b)
    ClaseCurso.mostrar_Lista()




