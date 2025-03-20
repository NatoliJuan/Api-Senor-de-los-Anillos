# Si pulsa 1: devuelve todos los libros.
# Si pulsa 2: Selecciona un libro y devulve todos los capítulos.
# Si pulsa 3: Devulve todos los personajes.
# Si pulsa 4 Elige personaje y devuelve todas sus citas.

from utils.funciones import *
# from pruebas import*
def main():
    while True:
        try:
            usuario = int(input("""1- Devuelve los libros.
2- Selecciona un libro y devulve los capitulos.
3- Devuelve los personajes.
4- Elige personaje y devuleve las citas: """))
            print()

            if usuario in [1, 2, 3, 4]:
                break
            else:
                print("Por favor, elige 1, 2, 3 o 4")
        except ValueError:
            print("Introduce un valor correto")

# Si pulsa 1: devuelve todos los libros.
            
    if usuario == 1:
        eleccion1 = obtener_libros()
        mostrar_libros = json.dumps(eleccion1, indent=4)

        print(mostrar_libros)

    # Si pulsa 2: Selecciona un libro y devulve todos los capítulos.
        
    elif usuario ==  2:

        eleccion2 = obtener_capitulos()
        mostrar_capitulos = json.dumps(eleccion2, indent=4)

        print(mostrar_capitulos)
    
    # Si pulsa 3: Devulve todos los personajes.
        
    elif usuario == 3:
        eleccion3 = obtener_personajes()
        mostrar_personajes = json.dumps(eleccion3, indent=4)
        print(mostrar_personajes)
    
    # Si pulsa 4 Elige personaje y devuelve todas sus citas.
        
    else:
        eleccion4 = obtener_citas()
        mostrar_citas = json.dumps(eleccion4, indent=4)

        print(mostrar_citas)

if __name__ == "__main__":
    main()

