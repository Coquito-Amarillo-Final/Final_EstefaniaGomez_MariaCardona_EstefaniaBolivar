# Manual técnico del sistema

Este manual técnico tiene como objetivo servir como guía para las personas encargadas del desarrollo y mantenimiento del sistema de Coquito Amarillo S.A.S.

El proyecto consiste en una API REST creada para ayudar a la empresa a organizar mejor la información relacionada con clientes, productos y pedidos. Por medio de este sistema, la empresa podrá registrar clientes, administrar los productos disponibles y llevar control de los pedidos realizados de una forma más rápida y ordenada. Además, el sistema busca mejorar la gestión de la información dentro de la empresa, evitando pérdidas de datos y facilitando el manejo de los procesos principales relacionados con la venta de artesanías.

## Requerimientos del entorno: 

Para que el sistema funcione correctamente, es necesario mencionar con algunas herramientas básicas de desarrollo.

### Lenguaje de programación 

El proyecto fue desarrollado en Python, ya que es un lenguaje fácil de utilizar y muy utilizado en el desarrollo de aplicaciones backend.

## Herramientas utilizadas

Para la construcción de la API se utilizaron las siguientes herramientas:

### Flask

framework utilizado para crear la aplicación.

### Flask-RESTful

librería que facilita la creación de endpoints y servicios REST.

### Entorno de desarrollo

El sistema puede ejecutarse tanto en Visual Studio Code como en GitHub Codespaces, permitiendo trabajar de forma local o en la nube.

### Herramientas de prueba

Para probar el funcionamiento de la API se recomienda usar Postman, ya que permite enviar solicitudes HTTP y verificar las respuestas del sistema en formato JSON.

## Guía de instalación y configuración

Para ejecutar correctamente el proyecto se deben realizar los siguientes pasos:

### Descargar el proyecto

Primero se debe clonar el repositorio desde GitHub utilizando el siguiente comando: git clone URL_DEL_REPOSITORIO

### Ingresar a la carpeta del proyecto

Luego se debe entrar a la carpeta principal del proyecto: cd API_cs-main

### Instalar dependencias

Después se instalan las librerías necesarias con el comando: pip install flask flask-restful

### Ejecutar la API

Ejecutar el archivo principal del proyecto para iniciar el servidor.

## Arquitectura de endpoints (rutas de la API)

La API se encuentra organizada en tres módulos principales:

### Módulo de clientes

Permite registrar, consultar, actualizar y eliminar clientes dentro del sistema.

### Módulo de productos

Permite administrar los productos artesanales, incluyendo información como precio, descripción y stock disponible.

### Módulo de pedidos

Permite registrar pedidos asociados a clientes y productos, además de consultar y actualizar el estado de los pedidos.

## Los módulos funcionan mediante los métodos HTTP:

GET

POST

PUT

DELETE

## Protocolo de comunicación y seguridad

### Formato de datos

Toda la información enviada y recibida por la API utiliza formato JSON, lo que facilita la comunicación entre el cliente y el servidor.

### Códigos de estado HTTP

La API utiliza códigos HTTP para indicar el resultado de cada solicitud:

200: solicitud realizada correctamente.

201: recurso creado exitosamente.

400: error en la solicitud o datos incompletos.

404: recurso no encontrado.