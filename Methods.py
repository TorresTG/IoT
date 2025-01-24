import json


class Methods:

    def __init__(self):
        self.__lista_clases = []

    def __str__(self):
        def clean_key(key):
            return key.lstrip('_').split('__')[-1]

        def process_value(value):
            if isinstance(value, Methods):  # Si el valor es otro objeto de la clase, procesar recursivamente
                return {clean_key(k): process_value(v) for k, v in vars(value).items()}
            elif isinstance(value, list):  # Si es una lista, procesar cada elemento
                return [process_value(item) for item in value]
            elif isinstance(value, dict):  # Si es un diccionario, procesar sus valores
                return {clean_key(k): process_value(v) for k, v in value.items()}
            return value  # Devolver valores simples directamente

        # Crear un diccionario con las variables de instancia del objeto
        serialized_data = {clean_key(k): process_value(v) for k, v in vars(self).items()}

        # Convertir a JSON con formato
        return json.dumps([serialized_data], indent=4)


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