
class Methods:

    def __init__(self, *args):
        if all(arg is None for arg in args):
            self.__lista_Cursos = []

    def __str__(self):
        return "\n".join(
            f"{key} : \033[35m{value}\033[0m" for key, value in self.__dict__.items()
            if not key.startswith('_Methods__')
        )

    def agregar_a_Lista(self, clase):
        self.__lista_Cursos.append(clase)

    def eliminar_a_Lista(self, index):
        if 0 <= index < len(self.__lista_Cursos):
            del self.__lista_Cursos[index]
        else:
            print(f"No existe el valor en la posicion: {index}")

    def editar_a_Lista(self, index, nueva_clase):
        if 0 <= index < len(self.__lista_Cursos):
            self.__lista_Cursos[index] = nueva_clase
        else:
            print(f"No existe el valor en la posicion: {index}")

    def mostrar_Lista(self):
        for x in self.__lista_Cursos:
            print(x)
            print("--------")
