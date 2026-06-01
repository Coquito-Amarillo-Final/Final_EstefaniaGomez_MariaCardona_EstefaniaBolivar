# Plan de aseguramiento de calidad
 
## Introducción
 
Plan de Aseguramiento de Calidad del Software para el proyecto de desarrollo de la API REST destinada a la empresa Coquito Amarillo S.A.S, la cual es una colombiana dedicada a la producción y comercialización de productos con presencia en Medellín, Bogotá y Cali.
 
El proyecto surge de la necesidad de la empresa de reemplazar sus procesos manuales por un sistema digital que le permita gestionar eficientemente la información de clientes, productos y pedidos, evitando pérdidas de datos, reduciendo tiempos de respuesta y mejorando la experiencia de sus clientes.
 
Este documento establece los lineamientos, actividades, responsabilidades y métricas que guiarán el aseguramiento de calidad durante todo el ciclo de vida del proyecto.
 
## Objetivo del plan de aseguramiento
 
Garantizar que la API REST desarrollada para Coquito Amarillo S.A.S. cumpla con los requerimientos funcionales y no funcionales definidos, entregando un producto confiable, bien documentado y verificado mediante pruebas sistemáticas, en conformidad con las normas ISO/IEC 25010 e IEEE 730.
 
## Alcance
 
Este plan aplica a todas las fases del proyecto: análisis, diseño, implementación y pruebas de la API REST. Cubre los siguientes módulos y actividades:
 
- Módulo de gestión de clientes: endpoints CRUD (/clientes).
- Módulo de gestión de productos: endpoints CRUD (/productos).
- Módulo de gestión de pedidos: endpoints CRUD (/pedidos).
- Validación de requerimientos funcionales RF01, RF02, RF03 y RF04.
- Verificación de requerimientos no funcionales RNF01 (entorno GitHub Codespaces), RNF02 (códigos HTTP) y RNF03 (formato JSON).
- Control de versiones mediante GitHub.
- Documentación técnica, manual de usuario y manual técnico.
Fuera del alcance: pasarelas de pago, facturación electrónica, interfaz gráfica e implementación de base de datos persistente.
 
## Normas y estándares de referencia
 
El plan se rige por las siguientes normas:
 
| **Norma** | **Área de aplicación** | **Uso en el proyecto** |
| --- | --- | --- |
| **ISO/IEC 25010** | Calidad del producto software | Evaluar fiabilidad, mantenibilidad, eficiencia y compatibilidad de la API REST; referencia para las características de calidad del sistema. |
| **IEEE 730** | Aseguramiento de calidad del software (SQA) | Guía para planear y documentar las actividades de QA: pruebas, verificación de requerimientos, revisiones de código y gestión de configuración. |
 
## Organización del equipo y responsabilidades
 
El equipo de desarrollo está conformado por tres integrantes que trabajan de forma colaborativa. Cada integrante tiene un rol principal que le permite ejercer un control riguroso sobre los entregables bajo su liderazgo:
 
| **Integrante** | **Rol principal** | **Responsabilidades clave** | **Apoya en** |
| --- | --- | --- | --- |
| **Estefania Bolivar Marín** | Desarrollo | Implementación de la API REST y revisión de RF | Pruebas, documentación, presentación oral |
| **Estefania Gomez Gallego** | Pruebas | Creación y ejecución de pruebas en Postman | Desarrollo, documentación, presentación oral |
| **Maria Jose Cardona Velasquez** | Documentación | Redacción de documentos técnicos y manuales | Desarrollo, pruebas, presentación oral |
 
## Actividades y aseguramiento de calidad
 
Las siguientes actividades serán ejecutadas de forma sistemática para garantizar la calidad del producto en todas las etapas del proyecto:
 
| **Actividad** | **Frecuencia** | **Herramienta / Evidencia** |
| --- | --- | --- |
| Revisión de requerimientos funcionales y no funcionales | Inicio del proyecto | Documento técnico |
| Pruebas funcionales de endpoints CRUD (clientes, productos, pedidos) | Por cada entrega | Postman – colección de pruebas |
| Validación de códigos de estado HTTP | Por cada endpoint | Postman – capturas de respuesta |
| Validación de formato JSON en peticiones y respuestas | Continua | Postman / Revisión manual de código |
| Revisión de validación de datos inválidos o incompletos | Por cada endpoint | Postman – casos de error |
| Revisión colaborativa del código fuente | Por cada commit | GitHub – pull requests |
| Control de versiones y registro de cambios | Continua | GitHub – historial de commits |
| Actualización de documentación técnica y de endpoints | Al finalizar cada módulo | Documento Word / Manual .md |
| Revisión final y aprobación del entregable | Al finalizar el proyecto | Lista de verificación final |
 
## Casos de prueba
 
Los casos de prueba cubren los tres módulos de la API (clientes, productos y pedidos), verificando tanto los flujos principales (respuestas exitosas) como los flujos alternos (manejo de errores). Todas las pruebas se ejecutan en Postman.
 
### Tabla de casos de prueba
 
| **Código** | **Caso de Prueba** | **Pasos** | **Resultado Esperado** | **Criterio de Aceptación** |
| --- | --- | --- | --- | --- |
| **CP01** | Crear cliente válido | POST /clientes con JSON completo (nombre, correo, contrasena_hash, numero_telefono) | 201 CREATED con datos del cliente e id generado | Respuesta 201 con id_cliente y fecha_registro |
| **CP02** | Crear cliente con campo faltante | POST /clientes sin el campo 'correo' | 400 BAD REQUEST con mensaje de error | Respuesta 400 indicando campo faltante |
| **CP03** | Consultar todos los clientes | GET /clientes | 200 OK con lista JSON de clientes | Lista con todos los clientes registrados |
| **CP04** | Consultar cliente por ID inexistente | GET /clientes/999 | 404 NOT FOUND | Mensaje de error indicando id no encontrado |
| **CP05** | Modificar cliente existente | PUT /clientes/1 con nuevo correo | 200 OK con datos actualizados | Solo el campo enviado cambia; los demás permanecen |
| **CP06** | Eliminar cliente existente | DELETE /clientes/1 | 200 OK con mensaje de confirmación | Mensaje de eliminación exitosa |
| **CP07** | Crear producto válido | POST /productos con JSON completo (nombre, precio, stock, descripcion, categoria, precio_envio) | 201 CREATED con datos del producto | Respuesta 201 con id_producto generado |
| **CP08** | Crear producto con campo faltante | POST /productos sin 'precio' | 400 BAD REQUEST | Mensaje indicando campo requerido faltante |
| **CP09** | Modificar producto con campo inválido | PUT /productos/1 con campo 'id_producto' | 400 BAD REQUEST | Error indicando campos no permitidos |
| **CP10** | Eliminar producto inexistente | DELETE /productos/999 | 404 NOT FOUND | Mensaje de error indicando id no encontrado |
| **CP11** | Crear pedido válido | POST /pedidos con id_cliente, items, total y direccion_entrega existentes | 201 CREATED con datos del pedido | Estado inicial 'pendiente', id y fecha generados |
| **CP12** | Crear pedido con cliente inexistente | POST /pedidos con id_cliente = 999 | 404 NOT FOUND | Error 'Cliente no encontrado' |
| **CP13** | Actualizar estado del pedido con valor inválido | PUT /pedidos/1 con estado 'entregando' | 400 BAD REQUEST | Error indicando estados válidos permitidos |
| **CP14** | Actualizar estado del pedido válido | PUT /pedidos/1 con estado 'enviado' | 200 OK con pedido actualizado | Estado cambia a 'enviado' |
| **CP15** | Eliminar pedido existente | DELETE /pedidos/1 | 200 OK con mensaje de confirmación | Pedido eliminado y mensaje exitoso |
 
## 8. métricas y criterios de aceptación
 
### Métricas del proyecto
 
| **Métrica** | **Descripción** | **Meta** | **Norma aplicada** |
| --- | --- | --- | --- |
| **Cobertura de endpoints** | Porcentaje de endpoints implementados vs. diseñados | 100% | ISO 25010 – Completitud funcional |
| **Éxito en pruebas Postman** | Porcentaje de rutas que responden con código HTTP correcto | 100% | IEEE 730 – Verificación funcional |
| **Respuestas en formato JSON** | Porcentaje de respuestas que retornan JSON válido | 100% | ISO 25010 – Compatibilidad |
| **Manejo correcto de errores HTTP** | Porcentaje de respuestas de error con código adecuado (400, 404, 500) | 100% | ISO 25010 – Fiabilidad |
| **Cobertura de requerimientos funcionales** | Número de RF completamente implementados y verificados | 4/4 | IEEE 730 – Trazabilidad |
| **Control de versiones** | Porcentaje del código gestionado en GitHub con commits por cada integrante | 100% | IEEE 730 – Gestión de configuración |
| **Documentación técnica** | Porcentaje de ítems documentados respecto a los requeridos | 100% | IEEE 730 – Documentación |
 
### Criterios de aceptación
 
| **Criterio de Aceptación** | **Resultado Esperado** |
| --- | --- |
| La API permite operaciones CRUD de clientes (CU01–CU04) | GET, POST, PUT y DELETE de /clientes responden correctamente en Postman. |
| La API permite operaciones CRUD de productos (CU05–CU08) | Los endpoints de /productos responden con códigos HTTP y JSON válidos. |
| La API permite operaciones CRUD de pedidos (CU09–CU12) | Los pedidos pueden registrarse, consultarse, actualizarse y eliminarse. |
| Respuestas exclusivamente en formato JSON (RNF03) | Todas las respuestas retornan JSON válido; ninguna respuesta llega en texto plano o HTML. |
| Códigos HTTP adecuados por tipo de operación (RNF02) | La API usa 200, 201, 400 y 404 en los escenarios correctos. |
| Validación de datos inválidos o incompletos | El sistema retorna 400 con mensajes de error cuando la información es inválida. |
| Proyecto gestionado mediante GitHub con commits por integrante | El repositorio tiene al menos un commit por cada integrante del equipo. |
| Documentación técnica y manuales completos | El documento incluye todos los apartados solicitados y los manuales están publicados. |
| Pruebas exitosas en entorno local (GitHub Codespaces) | La API se ejecuta sin errores críticos y todos los endpoints funcionan en el entorno local. |
 
## Matriz de riesgos
 
La siguiente matriz identifica los principales riesgos del proyecto, su probabilidad de ocurrencia, el impacto potencial y la estrategia de mitigación definida. El nivel de riesgo se calcula como Probabilidad × Impacto (escala 1–3).
 
| **Riesgo** | **Probabilidad** | **Impacto** | **Nivel** | **Estrategia de Mitigación** |
| --- | --- | --- | --- | --- |
| Caída del servidor / API REST | Alta (3) | Alta (3) | **9 - Crítico** | Usar entorno estable (GitHub Codespaces) y realizar monitoreo constante. |
| Pérdida de información (clientes, productos, pedidos) | Media (2) | Alta (3) | **6 - Alto** | Realizar copias de seguridad frecuentes y usar GitHub para respaldo del código. |
| Problemas de seguridad / acceso no autorizado | Media (2) | Alta (3) | **6 - Alto** | Implementar validaciones robustas y control de acceso en la API. |
| Errores en conexión entre WebApp y API | Alta (3) | Media (2) | **6 - Alto** | Realizar pruebas constantes de integración y usar Postman para verificar endpoints. |
| Fallos en validación de datos enviados | Media (2) | Alta (3) | **6 - Alto** | Implementar validaciones en todas las peticiones y ejecutar pruebas funcionales antes de entregar. |
| Errores en respuestas JSON de la API | Media (2) | Alta (3) | **6 - Alto** | Validar respuestas mediante pruebas en Postman y revisión de código. |
| Lentitud en respuestas de la API | Media (2) | Media (2) | **4 - Medio** | Realizar pruebas de rendimiento y optimizar la lógica de los endpoints. |
| Información incorrecta en productos o pedidos | Media (2) | Media (2) | **4 - Medio** | Validar los datos ingresados antes de almacenarlos; incluir pruebas de casos límite. |
| Fallos al consumir endpoints de la API | Media (2) | Media (2) | **4 - Medio** | Verificar el funcionamiento de las rutas mediante pruebas en Postman. |
| Usuarios con dificultad para consumir la API | Baja (1) | Media (2) | **2 - Bajo** | Documentar correctamente los endpoints y proveer ejemplos de uso en el manual. |
 
## Gestión de cambios
 
Todo cambio realizado durante el desarrollo de la API REST debe seguir el siguiente proceso:
 
- Identificar el cambio y el módulo afectado.
- Validar el cambio mediante pruebas en Postman antes de hacer el commit.
- Registrar el cambio en el repositorio GitHub con un mensaje descriptivo en el commit.
- Actualizar la documentación técnica o los manuales si el cambio afecta la interfaz o el comportamiento de la API.
- Informar al equipo de desarrollo para garantizar coherencia entre módulos.
## Herramientas técnicas
 
Las herramientas empleadas en el proyecto, tanto para el desarrollo como para las actividades de aseguramiento de calidad, son las siguientes:
 
| **Herramienta** | **Propósito en el proyecto** | **Uso en QA** |
| --- | --- | --- |
| **Python 3.x** | Lenguaje de programación principal | Base del código fuente a verificar |
| **Flask / Flask-RESTful** | Framework para la construcción de la API REST | Revisión de rutas, recursos y manejo de errores |
| **Postman** | Cliente HTTP para consumir endpoints | Ejecución de todos los casos de prueba funcionales |
| **GitHub / GitHub Codespaces** | Control de versiones y entorno de desarrollo en la nube | Trazabilidad de cambios y gestión de configuración |
| **Microsoft Word** | Procesador de texto para documentación | Redacción del documento técnico y del SQAP |
 
## Revisión y aprobación
 
Al finalizar el proyecto, cada integrante del equipo realizará una revisión formal de su área de responsabilidad antes de la aprobación final:
 
| **Actividad** | **Responsable** | **Resultado esperado** |
| --- | --- | --- |
| Revisión de requerimientos funcionales y cobertura de endpoints | Estefania Bolivar Marín | Verificar que los 12 endpoints implementados correspondan a los 4 RF definidos. |
| Revisión de pruebas funcionales en Postman | Estefania Gomez Gallego | Validar respuestas HTTP, códigos de estado y formato JSON de cada endpoint. |
| Revisión de la documentación técnica y manuales | Maria Jose Cardona Velasquez | Confirmar que el documento técnico, el manual de usuario y el manual técnico estén completos. |
| Aprobación final del proyecto | Equipo de trabajo (todas) | Validar la entrega final integrando código, documentación y evidencia de pruebas. |
