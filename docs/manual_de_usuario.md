# Manual de usuario - API-REST Coquito Amarillo S.A.S.
---
## 1. Introducción.
Este manual tiene como propósito describir cómo consumir de manera local la API REST desarrollada para Coquito Amarillo S.A.S. usando postman. La API permite crear, consultar, modificar y eliminar los datos de los clientes, productos y pedidos de la empresa.
Es **importante** recordar que los datos no se almacenan en una base de datos de información, por lo tanto al finalizar la ejecución del archivo los datos almacenados durante la prueba serán eliminados.
**La URL base es:** `http://localhost:5000`

---
## 2. Configuración de Postman.
1. Abrir postman y crear una nueva solicitud con **New > HTTP Request**.
2. Seleccionar el método HTTP deseado (GET, POST, PUT, DELETE) en el menú desplegable.
3. Ingresar la URL del endpoint en el campo de dirección.
4. Para POST y PUT dirigirse a la pestaña **Body > raw > JSON**.
5. Hacer click en el botón **Send** para envíar la solicitud.

---
## 3. Gestión de clientes.
### 3.1 Agregar un cliente nuevo - `POST /clientes`.
Los clientes a ingresar deben tener los siguientes datos:
| Campo | Tipo | Requerido | Ejemplo |
|-------|------|-----------|---------|
| `nombre` | texto | Sí | Daniela Villarreal |
| `correo` | texto | Sí | dany.v@email.com |
| `contrasena_hash` | texto | Sí | abc123hash |
| `numero_telefono` | texto | Sí | 3001234567 |


En formato JSON :
```json
{
  "nombre": "Daniela Villarreal",
  "correo": "dany.v@email.com",
  "contrasena_hash": "abc123hash",
  "numero_telefono": "3001234567"
}
```


**Respuesta exitosa:** `201 CREATED` con los datos del cliente, incluyendo el `id_cliente` y la `fecha_registro`.
**Respuesta fallida:** `400 BAD REQUEST` "error": "Campo requerido: '{campo}'".

### 3.2 Consultar todos los clientes - `GET /clientes`
No requiere body.
**Respuesta exitosa:** `200 OK` con la lista de todos los clientes.
### 3.3 Consultar a un cliente en específico - `GET /clientes/{id}`
Reemplazar `{id}` por el `id_cliente`.
**Ejemplo:** `GET /clientes/1`.
**Respuesta exitosa:** `200 OK` con los datos del cliente solicitado.
**Respuesta fallida:** `404 NOT FOUND` "error": "Cliente con id '{id}' no encontrado".
### 3.4  Modificar datos de un cliente - `PUT /clientes/{id}`
Se debe reemplazar `{id}` por el `id_cliente`.
Se deben enviar solo los cambios que se desean cambiar, los datos que permiten ser modificados son:

| Campo | Descripción |
|-------|-------------|
| `nombre` | Nuevo nombre del cliente |
| `correo` | Nuevo correo electrónico |
| `numero_telefono` | Nuevo número de teléfono |

**Respuesta exitosa:** `200 OK` con todos los datos del cliente pero con los datos modificados.
**Respuesta fallida:** 
* `404 NOT FOUND` "error": "Se requiere el ID del cliente para realizar cambios".
* `404 NOT FOUND` "error": "cliente con id {id} no encontrado".

### 3.5 Eliminar cliente - `DELETE /clientes/{id}`
Se debe reemplazar `{id}` por el `id_cliente`.
No requiere body.
**Respuesta exitosa:** `200 OK`"mensaje": "El cliente con el id '{id}' fue eliminado exitosamente".
**Respuesta fallida:** 
* `404 NOT FOUND` "error": "Se requiere el ID del cliente para eliminar"
* `404 NOT FOUND` "error": "cliente con id {id} no encontrado".
---
## 4. Gestión de productos.
### 4.1 Agregar un producto nuevo - `POST /clientes`.
Los productos creados deben tener los siguientes datos:
| Campo | Tipo | Requerido | Ejemplo |
|-------|------|-----------|---------|
| `nombre` | texto | Sí | Coquito  |
| `precio` | número | Sí | 18000 |
| `stock` | número entero | Sí | 50 |
| `descripcion` | texto | Sí | Collar de Coquito |
| `categoria` | texto | Sí | Accesorios |
| `precio_envio` | número | Sí | 3000 |


En  formato JSON:

```json
{
  "nombre": "Coquito",
  "precio": 18000,
  "stock": 50,
  "descripcion": "Collar de Coquito",
  "categoria": "Accesorios",
  "precio_envio": 3000
}
```


**Respuesta exitosa:** `201 CREATED` con los datos del producto, incluyendo el `id_producto`.
**Respuesta fallida:** `400 BAD REQUEST` "error": "Campo requerido: '{campo}'".
### 4.2 Consultar todos los productos - `GET /productos`
No requiere body.
**Respuesta exitosa:** `200 OK` con la lista de todos los productos.
### 4.3 Consultar un producto en específico - `GET /productos/{id}`
Reemplazar `{id}` por el `id_producto`.
**Ejemplo:** `GET /productos/1`.
**Respuesta exitosa:** `200 OK` con los datos del producto solicitado.
**Respuesta fallida:** `404 NOT FOUND` "error": "Producto con id '{id}' no encontrado".
### 4.4  Modificar datos de un producto - `PUT /productos/{id}`
Se debe reemplazar `{id}` por el `id_producto`.
El único dato que no puede ser modificado es el `id_producto`

**Respuesta exitosa:** `200 OK` con todos los datos del producto pero con los datos modificados.
**Respuesta fallida:** 
* `404 NOT FOUND` "error": "Se requiere el ID del producto para realizar cambios".
* `404 NOT FOUND` "error": "producto con id {id} no encontrado".
### 4.5 Eliminar producto - `DELETE /productos/{id}`
Se debe reemplazar `{id}` por el `id_producto`.
No requiere body.
**Respuesta exitosa:** `200 OK`"mensaje": "El producto con el id '{id}' fue eliminado exitosamente".
**Respuesta fallida:** 
* `404 NOT FOUND` "error": "Se requiere el ID del producto para eliminar".
* `404 NOT FOUND` "error": "producto con id {id} no encontrado".
---
## 5. Gestión de pedidos.
### 5.1 Agregar un pedido nuevo - `POST /pedidos`.
Hay que tener en cuenta que tanto el cliente y productos asociados deben de existir.
Los productos creados deben tener los siguientes datos:
| Campo | Tipo | Requerido | Ejemplo |
|-------|------|-----------|-------------|
| `id_cliente` | número entero | Sí | 1 |
| `items` | lista | Sí | 1, Coquito, 2, 18000 |
| `total` | número | Sí | 36000 |
| `direccion_entrega` | texto | Sí | Calle 50 #30-20, Medellín|


En  formato JSON:
```json
{
  "id_cliente": 1,
  "items": [
    {"id_producto": 1, "nombre": "Coquito", "cantidad": 2, "precio": 18000}
  ],
  "total": 36000,
  "direccion_entrega": "Calle 50 #30-20, Medellín"
}
```


**Respuesta exitosa:** `201 CREATED` con los datos del pedido, incluyendo el `id_producto`, la `fecha_producto` y el `estado_producto` .

**Respuesta fallida:** 
* `400 BAD REQUEST` "error": "Campo requerido: '{campo}'".
* `404 NOT FOUND` "error": "Cliente no encontrado".
*  `404 NOT FOUND` "error": "Producto con id '{id}' no encontrado".
### 5.2 Consultar todos los pedidos - `GET /pedidos`
No requiere body.
**Respuesta exitosa:** `200 OK` con la lista de todos los pedidos.
### 5.3 Consultar un pedido en específico - `GET /pedidos/{id}`
Reemplazar `{id}` por el `id_pedido`.
**Ejemplo:** `GET /pedidos/1`.
**Respuesta exitosa:** `200 OK` con los datos del producto solicitado.
**Respuesta fallida:** `404 NOT FOUND` "error": "Pedido con id '{id}' no encontrado".
### 5.4  Modificar datos de un pedido - `PUT /productos/{id}`
Se debe reemplazar `{id}` por el `id_producto`.
Los datos que pueden ser modificados son:
| Campo | Descripción |
|-------|-------------|
| `estado` | Nuevo estado del cliente |
| `direccion_entrega` | Nueva dirección de entrega |


Solo hay cinco estados validos:


| Estado | Descripción |
|--------|-------------|
| `pendiente` | Pedido recién creado, en espera de pago |
| `pagado` | Pago confirmado |
| `en_preparacion` | El pedido está siendo preparado |
| `enviado` | El pedido fue despachado |
| `entregado` | El cliente recibió el pedido |
| `cancelado` | El pedido fue cancelado |



**Respuesta exitosa:** `200 OK` con todos los datos del producto pero con los datos modificados.
**Respuesta fallida:** 
* `404 NOT FOUND` "error": "Se requiere el ID del pedido para realizar cambios".
* `404 NOT FOUND` "error": "pedido con id {id} no encontrado".
* `400 BAD REQUEST` "error": "Estado inválido. Opciones: ['pendiente', 'pagado', 'en_preparacion', 'enviado', 'entregado', 'cancelado']"
### 5.5 Eliminar pedido - `DELETE /pedidos/{id}`
Se debe reemplazar `{id}` por el `id_pedido`.
No requiere body.
**Respuesta exitosa:** `200 OK`"mensaje": "El pedido con el id '{id}' fue eliminado exitosamente".
**Respuesta fallida:** 
* `404 NOT FOUND` "error": ""error": "Se requiere el ID del pedido para eliminar"".
* `404 NOT FOUND` "error": "pedido con id {id} no encontrado".
---
## 6. Códigos de respuesta HTTP
| Código | Significado | Qué hacer |
|--------|-------------|-----------|
| `200 OK` | Operación exitosa | Verificar los datos en la respuesta |
| `201 Created` | Registro creado | Guardar el id retornado para futuras consultas |
| `400 Bad Request` | Datos incorrectos o faltantes | Revisar que todos los campos requeridos estén presentes |
| `404 Not Found` | El recurso no existe | Verificar que el id sea correcto |
| `500 Internal Server Error` | Error en el servidor | Revisar que el servidor esté corriendo |