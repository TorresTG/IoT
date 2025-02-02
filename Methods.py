import json
import os
documents_path = os.path.expanduser("~/Documents")
base_name = "inscrito"
extension = ".json"

class Methods:

    def __init__(self):
        self.lista_clases = []

    def agregar_a_Lista(self, clase):
        self.lista_clases.append(clase)

    def eliminar_a_Lista(self, index):
        if 0 <= index < len(self.lista_clases):
            del self.lista_clases[index]
        else:
            print(f"No existe el valor en la posicion: {index}")

    def editar_a_Lista(self, index, nueva_clase):
        if 0 <= index < len(self.lista_clases):
            self.lista_clases[index] = nueva_clase
        else:
            print(f"No existe el valor en la posicion: {index}")

    def mostrar_Lista(self):
        for x in self.lista_clases:
            if isinstance(x, dict):
                print(json.dumps(x, indent=4, ensure_ascii=False) + ",")
            else:
                print(f"{x},")

    def jsonObject(self, Clase_a_guardar):
        counter = 1
        file_path = "/Users/torres/Documents/inscrito.json"

        with open(file_path, "w") as file:
            file.write(str(Clase_a_guardar))
        print(f"El archivo se guardara en: {file_path}")
        return file_path


