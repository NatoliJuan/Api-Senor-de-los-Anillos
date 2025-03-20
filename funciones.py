import requests
import json
import unidecode

def obtener_libros():

    nombres_libros = []

    respuesta = requests.get("https://the-one-api.dev/v2/book") 

    datos = respuesta.json()
    
    with open("./data/libros.json","w") as f:
        json.dump(datos,f,indent=4)

    libros = datos["docs"]

    for libro in libros:
        name = unidecode.unidecode(libro["name"]).lower()

        nombres_libros.append(name)
    
    return nombres_libros 
    
def obtener_capitulos():

    nombre_capitulos = []

    eleccion1 = "5cf5805fb53e011a64671582"
    eleccion2 = "5cf58077b53e011a64671583"
    eleccion3 = "5cf58080b53e011a64671584"

    while True:
        try: 
            eleccion = int(input("""Elige el libro que prefieres: 1, 2 o 3. 
                                 
1-> "The Fellowship Of The Ring",
2-> "The Two Towers,
3-> "The Return Of The King": """))

            if eleccion == 1:
                eleccion = eleccion1
            elif eleccion == 2:
                eleccion = eleccion2
            elif eleccion == 3:
                eleccion = eleccion3

        except ValueError:
            print("Introduce un valor correto")
                
        respuesta = requests.get(f"https://the-one-api.dev/v2/book/{eleccion}/chapter") 
    
        datos = respuesta.json()

        with open("./data/capitulos.json","w") as f:
            json.dump(datos,f,indent=4)

        capitulos = datos["docs"]

        for capitulo in capitulos:
            chapter = unidecode.unidecode(capitulo["chapterName"]).lower()
            nombre_capitulos.append(chapter)
        
        return nombre_capitulos

def obtener_personajes():

    nombre_id_personajes = {}

    endpoint = "https://the-one-api.dev/v2/character"
    headers = {"Authorization": "Escribe aquí tu tokken"}

    respuesta = requests.get(endpoint, headers=headers)

    datos = respuesta.json()

        
    with open("./data/personajes.json","w") as f:
        json.dump(datos,f,indent=4)

    personajes = datos["docs"]

    for personaje in personajes: 
        nombre_personaje = unidecode.unidecode(personaje["name"]).lower()
        id_personaje = personaje["_id"]
        nombre_id_personajes[nombre_personaje] = id_personaje

        
    return nombre_id_personajes

def obtener_citas():
    
    nombre_id_personajes = obtener_personajes()

    citas_personajes = []

    nombre_personaje = input("Elige el personaje del que quieres obtener sus citas: ").lower()
    
    id_personaje = nombre_id_personajes.get(nombre_personaje)

    if id_personaje:
        endpoint = f"https://the-one-api.dev/v2/character/{id_personaje}/quote"
        headers = {"Authorization": "Escribe aquí tu tokken"}
        
        respuesta = requests.get(endpoint, headers=headers)
        datos = respuesta.json()

        with open("./data/citas.json", "w") as f:
            json.dump(datos, f, indent=4)

        citas = datos["docs"]

        for cita in citas:
            dialogo = unidecode.unidecode(cita["dialog"]).lower()
            citas_personajes.append(dialogo)
    else:
        print("No se encontró ningún personaje con ese nombre.")

    return citas_personajes
