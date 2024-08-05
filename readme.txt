Automatizacion API

-Aplicante: 
    Galo Sanchez

-Ejercicio: 

    Ejercicio 2

    Prueba automatizada de API de un flujo de agregar y actualizar los datos de una mascota en el api https://petstore.swagger.io/ que incluye:

        a. Añadir una mascota a la tienda
        b. Consultar la mascota ingresada previamente (Búsqueda por ID)
        c. Actualizar el nombre de la mascota y el estatus de la mascota a “sold”
        d. Consultar la mascota modificada por estatus (Busqueda por estatus)

-Tecnologias utilizadas:

    Para el ejercicio de automatizacion propuesto se ha utilizado el framework de requests en leguage de programacion Python 
    puesto que son las tecnologias en las que poseo mayor conocimiento. Adicionalmente se han utilizado librerias de soporte como Unittest
    para el manejo y organizacion de casos de prueba y Test Suites para un mayor control de ejecucion y generacion de reportes en HTML con 
    HtmlTestRunner. (Otras librerias tambien se han implementado para el uso en los diferentes casos de prueba y las validaciones propuestas).

-Descripcion de Archivos:

    -Scripts de Python: 'api_automation_example.py' que comprende 4 casos de prueba que van
    acorde a las acciones solicitadas en el ejercicio (Añadir una mascota a la tienda, Consultar la mascota ingresada previamente (Búsqueda por ID), 
    Actualizar el nombre de la mascota y el estatus de la mascota a “sold”, Consultar la mascota modificada por estatus (Busqueda por estatus)). 
    Adicionalmente se puede encontrar una funcion implementada por efectos de las validaciones deseadas.
    
    -Scripts de Python: 'test_suite.py' conforma el Test suite a ser ejecutado estableciendo el orden de ejecucion asi como la generacion del reporte
    HTML con los resultados obtenidos.
    
    -Archivo de texto: 'readmy.txt' presente documento en el que se detallan los pasos de ejecucion de los scripts y detalles adicionales de la 
    solucion implementada.
    
    -Archivo de texto: 'conclusiones.txt' archivo que resume los hallazgos y resultados obtenidos del ejercicio propuesto.
    
    -Directorio: Una carpeta con el nombre Reports donde se almacenaran los reportes HTML generados de cada iteracion ejecutada.

-Pasos de ejecucion:

    -Ejecutar el script 'test_suite.py'
    -Se lo puede hacer directamente desde el terminal 'python3 test_suite.py'
    -El reporte HTML se lo puede encontrar en la carpeta 'Reports' 

-Notas adicionales:

    Se han omitido las tildes en el presente documento para evitar caracteres no deseados en caso de abrir el documento en un dispositivo con un lenguaje 
    diferente al espanol.