class Pelicula:
    def __init__(peli, nombre, director, actor_principal, recaudacion_acumulada):
        peli.nombre = nombre
        peli.director = director
        peli.actor_principal = actor_principal
        peli.recaudacion_acumulada = recaudacion_acumulada

    def mostrar_datos(peli):
        print("Nombre:", peli.nombre)
        print("Director:", peli.director)
        print("Actor Principal:", peli.actor_principal)
        print("Recaudación Acumulada:", peli.recaudacion_acumulada)

    def cambiar_actor_principal(peli, nuevo_actor_principal):
        peli.actor_principal = nuevo_actor_principal

    def agregar_recaudacion(peli, cantidad):
        peli.recaudacion_acumulada += cantidad


# Ejemplo de uso
if __name__ == "__main__":
    pelicula = Pelicula("Titanic", "James Cameron", "Leonardo DiCaprio", 2200000000)
    pelicula.mostrar_datos()

    print("\nCambiando actor principal...")
    pelicula.cambiar_actor_principal("Kate Winslet")
    pelicula.mostrar_datos()

    print("\nAgregando recaudación...")
    pelicula.agregar_recaudacion(100000000)
    pelicula.mostrar_datos()

