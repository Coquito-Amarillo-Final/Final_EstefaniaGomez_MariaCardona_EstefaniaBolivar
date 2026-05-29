Contenido  
Introducción	2
Objetivo de la API	3
Instalación del proyecto	3
Ejecución de la API	5
Endpoints de la API	6
Métodos HTTP utilizados	13
Códigos de estado HTTP	13
Validaciones implementadas	14
Introducción
La presente documentación técnica describe el desarrollo e implementación de una API REST para la empresa Coquito Amarillo S.A.S., orientada a la gestión de clientes, productos y pedidos dentro de una plataforma virtual de artesanías.
La API fue desarrollada utilizando Python, Flask y Flask-RESTful, aplicando una arquitectura basada en servicios REST que permite la comunicación mediante solicitudes HTTP y respuestas en formato JSON. El sistema implementa operaciones CRUD para la administración de información relacionada con clientes, productos y pedidos, incluyendo validaciones de datos, manejo de errores y códigos de estado HTTP.
El proyecto tiene como propósito fortalecer el proceso de gestión de información dentro de la plataforma, permitiendo realizar operaciones de consulta, registro, actualización y eliminación de datos de manera estructurada y organizada.
Adicionalmente, la documentación presenta la estructura general del proyecto, los endpoints implementados, los métodos HTTP utilizados, las validaciones realizadas y las pruebas ejecutadas mediante Postman para verificar el correcto funcionamiento de la API REST desarrollada.
Objetivo de la API
La API REST de Coquito Amarillo S.A.S tiene como objetivo permitir la gestión de clientes, productos y pedidos mediante operaciones de consulta, registro, actualización y eliminación de la información a través de servicios web basados en arquitectura REST.
La API utiliza Flask y Flask-RESTful para procesar solicitudes HTTP y generar respuestas en formato JSON, facilitando el intercambio organizado de la información dentro de la plataforma virtual de artesanías.
La API implementa validaciones de datos, manejo de errores y códigos de estado HTTP con el propósito de garantizar un funcionamiento adecuado de los servicios disponibles.
Instalación del proyecto
Para realizar la instalación y ejecución de la API REST es necesario contar con un entorno de desarrollo configurado con Python y las dependencias utilizadas durante la implementación del proyecto.
Tecnologías usadas
La API REST fue desarrollada utilizando diferentes tecnologías y herramientas orientadas al desarrollo de servicios web, pruebas funcionales y control de versiones. Estas tecnologías permiten la implementación de endpoints REST, el intercambio de información en formato JSON y la ejecución de pruebas para verificar el correcto funcionamiento del sistema.
Tecnología	Descripción
Python	Lenguaje de programación utilizado para el desarrollo de la API REST
Flask	Framework utilizado para la creación de la aplicación web y la gestión de solicitudes HTTP
Flask-RESTful	Extensión de Flask utilizada para facilitar la implementación de servicios REST y endpoints
JSON	Formato utilizado para el intercambio de información entre la API y el cliente
Postman	Herramienta utilizada para realizar pruebas funcionales de los endpoints de la API
GitHub	Plataforma utilizada para el control de versiones y almacenamiento del proyecto
Visual Studio Code	Entorno de desarrollo utilizado para la implementación y edición del código fuente
Verificación de Python
Para verificar que Python se encuentra instalado correctamente en el sistema se debe ejecutar el siguiente comando en la terminal:
python –version
Si la instalación de este fue realizada correctamente, la terminal mostrara la versión actual de Python instalada en el equipo.
Descarga del proyecto
El proyecto puede descargarse o clonarse desde el repositorio de GitHub correspondiente y posteriormente abrirse en Visual Studio Code.
Instalacion de dependencias
Una vez abierto el proyecto se debe ejecutar el siguiente comando en la terminal para instalar las librerías necesarias para el funcionamiento de la API.
Pip install -r requirements.txt
Dependencias utilizadas
El archivo requirements.txt contiene las siguientes dependencias
flask
Flask-restful
Ejecución de la API
Una vez instalada las dependencias necesarias del proyecto, la API REST puede ejecutarse desde la terminal utilizando Python.
Ejecucion del servidor
Para iniciar la aplicación se debe ejecutar el siguiente comando dentro de la carpeta principal del proyecto.
Python app.py
Si la ejecución se realiza correctamente, Flask iniciara el servidor local y mostrara una dirección similar a la siguiente.
http://127.0.0.1:5000
Modo de ejecución
La API se ejecuta en modo de desarrollo mediante la instrucción.
app.run(debug=True)
El modo debug permite visualizar errores durante la ejecución y actualizar automáticamente los cambios realizados en el código fuente.
Verificación de funcionamiento
Una vez iniciada la aplicación, los endspoint de la API pueden probarse mediante postman o desde el navegador utilizando la dirección local generada por Flask.
Endpoints de la API
La API REST implementa diferentes Endpoints para la gestión de clientes, productos y perdidos mediante las operaciones de HTTP. Las respuestas son generadas en formatos JSON y utilizan códigos de estado HTTP para indicar el resultado de cada solicitud.
Endpoint principal
Método	Endpoint	Descripción
GET	/	Muestra el mensaje principal de la API REST
Respuesta: {           "message": "Bienvenido a Coquito Amarillo API"  }		
Gestión de clientes
La gestión de cluentes permite realizar operaciones de consulta, registro, actualización y eliminación de información relacionada con los usuarios registrados en la plataforma.
Obtener todos los clientes
Método	Endpoint	Descripción
GET	/clientes	Obtiene la lista completa de clientes registrados
Respuesta: {           "clientes": [] }		
Obtener clientes por ID
Método	Endpoint	Descripción
GET	/clientes/<id_cliente>	Obtiene la información de un cliente especifico mediante su identificador
Respuesta Exitosa: {      "id_cliente": 1,      "nombre": "Juan Perez",      "correo": "juan@gmail.com",      "numero_telefono": "3001234567",      "fecha_registro": "2026-05-28"  } Respuesta de error: {      "error": "Cliente con id '1' no encontrado"  }		
Registrar cliente
Método	Endpoint	Descripción
POST	/clientes	Registra un nuevo cliente dentro de la plataforma
Body de la solicitud: {      "nombre": "Juan Perez",      "correo": "juan@gmail.com",      "contrasena_hash": "123456",      "numero_telefono": "3001234567"} Respuesta de exitosa: {        "id_cliente": 1,       "nombre": "Juan Perez",       "correo": "juan@gmail.com",       "numero_telefono": "3001234567"  }		
Actualizar cliente
Método	Endpoint	Descripción
PUT	/clientes/<id_cliente>	Actualiza la información de un cliente existente
Body de la solicitud: {   "nombre": "Juan Actualizado",   "correo": "nuevo_correo@gmail.com" } Respuesta exitosa: {   "id_cliente": 1,   "nombre": "Juan Actualizado",   "correo": "nuevo_correo@gmail.com" } Respuesta de error: {   "error": "cliente con id '1' no encontrado" }		
Eliminar cliente
Método	Endpoint	Descripción
DELETE	/clientes/<id_cliente>	Elimina un cliente registrado mediante su identificador
Respuesta exitosa: {   "mensaje": "El cliente con el id '1' fue eliminado exitosamente" } Respuesta de error: {   "error": "cliente con id '1' no encontrado" }		
Gestión de productos
La gestión de productos permite administrar la información de las artesanías  registradas dentro de la plataforma.
Obtener todos los productos
Método	Endpoint	Descripción
GET	/productos	Obtiene la lista completa de productos registrados
Respuesta: {   "productos": [] }		
Obtener productos por ID
Método	Endpoint	Descripción
GET	/productos/<id_producto>	Obtiene la información de un producto mediante su identificador
Respuesta exitosa: {   "id_producto": 1,   "nombre": "Mochila Wayuu",   "precio": 120000,   "stock": 10,   "categoria": "Artesanías" } Respuesta de error: {   "error": "Producto con id '1' no encontrado" }		
Registrar producto
Método	Endpoint	Descripción
POST	/productos	Registra un nuevo producto
Body de la solicitud: {   "nombre": "Mochila Wayuu",   "precio": 120000,   "stock": 10,   "descripcion": "Artesanía tradicional",   "categoria": "Artesanías",   "precio_envio": 15000 } Respuesta exitosa: {   "id_producto": 1,   "nombre": "Mochila Wayuu",   "precio": 120000 }		
Actualizar producto
Método	Endpoint	Descripción
PUT	/productos/<id_producto>	Actualiza la información de un producto ya existente
Body de la solicitud: {   "stock": 5,   "precio": 100000 } Respuesta exitosa: {   "id_producto": 1,   "stock": 5,   "precio": 100000 }		
Eliminar producto
Método	Endpoint	Descripción
DELETE	/productos/<id_producto>	Elimina un producto mediante su identificador
Respuesta exitosa: {   "mensaje": "El producto con el id '1' fue eliminado exitosamente" }		
Gestión de pedidos
La gestión de pedidos permite registrar y administrar pedidos realizados por los clientes.
Obtener todos los pedidos
Método	Endpoint	Descripción
GET	/pedidos	Obtiene una lista de todos los pedidos existentes
{       "pedidos": []  }		
Obtener pedido por ID
Método	Endpoint	Descripción
GET	/pedidos/<id_pedido>	Obtiene la información de un pedido especifico mediante su identificador
Respuesta exitosa: {   "id_pedido": 1,   "total": 135000,   "direccion_entrega": "Medellín" }		
Registrar pedido
Método	Endpoint	Descripción
POST	/pedidos	Registra un pedido nuevo
Body de la solicitud: {   "id_cliente": 1,   "items": [     {       "id_producto": 1,       "cantidad": 1     }   ],   "total": 135000,   "direccion_entrega": "Medellín" } Respuesta exitosa: {   "id_pedido": 1,   "total": 135000,   "direccion_entrega": "Medellín" } Respuesta de error: {   "error": "Cliente no encontrado" }		
Actualizar pedido
Método	Endpoint	Descripción
PUT	/pedidos/<id_pedido>	Actualiza la información de un pedido existente mediante el identificador
Body de la solicitud: {   "estado": "Enviado" } Respuesta exitosa: {   "id_pedido": 1,   "estado": "Enviado" }		
Eliminar pedido
Método	Endpoint	Descripción
DELETE	/pedidos/<id_pedido>	Elimina un pedido existente mediante su identificador
Respuesta exitosa: {   "mensaje": "El pedido con el id '1' fue eliminado exitosamente" }		
Métodos HTTP utilizados
La API REST utilizo diferentes métodos HTTP para realizar operaciones relacionadas con la consulta y gestión de información dentro del sistema.
Método HTTP	Descripción
GET	Obtiene la información almacenada en la API, como clientes, productos y pedidos
POST	Registra nueva información dentro del sistema
PUT	Actualiza información existente mediante un identificador especifico
DELETE	Elimina información registrada dentro de la API
Códigos de estado HTTP
Código HTTP	Descripción
200 OK	La solicitud fue procesada correctamente
201 Created	El recurso fue creado exitosamente dentro del sistema
400 Bad Request	La solicitud contiene datos inválidos o completos
404 Not Found	El recurso solicitado no fue encontrado
La API REST utiliza códigos de estado HTTP para indicar el resultado de cada solicitud realizada por el cliente. Estos códigos permiten identificar si una operación fue ejecutada correctamente o si ocurrió algún error durante el proceso.
Validaciones implementadas
Validación	Implementación
Campos obligatorios	Verificación de datos requeridos en solicitudes POST
IDs existentes	Validación de clientes, productos y pedidos registrados
Estados permitidos	Control de estados validos en pedidos
Recursos inexistentes	Retorno de errores cuando un recurso no existe
Actualización de datos	Verificación previa antes de modificar información
