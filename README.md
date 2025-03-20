# Api Señor de los anillos 🧙‍♂️📚

<img src="img/anillos.png" alt="Logo anillos" width="300">

Este proyecto permite interactuar con una API pública del Señor de los Anillos. A través de un menú interactivo en la terminal, el usuario puede acceder a información sobre los libros, los capítulos de los libros, los personajes y las citas de los personajes. El código está estructurado para hacer consultas específicas a la API y mostrar los resultados de manera clara y ordenada.

## Funcionalidades 🚀

El programa ofrece las siguientes opciones:

1. **Devuelve todos los libros** 📖: Muestra una lista de todos los libros disponibles en la API.
2. **Selecciona un libro y devuelve los capítulos** 📑: Permite al usuario seleccionar un libro y ver todos sus capítulos.
3. **Devuelve todos los personajes** 🧝‍♀️🧙‍♂️: Muestra una lista de todos los personajes presentes en los libros.
4. **Elige un personaje y devuelve todas sus citas** 💬: Permite elegir un personaje y ver todas las citas asociadas con él.

## Requisitos 📦

Para utilizar este código, necesitas tener instalado Python y las siguientes bibliotecas:

- `requests` 🌐
- `json` 💾

## Cómo conseguir el token 🛠️
Para interactuar con la API, necesitarás un token de autorización. Sigue estos pasos para obtenerlo:

Regístrate en la API: Visita el sitio web de la API: https://the-one-api.dev
Crea una cuenta: Si no tienes una cuenta, regístrate y sigue las instrucciones para obtener acceso.
Obtén tu token: Después de crear una cuenta, podrás generar un token desde tu perfil. Copia este token, ya que lo necesitarás para hacer las consultas a la API.

## Uso 💻
Clona o descarga este repositorio.

Coloca el token obtenido en el archivo utils/funciones.py en la sección donde se configura la autorización de la API. Ejemplo:

headers = {
    "Authorization": "Bearer TU_TOKEN_AQUI"
}
Ejecuta el código principal. Al ejecutar el archivo, aparecerá un menú en la terminal para que puedas elegir qué información deseas obtener.

python main.py

Selecciona una de las opciones disponibles (1, 2, 3 o 4) para obtener la información correspondiente.

Ejemplo de salida 📊
Cuando seleccionas una opción, el programa devuelve la información correspondiente en formato JSON. Por ejemplo:

Si seleccionas "1" para obtener todos los libros, la salida será similar a:

json
Copiar código
[
    {
        "id": "5cf58080b53e011a64671582",
        "name": "The Fellowship of the Ring",
        "author": "J.R.R. Tolkien",
        "pages": 423
    },
    {
        "id": "5cf58080b53e011a64671583",
        "name": "The Two Towers",
        "author": "J.R.R. Tolkien",
        "pages": 352
    },
    ...
]

## ¡Disfruta explorando el mundo de El Señor de los Anillos a través de la API! 🌍

## Autor
Juan Natoli




