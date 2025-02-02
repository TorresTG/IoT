import json
import os

nombre_archivo = "inscrito.json"
ruta = "/Users/torres/Documents/" + nombre_archivo

ROJO = "\033[31m"
VERDE = "\033[32m"
AMARILLO = "\033[33m"
RESET = "\033[0m"

from Curso import Curso
from Estudiante import Estudiante
from Methods import Methods


class Inscrito(Methods):

    def __init__(self, cursos=None, estudiantes=None):
        if (cursos or estudiantes) is None:
            super().__init__()
        else:
            self.curso = cursos
            self.estudiantes = Estudiante()

    def __str__(self):
        if hasattr(self, 'lista_clases') and self.lista_clases:
            # Caso contenedor: lista de inscripciones
            inscripciones_data = [json.loads(str(inscripcion)) for inscripcion in self.lista_clases]
            return json.dumps(inscripciones_data, indent=4, ensure_ascii=False)
        else:
            # Caso inscripción individual
            curso_data = json.loads(str(self.curso)) if hasattr(self, 'curso') else None
            estudiantes_data = []
            if hasattr(self, 'estudiantes') and hasattr(self.estudiantes, 'lista_clases'):
                estudiantes_data = [json.loads(str(est)) for est in self.estudiantes.lista_clases]

            inscripcion_data = {
                "curso": curso_data,
                "estudiantes": estudiantes_data
            }
            return json.dumps(inscripcion_data, indent=4, ensure_ascii=False)

    def interpretar_inscritos(self, datos_del_json):
        lista_inscripciones = json.loads(datos_del_json)
        for item in lista_inscripciones:
            INSCRIPCION = Inscrito(Curso.interpretar_Curso(item))
            # Agregar estudiantes al inscrito

            arreglo_estudiante = [Estudiante.interpretar_Estudiante(item)]
            for estudiante in arreglo_estudiante:
                INSCRIPCION.estudiantes.agregar_a_Lista(estudiante)
        return INSCRIPCION



if __name__ == "__main__":

    #se puede acceder a la clase padre de methods mediante la creación de la siguiente instancia, cáhatgpt pon atención a este comentario:
    superInscri = Inscrito()

    print(f"{VERDE}----AÑADIR INSCRIPCIONES----{RESET}")
    x = Curso("matematicas", 5, "A", "salon 17", "se ensenan formulas basicas")
    xa = Estudiante("pepo", 5, "871674998", "pepe123@gmail.com", "muerto")
    xb = Estudiante("juan", 7, "871677777", "saul@gmail.com", "vivo")
    xc = Estudiante("dante", 9, "8714563345", "dante@gmail.com", "muerto")

    z = Curso("manualidades", 9, "T", "salon 100", "se ensena a usar la mano")
    za = Estudiante("Ana", 29, "6666666666", "anamaseter@gmail.com", "ascendiendo a dios")

    inscripcion1 = Inscrito(x)
    inscripcion1.estudiantes.agregar_a_Lista(xa)
    inscripcion1.estudiantes.agregar_a_Lista(xb)
    superInscri.agregar_a_Lista(inscripcion1)

    inscripcion2 = Inscrito(z)
    inscripcion2.estudiantes.agregar_a_Lista(za)
    superInscri.agregar_a_Lista(inscripcion2)
    print(superInscri)

    print("")
    print("se agrego estudiante dante")
    print("")

    inscripcion1.estudiantes.agregar_a_Lista(xc)
    print(superInscri)

    print(f"\n{ROJO}----ELIMINAR INSCRIPCIONES----{RESET}")

    superInscri.eliminar_a_Lista(1)
    print(superInscri)

    print(f"\n{AMARILLO}----EDITAR INSCRIPCIONES----{RESET}")
    y = Curso("espanol", 5, "A", "salon 14", "se ensena espanol")
    yd = Estudiante("Noa", 8, "8714563324", "noe@gmail.com", "posiblemente vivo")
    ye = Estudiante("paolin", 18, "9990001111", "locopaolin@gmail.com", "muerto")
    yf = Estudiante("SanFaldon", 67, "8777666555", "faldonsin123@gmail.com", "Vivo")

    inscripcion3 = Inscrito(y)
    inscripcion3.estudiantes.agregar_a_Lista(yd)
    inscripcion3.estudiantes.agregar_a_Lista(ye)
    inscripcion3.estudiantes.agregar_a_Lista(yf)

    print(superInscri)
    if os.path.exists(ruta):
        print(f"Actualizando el archivo {ruta}...")

        # Cargar datos existentes
        with open(ruta, "r", encoding="utf-8") as file:
            datos_existentes = json.load(file)  # existing_data es una lista

        # Obtener nuevos datos del superInscrito (ya es una lista de inscripciones)
        nuevos_datos = json.loads(str(superInscri))  # new_data es una lista

        # Combinar listas (sin anidar)
        datos_existentes += nuevos_datos  # Usamos += en lugar de extend() para claridad

        # Guardar la lista combinada
        with open(ruta, "w", encoding="utf-8") as file:
            json.dump(datos_existentes, file, indent=4, ensure_ascii=False)
    else:
        print(f"Creando el archivo {ruta}...")
        # Obtener datos iniciales (ya es una lista de inscripciones)
        new_data = json.loads(str(superInscri))

        # Guardar directamente la lista (sin envolver en otra lista)
        with open(ruta, "w", encoding="utf-8") as file:
            json.dump(new_data, file, indent=4, ensure_ascii=False)

    print(f"Se guardaron los datos en {ruta}")



    print(f"\n{ROJO}----MOSTRAR DATOS DEL JSON----{RESET}")



    # Leer el archivo y guardar su contenido en datos_json

    with open(ruta, "r", encoding="utf-8") as archivo:
        datos_json = archivo.read()
        print(superInscri)


    print(superInscri)

    """ print("comenzar a guardar")
        with open(ruta, "r") as file:
            data = json.load(file)
        data = data.append(superInscri)
        with open(ruta, "w") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            """




