
class Pila:
    def __init__(self):
        self.items = []

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]
        return None

def iniciar_programa():
    pila = Pila()
    paginas = ["google.com", "wikipedia.org", "openai.com"]
    
    for pagina in paginas:
        pila.apilar(pagina)
        print(f"Página '{pagina}' cargada y apilada.")

    while True:
        accion = input("Presiona 'v' para volver a la página anterior o 's' para salir: ").lower()
        if accion == "volver":
            pagina_tope = pila.ver_tope()
            if pagina_tope:
                print(f"Volviendo a la página: {pagina_tope}")
                pila.desapilar()
            else:
                print("No hay más páginas en el historial.")
        elif accion == "salir":
            print("Saliendo...")
            break
        else:
            print("Acción no válida. Intentalo de nuevo.")
if __name__ == "__main__":
    iniciar_programa()