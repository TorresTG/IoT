import json


class Methods:

    def __init__(self):
        self.__lista_clases = []

    def __str__(self):
        def clean_key(key):
            return key.lstrip('_').split('__')[-1]

        def serialize(obj):
            if isinstance(obj, (Methods, dict)):
                return {clean_key(key): serialize(value) for key, value in
                        (vars(obj) if isinstance(obj, Methods) else obj).items()}
            if isinstance(obj, list):
                return [serialize(item) for item in obj]
            return obj

        return json.dumps(serialize(self), indent=4)


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
            print(f"{x},")
