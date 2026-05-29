# Casos de uso

## Tabla de resumen de casos de uso

| Código | Código de Actor | Caso de uso | Descripción | Código de requerimiento asociado |
|--------|----------------|-------------|-------------|----------------------------------|
| CU01 | AC02 | Registrar clientes | Registrar un nuevo cliente en el sistema mediante solicitud a la API REST. | RF02 |
| CU02 | AC02 | Consultar clientes | Visualizar datos de los clientes almacenados en el sistema mediante solicitud a la API REST. | RF02 |
| CU03 | AC02 | Actualizar clientes | Modificar los datos de los clientes existentes en el sistema mediante solicitud a la API REST. | RF02 |
| CU04 | AC02 | Eliminar clientes | Eliminar los datos de los clientes existentes en el sistema mediante solicitud a la API REST. | RF02 |
| CU05 | AC02 | Registrar productos | Registrar nuevo producto en el sistema mediante solicitud a la API REST. | RF03 |
| CU06 | AC02 | Consultar productos | Visualizar datos de los productos almacenados en el sistema mediante solicitud a la API REST. | RF03 |
| CU07 | AC02 | Actualizar productos | Modificar los datos de los productos existentes en el sistema mediante solicitud a la API REST. | RF03 |
| CU08 | AC02 | Eliminar productos | Eliminar los datos de los productos existentes en el sistema mediante solicitud a la API REST. | RF03 |
| CU09 | AC02 | Registrar pedidos | Registrar un nuevo pedido en el sistema mediante solicitud a la API REST. | RF04 |
| CU10 | AC02 | Consultar pedidos | Visualizar datos de los pedidos almacenados en el sistema mediante solicitud a la API REST. | RF04 |
| CU11 | AC02 | Actualizar pedidos | Modificar los datos de los pedidos existentes en el sistema mediante solicitud a la API REST. | RF04 |
| CU12 | AC02 | Eliminar pedidos | Eliminar los datos de los pedidos existentes en el sistema mediante solicitud a la API REST. | RF04 |

---

## Especificación detallada de casos de uso

### Caso de uso CU01

- **Nombre:** Registrar clientes.
- **Código de actores:** AC02
- **Descripción:** Registrar un nuevo cliente en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF02

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API REST debe estar en ejecución.

**Flujo principal:**
1. El actor envía una solicitud POST con los datos del cliente nuevo.
2. La API valida la información enviada.
3. Los datos enviados son almacenados.
4. La API responde con una respuesta de éxito.

**Flujo alterno:**
1. El actor envía una solicitud POST con datos inválidos o con datos faltantes.
2. La API responde con un mensaje de error.

**Postcondiciones:**
1. El cliente queda registrado correctamente.

---

### Caso de uso CU02

- **Nombre:** Consultar clientes.
- **Código de actores:** AC02
- **Descripción:** Visualizar datos de los clientes almacenados en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF02

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. Deben existir clientes registrados.

**Flujo principal:**
1. El actor envía una solicitud GET.
2. La API busca los registros.
3. La API responde exitosamente y retorna los datos en formato JSON, en caso de que no haya ningún cliente registrado la API responde con una lista vacía.

**Postcondiciones:**
1. Los datos de los clientes pueden ser visualizada correctamente.

---

### Caso de uso CU03

- **Nombre:** Actualizar clientes.
- **Código de actores:** AC02
- **Descripción:** Modificar los datos de los clientes existentes en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF02

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. El cliente que se desea modificar debe existir.

**Flujo principal:**
1. El actor envía una solicitud PUT con los nuevos datos.
2. La API valida la información.
3. Se actualiza la información del cliente.
4. La API responde exitosamente.

**Flujo alterno:**
1. El actor envía una solicitud PUT para modificar datos de un cliente no existente.
2. No existe el cliente ingresado.
3. La API responde con un mensaje de error.

**Postcondiciones:**
1. Los datos del cliente son modificados.

---

### Caso de uso CU04

- **Nombre:** Eliminar clientes.
- **Código de actores:** AC03
- **Descripción:** Eliminar los datos de los clientes existentes en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF02

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. El cliente que se desea eliminar debe existir.

**Flujo principal:**
1. El actor envía una solicitud DELETE.
2. La API elimina al cliente seleccionado.
3. La API responde exitosamente.

**Flujo alterno:**
1. El actor envía una solicitud DELETE para eliminar a un cliente no existente.
2. No existe el cliente ingresado.
3. La API responde con un mensaje de error.

**Postcondiciones:**
1. El cliente es eliminado.

---

### Caso de uso CU05

- **Nombre:** Registrar productos.
- **Código de actores:** AC03
- **Descripción:** Registrar nuevo producto en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF03

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.

**Flujo principal:**
1. El actor envía una solicitud POST con los datos del producto nuevo.
2. La API valida la información enviada.
3. Los datos enviados son almacenados.
4. La API responde con una respuesta de éxito.

**Flujo alterno:**
1. El actor envía una solicitud POST con datos inválidos o con datos faltantes.
2. La API responde con un mensaje de error.

**Postcondiciones:**
1. El producto es registrado.

---

### Caso de uso CU06

- **Nombre:** Consultar productos.
- **Código de actores:** AC03
- **Descripción:** Visualizar datos de los pedidos almacenados en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF03

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. Deben existir productos registrados.

**Flujo principal:**
1. El actor envía una solicitud GET.
2. La API busca los registros.
3. La API responde exitosamente y retorna los datos en formato JSON, en caso de que no haya ningún producto registrado la API responde con una lista vacía.

**Postcondiciones:**
1. Los datos de los productos pueden ser visualizada correctamente.

---

### Caso de uso CU07

- **Nombre:** Actualizar productos.
- **Código de actores:** AC02
- **Descripción:** Modificar los datos de los productos existentes en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF03

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. El producto que se desea modificar debe existir.

**Flujo principal:**
1. El actor envía una solicitud PUT con los nuevos datos.
2. La API valida la información.
3. Se actualiza la información del producto.
4. La API responde exitosamente.

**Flujo alterno:**
1. El actor envía una solicitud PUT para modificar datos de un producto no existente.
2. No existe el producto ingresado.
3. La API responde con un mensaje de error.

**Postcondiciones:**
1. Los datos del producto son modificados.

---

### Caso de uso CU08

- **Nombre:** Eliminar productos.
- **Código de actores:** AC03
- **Descripción:** Eliminar los datos de los productos existentes en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF03

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. El producto que se desea eliminar debe existir.

**Flujo principal:**
1. El actor envía una solicitud DELETE.
2. La API elimina al producto seleccionado.
3. La API responde exitosamente.

**Flujo alterno:**
1. El actor envía una solicitud DELETE para eliminar a un producto no existente.
2. No existe el producto ingresado.
3. La API responde con un mensaje de error.

**Postcondiciones:**
1. El producto es eliminado.

---

### Caso de uso CU09

- **Nombre:** Registrar pedidos.
- **Código de actores:** AC03
- **Descripción:** Registrar nuevo pedido en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF04

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. Debe de existir al menos un cliente registrado.
4. El cliente que realiza el pedido debe de corresponder a un cliente existente.
5. Cada producto de la lista debe corresponder a un producto existente.

**Flujo principal:**
1. El actor envía una solicitud POST con los datos del pedido nuevo.
2. La API valida la información enviada.
3. Los datos enviados son almacenados.
4. La API responde con una respuesta de éxito.

**Flujo alterno:**
1. El actor envía una solicitud POST con datos inválidos o con datos faltantes.
2. La API responde con un mensaje de error.

**Postcondiciones:**
1. El pedido es registrado.

---

### Caso de uso CU10

- **Nombre:** Consultar pedidos.
- **Código de actores:** AC03
- **Descripción:** Visualizar datos de los pedidos almacenados en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF04

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. Deben existir pedidos registrados.

**Flujo principal:**
1. El actor envía una solicitud GET.
2. La API busca los registros.
3. La API responde exitosamente y retorna los datos en formato JSON, en caso de que no haya ningún pedido registrado la API responde con una lista vacía.

**Postcondiciones:**
1. Los datos de los pedidos pueden ser visualizada correctamente.

---

### Caso de uso CU11

- **Nombre:** Actualizar pedidos.
- **Código de actores:** AC02
- **Descripción:** Modificar los datos de los pedidos existentes en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF04

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. El pedido que se desea modificar debe existir.

**Flujo principal:**
1. El actor envía una solicitud PUT con los nuevos datos.
2. La API valida la información.
3. Se actualiza la información del pedido.
4. La API responde exitosamente.

**Flujo alterno:**
1. El actor envía una solicitud PUT para modificar datos de un pedido no existente.
2. No existe el producto ingresado.
3. La API responde con un mensaje de error.

**Postcondiciones:**
1. Los datos del pedido son modificados.

---

### Caso de uso CU12

- **Nombre:** Eliminar pedidos.
- **Código de actores:** AC03
- **Descripción:** Eliminar los datos de los pedidos existentes en el sistema mediante solicitud a la API REST.
- **Código de requerimiento asociado:** RF04

**Precondiciones:**
1. El actor tiene acceso activo a Postman o a la WebApp.
2. La API debe estar en ejecución.
3. El pedido que se desea eliminar debe existir.

**Flujo principal:**
1. El actor envía una solicitud DELETE.
2. La API elimina al pedido seleccionado.
3. La API responde exitosamente.

**Flujo alterno:**
1. El actor envía una solicitud DELETE para eliminar a un pedido no existente.
2. No existe el producto ingresado.
3. La API responde con un mensaje de error.

**Postcondiciones:**
1. El pedido es eliminado.
