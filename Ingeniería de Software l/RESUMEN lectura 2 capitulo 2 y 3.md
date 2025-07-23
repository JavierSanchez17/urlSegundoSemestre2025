# Capítulo 2: Conceptos de Arquitectura de Software

## 1. Definición de Arquitectura de Software

La arquitectura de un sistema de software intensivo es el conjunto de estructuras del sistema, formadas por:

- Elementos de software (módulos, clases, servicios, etc.).
- Propiedades externas de dichos elementos.
- Relaciones entre ellos.

Esta definición, adoptada por el SEI de Carnegie-Mellon, ofrece la base para entender cómo se diseña, describe y evalúa cualquier sistema de software.

---

## 2. Estructuras y Propiedades Externas

1. **Estructuras estáticas (tiempo de diseño):**
    
    - Definen los elementos internos y cómo se organizan: módulos, clases, procedimientos, componentes de hardware (discos, routers) y sus dependencias.
    - Ejemplo: jerarquías de módulos o relaciones de dependencia.
2. **Estructuras dinámicas (tiempo de ejecución):**
    
    - Describen las interacciones en ejecución: flujos de información, llamadas a procedimientos, creación y destrucción de datos.
3. **Propiedades externas:**
    
    - **Comportamiento visible:** qué hace el sistema desde fuera, modelado como “caja negra” (petición → respuesta).
    - **Propiedades de calidad (no funcionales):** performance, seguridad, escalabilidad, disponibilidad, mantenibilidad, accesibilidad, etc.

---

## 3. Arquitecturas Candidatas: Ejemplo de Sistema de Reservas Aéreas

Se presentan dos estilos de arquitectura como candidatas:

|Criterio|Arquitectura Cliente/Servidor (2 capas)|Arquitectura Cliente Delgado (3 capas)|
|---|---|---|
|Estructura estática|Clientes (presentación, lógica, datos, red) ↔ Servidor (BD) via WAN|Clientes (presentación, red) ↔ Servidor de aplicaciones (lógica, datos) ↔ Servidor de BD|
|Estructura dinámica|Modelo solicitud-respuesta directo entre cliente y servidor|Solicitud cliente → app server → BD → app server → cliente|
|Ventajas típicas|Simplicidad operativa, rapidez de desarrollo, menor coste inicial|Mejor escalabilidad, menor requerimiento hardware cliente, mayor seguridad|
|Desventajas típicas|Menor flexibilidad para escalar, clientes más pesados|Complejidad operativa y de despliegue mayor|

Cada candidato debe analizarse para evaluar cómo satisface el comportamiento funcional (reservar, cancelar, transferir vuelos) y las propiedades de calidad (tiempo de respuesta, throughput, disponibilidad).

---

## 4. Elementos Arquitectónicos

Un elemento arquitectónico es una unidad fundamental del sistema con:

- **Responsabilidades claras.**
- **Límite bien definido.**
- **Interfaces explícitas** que exponen sus servicios.

Ejemplos: subsistemas, bibliotecas, servicios Web, componentes de negocio, dispositivos de red.

---

## 5. Stakeholders (Partes Interesadas)

- **Definición:** persona, grupo o entidad con interés o preocupación sobre la arquitectura.
- **Ejemplos:** usuarios finales, desarrolladores, operadores, testers, patrocinadores, reguladores.
- **Preocupaciones (“concerns”):** requisitos funcionales, costes, plazos, calidad, seguridad.
- **Triángulo de calidad:**
    - Alcanzar dos de tres atributos (coste, calidad, tiempo de entrega) suele ser lo máximo posible.
    - El arquitecto equilibra los trade-offs según prioridades de stakeholders.

---

## 6. Descripción Arquitectónica (AD)

- **Definición:** conjunto de productos (modelos, principios, restricciones, etc.) que documentan la arquitectura de forma comprensible para los stakeholders y demuestran que sus preocupaciones están satisfechas.
- **Uso:** sirve como memoria, registro de decisiones y base de análisis.
- **Requisito:** debe incluir sólo la información necesaria y estar actualizada.

---

## 7. Relaciones Clave entre Conceptos

```text
Stakeholder → define necesidades y preocupaciones  
Sistema → responde a esas necesidades  
Arquitectura → compuesta por elementos y relaciones  
AD (Descrip. Arquitectónica) → documenta arquitectura para stakeholders  
```

---

## 8. Principios Fundamentales

- Todo sistema tiene arquitectura, documentada o no.
- Las propiedades externas emergen de estructuras internas.
- Los sistemas son tan fuertes como sus elementos más débiles.
- Una buena arquitectura satisface los objetivos de sus stakeholders.
- Una AD eficaz comunica claramente la arquitectura a quienes la necesitan.

---

## 9. Puntos Clave para Recordar

- **Estructuras estáticas vs dinámicas vs externas vs calidad.**
- **Arquitecturas candidatas:** múltiples enfoques, análisis comparativo.
- **Elementos arquitectónicos** como piezas modulares.
- **Stakeholders** impulsan el diseño, a través de sus prioridades.
- **ADs**: documento vivo que alinea la arquitectura con las expectativas.


# Capítulo 3: Viewpoints y Views

## 1. Introducción a Viewpoints y Views

La forma de comunicar la arquitectura de software a distintos interesados se basa en dos conceptos clave:

- Un **viewpoint** es una perspectiva o plantilla que define el estilo, las convenciones y los requisitos para desarrollar una representación arquitectónica.
- Una **view** es la instancia concreta de esa perspectiva, mostrando los elementos y relaciones de la arquitectura para satisfacer inquietudes específicas de los stakeholders.

---

## 2. Conceptos Fundamentales

- Viewpoint
    
    - Define la **sintaxis** (lenguaje, notación) y la **semántica** (modelos, análisis) que se utilizarán.
    - Enumera a los **stakeholders** relevantes y sus **concerns** (requisitos y objetivos).
    - Establece criterios de validación y técnicas de análisis.
- View
    
    - Representación tangible: diagramas, tablas, descripciones textuales.
    - Incluye los **elementos arquitectónicos**, sus **interfaces** y las **relaciones** entre ellos.
    - Se genera a partir de un viewpoint para mostrar cómo se aborda cada concern.
- IEEE 1471
    
    - Norma que formaliza los conceptos de stakeholders, concerns, viewpoints y views.
    - Destaca la necesidad de documentar varias views para cubrir todas las preocupaciones relevantes.

---

## 3. Estructura de un Viewpoint

Cada viewpoint suele componerse de los siguientes apartados:

1. Nombre y propósito del viewpoint.
2. Stakeholders a los que va dirigido.
3. Concerns que atiende (por ejemplo, rendimiento, seguridad, mantenibilidad).
4. Tipo de modelo (estático, dinámico, de asignación).
5. Lenguaje o notación recomendados (UML, ADL, diagramas de flujo).
6. Técnicas de validación y criterios de éxito.

---

## 4. Contenido de una View

Al crear una view, se documentan:

- **Elementos arquitectónicos**: componentes, módulos, procesos, nodos.
- **Relaciones**: dependencias, flujos de datos o control, asignaciones físicas.
- **Escenarios**: casos de uso o interacciones clave que ilustran el comportamiento.
- **Justificación**: comentarios que expliquen cómo este view satisface los concerns.

---

## 5. Proceso para Generar Views

1. **Identificar stakeholders** y recopilar sus concerns.
2. **Seleccionar viewpoints** que cubran esos concerns de forma complementaria.
3. **Definir y crear views** usando los modelos y notaciones de cada viewpoint.
4. **Validar** cada view frente a los criterios y técnicas especificadas.
5. **Asegurar la consistencia** entre todas las views mediante correspondencias y trazabilidad.

---

## 6. Ejemplos de Viewpoints y Views

|Viewpoint|Ejemplo de View|
|---|---|
|Lógico|Diagrama de componentes y sus interfaces|
|Dinámico|Diagramas de secuencia o de colaboración para flujos de uso|
|Desarrollo (Código)|Estructura de paquetes, proyectos y dependencias en repositorio|
|Despliegue|Mapa de nodos físicos y sus conexiones|
|4+1 (Kruchten)|Vistas Lógica, de Procesos, de Desarrollo, Física y Escenarios|

---

## 7. Buenas Prácticas y Ventajas

- Cubrir **todas** las inquietudes críticas con un conjunto equilibrado de viewpoints.
- Emplear **notaciones familiares** a los stakeholders para mejorar la comprensión.
- Mantener **actualizadas** las views a medida que evoluciona la arquitectura.
- Usar **escenarios** comunes (5 a 10) para validar la interacción entre views.
