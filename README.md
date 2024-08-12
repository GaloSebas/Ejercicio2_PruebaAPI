# Ejercicio de Automaizacion API
## Autor: Galo Sanchez

### Descripcion del Ejercicio

    Ejercicio 2

    Prueba automatizada de API de un flujo de agregar y actualizar los datos de una mascota en el api https://petstore.swagger.io/ que incluye:

        1. Añadir una mascota a la tienda
        2. Consultar la mascota ingresada previamente (Búsqueda por ID)
        3. Actualizar el nombre de la mascota y el estatus de la mascota a “sold”
        4. Consultar la mascota modificada por estatus (Busqueda por estatus)

### Prerequisitos

- Asegurate de tener instalado lo siguiente:

    1. Sistema operativo Windows 11
    2. IDE IntelliJ IDEA (Community Edition) v2023.3.1
    3. Gradle versión 7.6.1 (debe estar en la variable de entorno)
    4. Apache maven 3.9.8 (debe estar en la variable de entorno)
    4. JDK versión 17  (debe estar en la variable de entorno)

### Pasos de Ejecucion

- Abre el terminal desde el directorio del proyecto y ejecuta:

    1. ./gradlew clean test

### Descripcion de las Tecnologias Utilizadas

- Para el ejercicio de automatizacion propuesto se ha utilizado el framework de Karate en leguage de programacion java.
- Adicionalmente se ha hecho uso de los siguientes frameworks: gherkin, cucumber, Junit y librerias como lombok, SonarLink, cucumber for java

### Notas adicionales

- El reporte sera generado en: api_automation_serenitybdd_karate\build\reports\tests\test\index.html 
- Se han omitido las tildes en el presente documento para evitar caracteres no deseados en caso de abrir el documento en un dispositivo con un lenguaje diferente al espanol.