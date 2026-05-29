# Arquitectura del sistema

La arquitectura implementada en el proyecto es una arquitectura cliente-servidor basada en API REST. sta estructura permite que la interfaz de usuario en nuestro caso, Postman y la lógica de procesamiento, el servidor, trabajen de forma independiente, comunicándose a través de peticiones HTTP. La estructura del sistema está organizada en tres componentes que separan las responsabilidades del software:

---
## Organización de archivos del sistema

### 1. [app.py](api/app.py)

Este componente actúa como el controlador central. Utiliza el micro-framework Flask para gestionar las rutas de acceso, endpoints, recibir las solicitudes del cliente y procesar las operaciones de creación, consulta, actualización y eliminación de datos. Además, es el encargado de validar que la información recibida sea correcta antes de generar una respuesta oficial.

### 2. [models.py](api/models.py)

 En este archivo se define la estructura lógica de las entidades del negocio: Clientes, Productos y Pedidos. Cada modelo organiza los atributos de los objetos y contiene la lógica necesaria para transformar los datos internos del servidor a un formato JSON.


### 3. [requirements.txt](api/requirements.txt)

Es el registro técnico que garantiza la portabilidad del proyecto. En él se listan las librerías necesarias en este caso Flask y Flask-RESTful para que el sistema pueda ser desplegado y ejecutado en cualquier entorno de desarrollo.

---

## Flujo de Funcionamiento

 Cuando se realiza una acción desde el cliente, el servidor intercepta la petición, identifica el recurso solicitado y ejecuta la lógica correspondiente. Finalmente, el sistema devuelve un paquete de datos en formato JSON acompañado de un código de estado.