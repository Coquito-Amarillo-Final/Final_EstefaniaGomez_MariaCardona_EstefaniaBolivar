# Historias de usuario API REST Coquito Amarillo.

El presente documento contiene las historias de usuario definidas para el desarrollo de la API REST de Coquito Amarillo S.A.S. 

Las historias de usuario serán redactadas utilizando la siguiente estructura:

`Como:` El tipo de usuario.

`Quiero:` funcionalidad.

`Para:` beneficio.

---

## Tabla de resumen:

| Código | Nombre | 
|--------|-------------|
| HU01 | Crear cliente. |
| HU02 | Consultar clientes. | 
| HU03 | Modificar datos de un cliente. | 
| HU04 | Eliminar cliente. | 
| HU05 | Crear producto. | 
| HU06 | Consultar productos. | 
| HU07 | Modificar datos de un producto. | 
| HU08 | Eliminar producto. | 
| HU09 | Crear pedido. | 
| HU10 | Consultar pedidos. | 
| HU11 | Modificar datos de un pedido. | 
| HU12 | Eliminar pedido. | 

## Historias de usuario:

### HU01 - Crear cliente.

`Como` administrador de la tienda.

`Quiero` registrar un nuevo cliente en el sistema.

`Para` poder gestionar sus pedidos y sus datos de contacto.

### Criterios de aceptación:

* El sistema debe permitir registrar clientes.
* El cliente debe tener nombre, correo y número de teléfono.
* El sistema debe generar automaticamente un id único para cada cliente.
* El sistema debe guardar automaticamente la fecha de registro del cliente.
* El sistema debe dejar activo al cliente por defecto apenas se registra.
* Si falta algún campo requerido, el sistema debe retornar error `400`.

---
### HU02 - Consultar cliente.

`Como` administrador de la tienda.

`Quiero` consultar la lista de clientes registrados en el sistema.

`Para` visualizar la información de los clientes almacenada.

### Criterios de aceptación:

* El sistema debe listar todos los clientes registrados.
* El cliente debe permitir consultar un cliente específico mediante su id.
* Si el id no existe el sistema debe retornar error `404`.

---
### HU03 - Modificar datos de un cliente.

`Como` administrador de la tienda.

`Quiero` modificar los datos de un cliente registrado en el sistema.

`Para` mantener la información de los clientes actualizada.

### Criterios de aceptación:

* El sistema debe permitir que se modifique el nombre, el correo, el teléfono y el estado del cliente.
* El sistema solo debe modificar los datos envíados, los demás deben quedar igual.
* El sistema debe retornar los datos del cliente actualizados.
* Si no se ingresa el id del cliente, el sistema debe retornar error `400`.
* Si el cliente no existe el sistema debe retornar error `404`.

---
### HU04 - Eliminar cliente.

`Como` administrador de la tienda.

`Quiero` eliminar a un cliente registrado en el sistema.

`Para` eliminar información que ya no sea necesaria.

### Criterios de aceptación:

* El sistema debe permitir eliminar clientes por id.
* El sistema debe confirmar la eliminación del cliente con un mensaje.
* Si no se ingresa el id del cliente, el sistema debe retornar error `400`.
* Si el cliente no existe el sistema debe retornar error `404`.

---
### HU05 - Crear producto.

`Como` administrador de la tienda.

`Quiero` registrar un nuevo producto en el sistema.

`Para` que el producto este disponible para los pedidos.

### Criterios de aceptación:

* El sistema debe permitir crear productos.
* El producto debe incluir nombre, precio, stock, descripcion, categoría y precio de envio.
* El sistema debe asignar un id unico automaticamente.
* Si falta algún campo requerido, el sistema debe retornar error `400`.

---
### HU06 - Consultar productos.

`Como` administrador de la tienda.

`Quiero` consultar el catálogo de productos.

`Para` visualizar el catálogo disponible.

### Criterios de aceptación:

* El sistema debe retornar todos los productos con sus datos.
* El sistema debe permitir que se consulte solo un producto por medio de su id.
* Si el id no existe, el sistema debe retornar error `404`.

---
### HU07 - Modificar datos de un producto.

`Como` administrador de la tienda.

`Quiero` modificar los datos de un producto.

`Para` mantener actualizado el catálogo.

### Criterios de aceptación:

* El sistema debe poder permitir la actualización de los datos del producto.
* El sistema no debe permitir que se modifiqué el id del producto.
* El sistema solo debe modificar los datos enviados.
* El sistema debe retornar los datos del producto actualizados.
* Si no se ingresa el id del producto, el sistema debe retornar error `400`.
* Si el id no existe, el sistema debe retornar error `404`.

---
### HU08 - Eliminar producto.

`Como` administrador de la tienda.

`Quiero` eliminar un producto.

`Para` retirar productos que ya no están disponibles.

### Criterios de aceptación:

* El sistema debe permitir eliminar productos por id.
* El sistema debe confirmar la eliminación del producto.
* Si el id no existe, el sistema debe retornar error `404`.

---
### HU09 - Crear pedido.

`Como` administrador de la tienda.

`Quiero` registrar un pedido.

`Para` gestionar las compras realizadas por los clientes.

### Criterios de aceptación:

* El pedido debe asociarse a un cliente existente.
* Todos los productos dentro del pedido deben existir en el sistema.
* El pedido debe incluir id de cliente, items, total y dirección de entrega.
* El sistema debe asignar un id unico automaticamente.
* El sistema debe crear el pedido con estado pendiente por defecto.
* Si no se ingresa el id del producto, el sistema debe retornar error `400`.
* Si el cliente asociado no existe, el sistema debe retornar error `404`.
* Si al menos uno de los productos asociados no existe, el sistema debe retornar error `404`.
* Si no se ingresan todos los campos, el sistema debe retornar error `400`.

---
### HU10 - Consultar pedidos.

`Como` administrador de la tienda.

`Quiero` visualizar los pedidos realizados por los clientes.

`Para` hacer seguimiento a las compras de los clientes.

### Criterios de aceptación:

* El sistema debe retornar todos los pedidos con sus datos completos.
* El sistema debe permitir que se consulte un pedido por medio de su id.
* El pedido debe incluir id de cliente, items, total y dirección de entrega.
* Si el id no existe, el sistema debe retornar error `404`.

---
### HU11 - Modificar datos de un pedido.

`Como` administrador de la tienda.

`Quiero` actualizar datos de un pedido hecho por el cliente.

`Para` realizar seguimiento sobre el proceso de entrega.

### Criterios de aceptación:

* El sistema debe permitir actualizar el estado del pedido y la dirección de entrega.
* El sistema debe permitir que se consulte un pedido por medio de su id.
* Si no se ingresa el id del pedido, el sistema debe retornar error `400`.
* Si se envia un estado invalido, el sistema debe retornar error `400`.
* Si el id no existe, el sistema debe retornar error `404`.

---
### HU12 - Eliminar pedido.

`Como` administrador de la tienda.

`Quiero` eliminar pedidos registrados.

`Para` eliminar pedidos que ya no sean necesarios.

### Criterios de aceptación:

* El sistema debe permitir eliminar pedidos por id.
* El sistema debe confirmar la eliminación del pedido.
* Si no se ingresa el id del pedido, el sistema debe retornar error `400`.
* Si el id no existe, el sistema debe retornar error `404`.
