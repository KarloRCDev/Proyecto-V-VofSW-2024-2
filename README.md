Correcciones de Código y Mejoras de Seguridad
Este documento detalla las correcciones realizadas en el proyecto easyVote para abordar problemas identificados por SonarLint y mejorar la calidad general del código.
1. Refactorización de la Función de Ordenamiento Burbuja
Problema: SonarLint(python:S3776) - Complejidad ciclomática excesiva.
Solución: Se refactorizó la función burbuja para reducir su complejidad:

Se extrajeron las operaciones de comparación e intercambio a funciones separadas.
Se simplificó el bucle principal.

Beneficios:

Menor complejidad ciclomática.
Mayor legibilidad y mantenibilidad del código.

2. Mejora de Seguridad en la Conexión a la Base de Datos
Problema: SonarLint(python:S2115) - Credenciales de base de datos en el código fuente.
Solución: Se implementó un manejo más seguro de las credenciales de la base de datos:

Se creó un archivo config.py para almacenar la configuración de la base de datos.
Se implementó una clase SesionManager para manejar las conexiones de forma segura.
Se utilizó el patrón de contexto (with statement) para gestionar recursos.

Beneficios:

Mayor seguridad al no exponer credenciales en el código fuente.
Mejor gestión de recursos de base de datos.
Código más modular y fácil de mantener.

3. Corrección de Convenciones de Nomenclatura
Problema: SonarLint(python:S116) - Nombres de variables que no siguen las convenciones de Python.
Solución: Se renombraron las variables para seguir la convención snake_case de Python:

candidatosM -> candidatos_m
votosM -> votos_m
candidatosF -> candidatos_f
votosF -> votos_f

Además, se realizaron mejoras adicionales:

Se dividió el código en métodos más pequeños y específicos.
Se mejoró el manejo de conexiones a la base de datos.
Se optimizó el formateo de la salida de tiempo.

Beneficios:

Mayor consistencia con las convenciones de Python.
Mejor legibilidad y mantenibilidad del código.
Estructura de código más organizada y modular.

Implementación
Para implementar estos cambios:

Actualice el archivo de la función burbuja con el nuevo código refactorizado.
Cree un archivo config.py para almacenar las configuraciones de la base de datos.
Actualice las clases y métodos relevantes con los nuevos nombres de variables y estructuras de código.
Asegúrese de agregar config.py a su .gitignore para evitar exponer información sensible.

Estas correcciones mejoran significativamente la calidad, seguridad y mantenibilidad del código del proyecto easyVote.
