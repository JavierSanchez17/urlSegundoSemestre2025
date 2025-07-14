## Usando estilos y patrones en software

Históricamente, en la industria del software ha sido común que diseñadores y arquitectos creen nuevas soluciones para problemas conocidos, sin aprovechar experiencias previas. Esto ocurrió en parte por la falta de soluciones estándar accesibles para problemas de diseño y arquitectura.

**En los años 90** surgió el movimiento de patrones de diseño, inspirado en el trabajo de Christopher Alexander en arquitectura de edificios. Se comenzó a catalogar soluciones probadas y reutilizables para problemas comunes de software.

### ¿Qué es un patrón de software?

Un patrón proporciona una solución estándar y comprobada que puede reutilizarse. Incluye cinco elementos esenciales:

1. **Nombre:** Memorable y significativo para facilitar su discusión.
    
2. **Contexto:** Situación en la que se aplica el patrón.
    
3. **Problema:** Descripción clara del desafío que resuelve.
    
4. **Solución:** Diseño que explica cómo los elementos colaboran.
    
5. **Consecuencias:** Impacto, beneficios y posibles desventajas.
    

### Ejemplo: Patrón Adapter

Este patrón adapta la interfaz de un componente para que otro pueda usarlo. Se utiliza cuando dos sistemas no son compatibles directamente, como un cliente .NET que necesita usar un servicio Java. El _adapter_ transforma las llamadas y respuestas para que ambos elementos puedan comunicarse.

**Ventajas:**

- Desacoplamiento entre cliente y servicio.
    
- Reutilización con distintos clientes.
    

**Desventajas:**

- Posible pérdida de eficiencia.
    
- Mayor mantenimiento si cambian las interfaces.
    

### Tipos de patrones

1. **Estilos arquitectónicos:** Soluciones para la estructura global del sistema.
    
2. **Patrones de diseño:** Soluciones para detalles estructurales de componentes.
    
3. **Modismos de lenguaje (idioms):** Soluciones específicas a un lenguaje de programación.
    

### Ejemplo de estilo arquitectónico: Pipes and Filters

Usado para sistemas que procesan datos en pasos secuenciales.

- **Filtros:** Procesan datos de forma modular.
    
- **Tuberías (pipes):** Conectan los filtros y transfieren datos.
    
- **Ventajas:** Reutilización, cambios fáciles, soporte a procesamiento paralelo.
    
- **Desventajas:** Manejo de errores complejo, transformación de datos añade sobrecarga.

|Estilo|Ventajas principales|Desventajas clave|
|---|---|---|
|Cliente/Servidor|Centraliza procesamiento sensible|Ineficiencia por comunicación remota|
|Computación en capas|Claridad, reutilización|Complejidad y sobrecarga entre capas|
|Peer-to-Peer|Escalabilidad y resiliencia|Dificultad para garantizar respuesta uniforme|
|Publicador/Suscriptor|Comunicación asíncrona flexible|Suscriptores dependen del editor|