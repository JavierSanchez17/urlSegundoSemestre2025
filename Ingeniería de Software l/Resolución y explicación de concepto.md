**INTEGRANTES**
1. 1501321 - Allan Eduardo Pérez Ajanel
2. 2012421 -  Francisco Javier Sánchez Tasej
# **Manejo de Excepciones**
<hr>

El manejo de excepciones es una técnica que permite detectar y controlar errores que ocurren durante la ejecución de un programa, sin que éste se detenga bruscamente. En lugar de devolver códigos de error, se lanzan excepciones que pueden ser capturadas y gestionadas de manera ordenada.

Generalmente, el manejo de excepciones involucra estructuras como los bloques try y catch (u otros equivalentes según el lenguaje), donde el código susceptible a errores se coloca dentro de un bloque try. Si ocurre un error (llamado excepción), el flujo de ejecución pasa automáticamente al bloque catch, donde se define cómo responder: por ejemplo, mostrando un mensaje, registrando el error o ejecutando acciones alternativas. De esta forma, el manejo de excepciones actúa como una "red de seguridad", aumentando la robustez, mantenibilidad y experiencia de usuario del software
## **Principios Clave del Manejo de Excepciones**

- **Usar excepciones en lugar de códigos devueltos:**
    - En lugar de devolver un código de error que el programador debe verificar, se recomienda lanzar una excepción para separar la lógica del programa del control de errores.
    - Esto hace que el código sea más impio y legible

![[Pasted image 20250731092429.png]]

- **Separar lógica del manejo de errores:**
    - La idea es escribir el código como si todo fuera a salir bien, y manejar los errores aparte usando try, catch y finally.

![[Pasted image 20250731092451.png]]

- **Usar excepciones no comprobadas (unchecked):**
    - Las excepciones comprobadas (checked) en Java obligan a cambiar muchos métodos para declarar la excepción.
    - Las no comprobadas (unchecked) permiten mantener el código más flexible.

![[Pasted image 20250731092643.png]]
_En Python se puede lanzar errores cuando algo no tiene sentido, todas son no comprobadas_

- **Incluir contexto en las excepciones:**
    - Las excepciones deben tener mensajes claros que expliquen el error y ayuden a encontrarlo fácilmente (ej. tipo de error, ubicación, datos).

![[Pasted image 20250731092801.png]]

- **Evitar devolver o pasar null:**
    - En lugar de devolver null, es mejor lanzar una excepción o usar un “objeto especial” para evitar errores de tipo NullPointerException.

![[Pasted image 20250731092818.png]]
