import json



class Methods:

    def __init__(self):
        self.__lista_clases = []

    def __str__(self):
        def clean_key(key):
            return key.lstrip('_').split('__')[-1]

        def process_value(value):
            if isinstance(value, Methods):
                # Procesa los atributos del objeto Methods
                result = {clean_key(k): process_value(v) for k, v in vars(value).items()}
                # este if sirve para quitar el nombre de el arreglo de estudiantes
                if 'lista_clases' in result:
                    return result['lista_clases']
                return result
            elif isinstance(value, list):
                # Procesa cada elemento en una lista recursivamente
                return [process_value(item) for item in value]
            elif isinstance(value, dict):
                # Procesa cada clave-valor en un diccionario
                return {clean_key(k): process_value(v) for k, v in value.items()}
            return value  # Retorna directamente valores simples

        # Procesa la lista interna de clases y convierte a JSON
        serialized_data = [process_value(item) for item in self.lista_clases]
        return json.dumps(serialized_data, indent=4)

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
    """
    def interpretar_json(self, datos_del_json):
        lista_inscripciones = json.loads(datos_del_json)
        for item in lista_inscripciones:
            INSCRIPCION = Inscrito(Curso.interpretar_Curso(item,True))
            # Agregar estudiantes al inscrito

            arreglo_estudiante = [Estudiante.interpretar_Estudiante(item)]
            for estudiante in arreglo_estudiante:
                INSCRIPCION.estudiantes.agregar_a_Lista(estudiante)
        return INSCRIPCION
    """




