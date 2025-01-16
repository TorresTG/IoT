
class Methods:


    def __init__(self, *args):
        if all(arg is None for arg in args):
            self.__lista_Cursos = []

    def __str__(self):
        return "\n".join(
            f"viene de {key} con valor de: \033[35m{value}\033[0m" for key, value in self.__dict__.items()
            if not key.startswith('_Methods__')
        )

    def agregar_a_Lista(self, curso):
        self.__lista_Cursos.append(curso)

    def eliminar_a_Lista(self, index):
        if 0 <= index < len(self.__lista_Cursos):
            del self.__lista_Cursos[index]
        else:
            print(f"No existe el valor en la posicion: {index}")

    def editar_a_Lista(self, index, nuevo_curso):
        if 0 <= index < len(self.__lista_Cursos):
            self.__lista_Cursos[index] = nuevo_curso
        else:
            print(f"No existe el valor en la posicion: {index}")

    def mostrar_Lista(self):
        for x in self.__lista_Cursos:
            print(x)
            print("--------")
