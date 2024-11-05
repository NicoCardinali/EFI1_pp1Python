# API de Gestión de Categorías y Comentarios

Este proyecto define una API REST para la gestión de CELULARES. Proporciona varios endpoints para la autenticación, la gestión de categorías y la obtención de otros detalles. Los endpoints principales incluyen autenticación para obtener un token, CRUD para categorías, y métodos de lectura.

## Endpoints de la API

A continuación se describen los principales endpoints de la API, junto con ejemplos de solicitud y respuesta.

### Autenticación

#### Obtener token de autenticación

- **Método:** `POST`
- **Endpoint:** `/login/`
- **Cuerpo de la solicitud:**
    ```json
    {
        "username": "admin",
        "password": "admin"
    }
    ```
- **Ejemplo de respuesta:**
    {
        "token": "tu_token_de_autenticacion"
    }
    ```

### Categorías

#### Obtener todas las equipos (igual con las demas esquemas)

- **Método:** `GET`
- **Endpoint:** `/equipos/`
- **Cabecera de la solicitud:** `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta:**
    ```json
     [
        {
            "id": 1,
            "nombre": "Nombre de la categoría",
            "anio": 2024,
            "costo": 9999,
            "modelo_id": 1,
            "modelo" {Datos del modelo}
    ```



#### Crear un nuevo equipo

- **Método:** `POST`
- **Endpoint:** `/equipos/`
- **Cabecera de la solicitud:** `Authorization: Token <tu_token_de_autenticacion>`
- **Cuerpo de la solicitud:**
    ```json
    {
        "nombre": "Nuevo equipo",
        "anio": "anio equipo",
        "costo": "costo equipo",
        "modelo_id": "id del modelo elegido"
    }
    ```
- **Ejemplo de respuesta:**
    ```json
    {
            "id": 2,
            "nombre": "Nuevo equipo",
            "anio": "anio equipo",
            "costo": "costo equipo",
            "modelo_id": "id del modelo elegido",
            "modelo": {Datos del modelo}
    }
    ```

#### Actualizar una categoría por ID

- **Método:** `POST`
- **Endpoint:** `/equipos/1`
- **Cabecera de la solicitud:** `Authorization: Token <tu_token_de_autenticacion>`
- **Cuerpo de la solicitud:**
    ```json
    {
        "nombre": "Nuevo nombre",
        "anio": "anio equipo",
        "costo": "costo equipo",
        "modelo_id": "id del modelo elegido"
    }
    ```
- **Ejemplo de respuesta:**: "Equipo actualizado con éxito"

#### Eliminar una categoría por ID

- **Método:** `POST`
- **Endpoint:** `/api/categorias/1`
- **Cabecera de la solicitud:** `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta:** `"Equipo eliminado con éxito"`

### Comentarios

#### Obtener todos los Esquemas

- **Método:** `GET`
- **Endpoint:** `/fabricantes/` "POR EJEMPLO"
- **Cabecera de la solicitud:** `Authorization: Token <tu_token_de_autenticacion>`
- **Ejemplo de respuesta:**
    ```json
    [
        {
            "id": 1,
            "nombre": "Nombre 1",
            "pais_origen": "pais 1"
        }
        {
            "id": 2,
            "nombre": "Nombre 2",
            "pais_origen": "pais 2"
        }
    ]
    ```
