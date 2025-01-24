
class Methods:

    def __init__(self):
        self.__lista_clases = []

    def __str__(self):
        return "\n".join(
            f"{key} : \033[35m{value}\033[0m" for key, value in self.__dict__.items()
            if not key.startswith('_Methods__')
        )

    @property
    def lista_clases(self):
        return self.__lista_clases

    def agregar_a_Lista(self, clase):
        self.__lista_clases.append(clase)

    def eliminar_a_Lista(self, index):
        if 0 <= index < len(self.__lista_clases):
            del self.__lista_clases[index]
        else:
            print(f"No existe el valor en la posicion: {index}")

    def editar_a_Lista(self, index, nueva_clase):
        if 0 <= index < len(self.__lista_clases):
            self.__lista_clases[index] = nueva_clase
        else:
            print(f"No existe el valor en la posicion: {index}")

    def mostrar_Lista(self):
        for x in self.__lista_clases:
            print(x)
            print("--------")