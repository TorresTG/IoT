import json
import os


class Methods:

    def __init__(self):
        self.lista_clases = []

    @property
    def lista(self):
        return self.lista_clases

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

    def crear_json(self, ruta, clase_a_guardar):
        if os.path.exists(ruta):
            print(f"Actualizando el archivo {ruta}...")

            with open(ruta, "r") as file:
                datos_existentes = json.load(file)

            nuevos_datos = json.loads(str(clase_a_guardar))

            datos_existentes += nuevos_datos

            with open(ruta, "w") as file:
                json.dump(datos_existentes, file, indent=4, ensure_ascii=False)
        else:
            print(f"Creando archivo en la ruta {ruta}")
            new_data = json.loads(str(clase_a_guardar))
            with open(ruta, "w") as file:
                json.dump(new_data, file, indent=4, ensure_ascii=False)


    # hacer que este metodo obtenga los elementos de curso.json, inscrito.json y estudiante.json para dividir la lectura
    # de la inserccion de datos
    def leer_datos(self, ruta):
        if os.path.exists(ruta):
            with open(ruta, "r", encoding="utf-8") as archivo:
                return json.load(archivo)
        else:
            print(f"Creando archivo en la ruta {ruta}")
            new_data = []
            with open(ruta, "w") as file:
                json.dump(new_data, file, indent=4, ensure_ascii=False)

    def obtencion(self, ruta, Curso=None, Estudiante=None, Inscrito=None):
        data = self.leer_datos(ruta)
        temp_list = []
        if Inscrito:
            for item in data:
                curso = Curso(**item["curso"]) if "curso" in item else None
                insc = Inscrito(curso)
                for est_data in item.get("estudiantes", []):
                    estudiante = Estudiante(**est_data)
                    insc.estudiantes.agregar_a_Lista(estudiante)
                temp_list.append(insc)
        return temp_list

    def depositar_datos(self, ruta):
        if os.path.exists(ruta):
            lista_a_guardar = [objeto.to_dict() for objeto in self.lista_clases]
            with open(ruta, "w", encoding="utf-8") as archivo:
                json.dump(lista_a_guardar, archivo, indent=4, ensure_ascii=False)
            print(f"Datos guardados en {ruta}")
        else:
            print("No Existe Ruta")

    def depositar_uno(self, ruta):
        if self.lista_clases:
            ultimo = self.lista_clases[-1].to_dict()
            with open(ruta, "r+") as f:
                datos = json.load(f)
                datos.append(ultimo)
                f.seek(0)
                json.dump(datos, f, indent=4)
