from Curso import Curso
from InputMaestro import InputMaestro

json_path = "/Users/torres/Documents/pruebas_python/CursoInput.json"

if __name__ == "__main__":
    gestor = InputMaestro(True, "Curso", ["nombre", "grado", "seccion", "salon", "descripcion"],
                        Curso, "/Users/torres/Documents/pruebas_python/CursoInput.json")
    gestor.empezar_la_matanga()