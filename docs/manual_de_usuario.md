# Manual de usuario - API-REST Coquito Amarillo S.A.S.

---

## 1. Introducción
Este manual tiene como propósito describir cómo consumir de manera local la API REST desarrollada para Coquito Amarillo S.A.S. usando postman. La API permite crear, consultar, modificar y eliminar los datos de los clientes, productos y pedidos de la empresa.

Es **importante** recordar que los datos no se almacenan en una base de datos de información, por lo tanto al finalizar la ejecución del archivo los datos almacenados durante la prueba serán eliminados.

**La URL base es:** `http://localhost:5000`

---

## 2. Configuración de Postman
1. Abrir postman y crear una nueva solicitud con **New > HTTP Request**.
2. Seleccionar el método HTTP deseado (GET, POST, PUT, DELETE) en el menú desplegable.
3. Ingresar la URL del endpoint en el campo de dirección.
4. Para POST y PUT dirigirse a la pestaña **Body > raw > JSON**.
5. Hacer click en el botón **Send** para envíar la solicitud.

---

## 3. Gestión de clientes

### 3.1 Agregar un cliente nuevo - `POST /clientes`
Los clientes a ingresar deben tener los siguientes datos:

| Campo | Tipo | Requerido | Ejemplo |
|-------|------|-----------|---------|
| `nombre` | texto | Sí | Daniela Villarreal |
| `correo` | texto | Sí | dany.v@email.com |
| `contrasena_hash` | texto | Sí | abc123hash |
| `numero_telefono` | texto | Sí | 3001234567 |

En formato JSON:
```json
{
  "nombre": "Daniela Villarreal",
  "correo": "dany.v@email.com",
  "contrasena_hash": "abc123hash",
  "numero_telefono": "3001234567"
}