
# API REST DOCUMENTACIÓN

---

## Tabla de contenido

- [Introducción](#introducción)
- [Coquito Amarillo API](#coquito-amarillo-api)
- [Objetivo de la API](#objetivo-de-la-api)
- [Instalación del proyecto](#instalación-del-proyecto)
- [Ejecución de la API](#ejecución-de-la-api)
- [Endpoints de la API](#endpoints-de-la-api)
- [Métodos HTTP utilizados](#métodos-http-utilizados)
- [Códigos de estado HTTP](#códigos-de-estado-http)
- [Validaciones implementadas](#validaciones-implementadas)
- [Manejo de errores](#manejo-de-errores)
- [Consideraciones de uso](#consideraciones-de-uso)
- [Conclusión](#conclusión)

---

# Introducción

---

La presente documentación técnica describe el desarrollo e implementación de una API REST para la empresa Coquito Amarillo S.A.S., orientada a la gestión de clientes, productos y pedidos dentro de una plataforma virtual de artesanías.

La API fue desarrollada utilizando Python, Flask y Flask-RESTful, aplicando una arquitectura basada en servicios REST que permite la comunicación mediante solicitudes HTTP y respuestas en formato JSON. El sistema implementa operaciones CRUD para la administración de información relacionada con clientes, productos y pedidos, incluyendo validaciones de datos, manejo de errores y códigos de estado HTTP.

El proyecto tiene como propósito fortalecer el proceso de gestión de información dentro de la plataforma, permitiendo realizar operaciones de consulta, registro, actualización y eliminación de datos de manera estructurada y organizada.

Adicionalmente, la documentación presenta la estructura general del proyecto, los endpoints implementados, los métodos HTTP utilizados, las validaciones realizadas y las pruebas ejecutadas mediante Postman para verificar el correcto funcionamiento de la API REST desarrollada.

---

# Coquito Amarillo API

---

Coquito Amarillo API es una API REST desarrollada para gestionar los principales procesos de una plataforma de comercio electrónico. Permite administrar clientes, productos y pedidos mediante un conjunto de endpoints diseñados para realizar operaciones de consulta, creación, actualización y eliminación de información.

La API utiliza el formato JSON para el intercambio de datos y sigue una estructura basada en recursos, facilitando la integración con aplicaciones web, móviles o cualquier sistema que requiera interactuar con los servicios ofrecidos. Su diseño busca proporcionar una interfaz clara, organizada y fácil de consumir para la gestión de operaciones relacionadas con el catálogo de productos y el procesamiento de pedidos.

---

# Objetivo de la API

---

La API REST de Coquito Amarillo S.A.S tiene como objetivo permitir la gestión de clientes, productos y pedidos mediante operaciones de consulta, registro, actualización y eliminación de la información a través de servicios web basados en arquitectura REST.

La API utiliza Flask y Flask-RESTful para procesar solicitudes HTTP y generar respuestas en formato JSON, facilitando el intercambio organizado de la información dentro de la plataforma virtual de artesanías.

La API implementa validaciones de datos, manejo de errores y códigos de estado HTTP con el propósito de garantizar un funcionamiento adecuado de los servicios disponibles.

---

# Instalación del proyecto

---

Para realizar la instalación y ejecución de la API REST es necesario contar con un entorno de desarrollo configurado con Python y las dependencias utilizadas durante la implementación del proyecto.

### Tecnologías usadas

La API REST fue desarrollada utilizando diferentes tecnologías y herramientas orientadas al desarrollo de servicios web, pruebas funcionales y control de versiones.

| Tecnología | Descripción |
|---|---|
| Python | Lenguaje de programación utilizado para el desarrollo de la API REST |
| Flask | Framework utilizado para la creación de la aplicación web y la gestión de solicitudes HTTP |
| Flask-RESTful | Extensión de Flask utilizada para facilitar la implementación de servicios REST y endpoints |
| JSON | Formato utilizado para el intercambio de información entre la API y el cliente |
| Postman | Herramienta utilizada para realizar pruebas funcionales de los endpoints de la API |
| GitHub | Plataforma utilizada para el control de versiones y almacenamiento del proyecto |
| Visual Studio Code | Entorno de desarrollo utilizado para la implementación y edición del código fuente |

### Verificación de Python

Para verificar que Python se encuentra instalado correctamente en el sistema se debe ejecutar el siguiente comando en la terminal:

```bash
python --version
```

Si la instalación fue realizada correctamente, la terminal mostrará la versión actual de Python instalada en el equipo.

### Descarga del proyecto

El proyecto puede descargarse o clonarse desde el repositorio de GitHub correspondiente y posteriormente abrirse en Visual Studio Code.

### Instalación de dependencias

Una vez abierto el proyecto se debe ejecutar el siguiente comando en la terminal para instalar las librerías necesarias para el funcionamiento de la API:

```bash
pip install -r requirements.txt
```

### Dependencias utilizadas

El archivo `requirements.txt` contiene las siguientes dependencias:

- `flask`
- `Flask-restful`

---

# Ejecución de la API

---

Una vez instaladas las dependencias necesarias del proyecto, la API REST puede ejecutarse desde la terminal utilizando Python.

### Ejecución del servidor

Para iniciar la aplicación se debe ejecutar el siguiente comando dentro de la carpeta principal del proyecto:

```bash
python app.py
```

Si la ejecución se realiza correctamente, Flask iniciará el servidor local y mostrará una dirección similar a la siguiente:

```
http://127.0.0.1:5000
```

### Modo de ejecución

La API se ejecuta en modo de desarrollo mediante la instrucción:

```python
app.run(debug=True)
```

El modo debug permite visualizar errores durante la ejecución y actualizar automáticamente los cambios realizados en el código fuente.

### Verificación de funcionamiento

Una vez iniciada la aplicación, los endpoints de la API pueden probarse mediante Postman o desde el navegador utilizando la dirección local generada por Flask.

### Flujo de uso de la API

La API Coquito Amarillo está diseñada para gestionar el ciclo básico de compra mediante la administración de clientes, productos y pedidos. El flujo de trabajo recomendado consiste en registrar primero la información necesaria para posteriormente crear y gestionar los pedidos asociados.

- **Registro de clientes:** Antes de realizar cualquier pedido, es necesario crear un cliente mediante el endpoint correspondiente. Una vez registrado, el sistema asignará automáticamente un identificador único que podrá utilizarse en futuras operaciones.
- **Registro de productos:** Los productos disponibles deben registrarse previamente indicando información como nombre, precio, categoría, descripción, stock y costo de envío. Cada producto recibe un identificador único que permitirá asociarlo posteriormente a los pedidos.
- **Creación de pedidos:** Para generar un pedido es necesario proporcionar un cliente existente y una lista de productos válidos. El sistema verificará la existencia de los recursos involucrados antes de registrar la solicitud.
- **Consulta y actualización:** Una vez creado un pedido, puede consultarse mediante su identificador para verificar su información actual; también es posible actualizar determinados datos, como la dirección de entrega o el estado del pedido.
- **Eliminación de recursos:** La API permite eliminar clientes, productos y pedidos cuando sea necesario mediante los endpoints de eliminación correspondientes.

---

# Endpoints de la API

---

La API REST implementa diferentes endpoints para la gestión de clientes, productos y pedidos mediante las operaciones HTTP. Las respuestas son generadas en formato JSON y utilizan códigos de estado HTTP para indicar el resultado de cada solicitud.

## Endpoint principal

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `GET` | `/` | Muestra el mensaje principal de la API REST |

**Respuesta:**
```json
{
  "message": "Bienvenido a Coquito Amarillo API"
}
```

---

## Gestión de clientes

La gestión de clientes permite realizar operaciones de consulta, registro, actualización y eliminación de información relacionada con los usuarios registrados en la plataforma.

&nbsp;

### Obtener todos los clientes

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `GET` | `/clientes` | Obtiene la lista completa de clientes registrados |

**Respuesta:**
```json
{
  "clientes": []
}
```

&nbsp;

### Obtener cliente por ID

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `GET` | `/clientes/<id_cliente>` | Obtiene la información de un cliente específico mediante su identificador |

**Respuesta exitosa:**
```json
{
  "id_cliente": 1,
  "nombre": "Juan Perez",
  "correo": "juan@gmail.com",
  "numero_telefono": "3001234567",
  "fecha_registro": "2026-05-28"
}
```

**Respuesta de error:**
```json
{
  "error": "Cliente con id '1' no encontrado"
}
```

&nbsp;

### Registrar cliente

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `POST` | `/clientes` | Registra un nuevo cliente dentro de la plataforma |

**Body de la solicitud:**
```json
{
  "nombre": "Juan Perez",
  "correo": "juan@gmail.com",
  "contrasena_hash": "123456",
  "numero_telefono": "3001234567"
}
```

**Respuesta exitosa:**
```json
{
  "id_cliente": 1,
  "nombre": "Juan Perez",
  "correo": "juan@gmail.com",
  "numero_telefono": "3001234567"
}
```

&nbsp;

### Actualizar cliente

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `PUT` | `/clientes/<id_cliente>` | Actualiza la información de un cliente existente |

**Body de la solicitud:**
```json
{
  "nombre": "Juan Actualizado",
  "correo": "nuevo_correo@gmail.com"
}
```

**Respuesta exitosa:**
```json
{
  "id_cliente": 1,
  "nombre": "Juan Actualizado",
  "correo": "nuevo_correo@gmail.com"
}
```

**Respuesta de error:**
```json
{
  "error": "Cliente con id '1' no encontrado"
}
```

&nbsp;

### Eliminar cliente

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `DELETE` | `/clientes/<id_cliente>` | Elimina un cliente registrado mediante su identificador |

**Respuesta exitosa:**
```json
{
  "mensaje": "El cliente con el id '1' fue eliminado exitosamente"
}
```

**Respuesta de error:**
```json
{
  "error": "Cliente con id '1' no encontrado"
}
```

---

## Gestión de productos

La gestión de productos permite administrar la información de las artesanías registradas dentro de la plataforma.

&nbsp;

### Obtener todos los productos

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `GET` | `/productos` | Obtiene la lista completa de productos registrados |

**Respuesta:**
```json
{
  "productos": []
}
```

&nbsp;

### Obtener producto por ID

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `GET` | `/productos/<id_producto>` | Obtiene la información de un producto mediante su identificador |

**Respuesta exitosa:**
```json
{
  "id_producto": 1,
  "nombre": "Mochila Wayuu",
  "precio": 120000,
  "stock": 10,
  "categoria": "Artesanías"
}
```

**Respuesta de error:**
```json
{
  "error": "Producto con id '1' no encontrado"
}
```

&nbsp;

### Registrar producto

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `POST` | `/productos` | Registra un nuevo producto |

**Body de la solicitud:**
```json
{
  "nombre": "Mochila Wayuu",
  "precio": 120000,
  "stock": 10,
  "descripcion": "Artesanía tradicional",
  "categoria": "Artesanías",
  "precio_envio": 15000
}
```

**Respuesta exitosa:**
```json
{
  "id_producto": 1,
  "nombre": "Mochila Wayuu",
  "precio": 120000
}
```

&nbsp;

### Actualizar producto

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `PUT` | `/productos/<id_producto>` | Actualiza la información de un producto ya existente |

**Body de la solicitud:**
```json
{
  "stock": 5,
  "precio": 100000
}
```

**Respuesta exitosa:**
```json
{
  "id_producto": 1,
  "stock": 5,
  "precio": 100000
}
```

&nbsp;

### Eliminar producto

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `DELETE` | `/productos/<id_producto>` | Elimina un producto mediante su identificador |

**Respuesta exitosa:**
```json
{
  "mensaje": "El producto con el id '1' fue eliminado exitosamente"
}
```

---

## Gestión de pedidos

La gestión de pedidos permite registrar y administrar pedidos realizados por los clientes.

&nbsp;

### Obtener todos los pedidos

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `GET` | `/pedidos` | Obtiene una lista de todos los pedidos existentes |

**Respuesta:**
```json
{
  "pedidos": []
}
```

&nbsp;

### Obtener pedido por ID

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `GET` | `/pedidos/<id_pedido>` | Obtiene la información de un pedido específico mediante su identificador |

**Respuesta exitosa:**
```json
{
  "id_pedido": 1,
  "total": 135000,
  "direccion_entrega": "Medellín"
}
```

&nbsp;

### Registrar pedido

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `POST` | `/pedidos` | Registra un pedido nuevo |

**Body de la solicitud:**
```json
{
  "id_cliente": 1,
  "items": [
    {
      "id_producto": 1,
      "cantidad": 1
    }
  ],
  "total": 135000,
  "direccion_entrega": "Medellín"
}
```

**Respuesta exitosa:**
```json
{
  "id_pedido": 1,
  "total": 135000,
  "direccion_entrega": "Medellín"
}
```

**Respuesta de error:**
```json
{
  "error": "Cliente no encontrado"
}
```

&nbsp;

### Actualizar pedido

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `PUT` | `/pedidos/<id_pedido>` | Actualiza la información de un pedido existente mediante el identificador |

**Body de la solicitud:**
```json
{
  "estado": "Enviado"
}
```

**Respuesta exitosa:**
```json
{
  "id_pedido": 1,
  "estado": "Enviado"
}
```

&nbsp;

### Eliminar pedido

| Método | Endpoint | Descripción |
|:---:|:---|:---|
| `DELETE` | `/pedidos/<id_pedido>` | Elimina un pedido existente mediante su identificador |

**Respuesta exitosa:**
```json
{
  "mensaje": "El pedido con el id '1' fue eliminado exitosamente"
}
```

---

# Métodos HTTP utilizados

---

La API REST utiliza diferentes métodos HTTP para realizar operaciones relacionadas con la consulta y gestión de información dentro del sistema.

| Método HTTP | Descripción |
|:---:|:---|
| `GET` | Obtiene la información almacenada en la API, como clientes, productos y pedidos |
| `POST` | Registra nueva información dentro del sistema |
| `PUT` | Actualiza información existente mediante un identificador específico |
| `DELETE` | Elimina información registrada dentro de la API |

---

# Códigos de estado HTTP

---

La API REST utiliza códigos de estado HTTP para indicar el resultado de cada solicitud realizada por el cliente. Estos códigos permiten identificar si una operación fue ejecutada correctamente o si ocurrió algún error durante el proceso.

| Código HTTP | Descripción |
|:---:|:---|
| `200 OK` | La solicitud fue procesada correctamente |
| `201 Created` | El recurso fue creado exitosamente dentro del sistema |
| `400 Bad Request` | La solicitud contiene datos inválidos o incompletos |
| `404 Not Found` | El recurso solicitado no fue encontrado |

---

# Validaciones implementadas

---

| Validación | Implementación |
|:---|:---|
| Campos obligatorios | Verificación de datos requeridos en solicitudes POST |
| IDs existentes | Validación de clientes, productos y pedidos registrados |
| Estados permitidos | Control de estados válidos en pedidos |
| Recursos inexistentes | Retorno de errores cuando un recurso no existe |
| Actualización de datos | Verificación previa antes de modificar información |

---

# Manejo de errores

---

La API implementa un sistema básico de validación para garantizar que las solicitudes recibidas contengan la información necesaria y que los recursos solicitados existan dentro del sistema. Cuando ocurre algún problema durante el procesamiento de una solicitud, se devuelve un código de estado HTTP acompañado de un mensaje descriptivo en formato JSON.

### Formato de respuesta

Las respuestas de error utilizan la siguiente estructura:

```json
{
  "error": "Descripción del error"
}
```

&nbsp;

### Error 400 — Solicitud incorrecta

Este error se genera cuando la petición enviada por el cliente no contiene la información requerida o presenta datos inválidos.

**Ejemplos:**

```json
{ "error": "Campo requerido: 'nombre'" }
```
```json
{ "error": "Se requiere el ID del cliente para realizar cambios" }
```
```json
{ "error": "Estado inválido. Opciones: ['pendiente', 'en_proceso', 'enviado', 'entregado']" }
```

&nbsp;

### Error 404 — Recurso no encontrado

Este error ocurre cuando el recurso solicitado no existe dentro del sistema.

**Ejemplos:**

```json
{ "error": "Cliente con id '5' no encontrado" }
```
```json
{ "error": "Producto con id '10' no encontrado" }
```
```json
{ "error": "Pedido con id '3' no encontrado" }
```

También se devuelve este código cuando se intenta crear un pedido asociado a un cliente inexistente o cuando alguno de los productos incluidos en el pedido no se encuentra registrado.

---

# Consideraciones de uso

---

Para garantizar el correcto funcionamiento de las operaciones disponibles, es importante tener en cuenta las siguientes reglas:

- Los identificadores de clientes, productos y pedidos son generados automáticamente por el sistema.
- Todas las solicitudes que envían información deben utilizar formato JSON.
- Los campos obligatorios deben incluirse en la solicitud para que esta pueda procesarse correctamente.
- Un pedido únicamente puede asociarse a un cliente previamente registrado.
- Los productos incluidos en un pedido deben existir dentro del catálogo de productos.
- El estado de un pedido solo puede actualizarse utilizando los valores permitidos por el sistema.
- Las respuestas de la API utilizan códigos de estado HTTP para indicar el resultado de cada operación.
- Los mensajes de error proporcionan información descriptiva que facilita la identificación de problemas durante la integración.

---

# Conclusión

---

La API Coquito Amarillo proporciona una interfaz REST orientada a la gestión de clientes, productos y pedidos dentro de una plataforma de comercio electrónico. Mediante una estructura de endpoints organizada y respuestas en formato JSON, permite realizar operaciones de consulta, creación, actualización y eliminación de recursos de manera consistente.

La documentación presentada describe los recursos disponibles, los métodos soportados, los formatos de intercambio de información y el manejo de errores implementado por el sistema. Esto facilita la integración con aplicaciones externas y proporciona una referencia clara para desarrolladores que necesiten consumir los servicios ofrecidos por la API.
