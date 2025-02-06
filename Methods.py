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

    def leer_json(self, ruta, Curso, Estudiante, Inscrito):
        with open(ruta, "r", encoding="utf-8") as archivo:
            datos_json = json.load(archivo)

            for objeto in datos_json:
                unCurso = objeto.get("curso")
                if not unCurso:
                    continue
                x = Curso(**unCurso)
                inscripcion = Inscrito(x)

                estudiantes = objeto.get("estudiantes", [])
                estudiantes_Convertido = [Estudiante(**unicoEstudiante) for unicoEstudiante in estudiantes]
                for xa in estudiantes_Convertido:
                    inscripcion.estudiantes.agregar_a_Lista(xa)

                self.agregar_a_Lista(inscripcion)
