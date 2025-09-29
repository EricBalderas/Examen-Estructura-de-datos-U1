# Ejercio 1 crear una lista que reciba nombres de alumnos hasta que se escriba "FIN"
def crear_lista_alumnos():
    """
    Crear una lista de nombres de alumnos hasta que se ingrese "FIN".
    """
    secuencia = []
    while True:
        nombre = input("Introduce el nombre del alumno (o 'FIN' para terminar): ")
        if nombre.upper() == "FIN":
            break
        secuencia.append(nombre)
    return secuencia
# En el main mostramos la lista creada y cuantos alumnos hay
if __name__ == "__main__":
    alumnos = crear_lista_alumnos()
    print("\nLista de Alumnos:")
    for i, alumno in enumerate(alumnos, start=1):
        print(f"{i}. {alumno}")
    print(f"\nTotal de alumnos: {len(alumnos)}")
