<hr>

**INTEGRANTES**
- SANCHEZ TASEJ FRANCISCO JAVIER     2012421
- SALGUERO SANDOVAL MIGUEL ANTONIO    1626923
- ORDOÑEZ LÓPEZ IVÁN ALEXANDER    1567523

## 1. Niveles de aislamiento

Los niveles de aislamiento determinan cómo y cuándo los cambios realizados por una transacción se vuelven visibles para otras transacciones concurrentes. Afectan tanto la integridad como la concurrencia dentro del sistema de gestión de bases de datos (DBMS). Los cuatro niveles estándar, de menor a mayor aislamiento, son:

- **Lecturas no comprometidas (Read Uncommitted):**
    - Permite leer datos que han sido modificados por otras transacciones, incluso si esos cambios no han sido confirmados (commit). Esto permite las llamadas “lecturas sucias” y proporciona el mayor rendimiento, pero el menor nivel de integridad
    - Problemas que pueden aparecer: lecturas sucias, lecturas no repetibles y lecturas fantasmas.
        
- **Lecturas comprometidas (Read Committed):**
    - Solo permite leer datos que han sido confirmados por otras transacciones. No permite lecturas sucias, pero sí lecturas no repetibles y lecturas fantasmas
    - Cada vez que se realiza una consulta, se garantiza que los datos ya fueron confirmados; sin embargo, si se vuelve a consultar la misma fila, su valor podría haber cambiado debido a otra transacción.
        
- **Lecturas repetibles (Repeatable Read):**
    - Asegura que si una transacción lee una fila, ninguna otra transacción puede modificar o eliminar esa fila hasta que la transacción original termine. Previene las lecturas no repetibles, pero permite lecturas fantasmas
    - Las filas leídas durante la transacción permanecen inalteradas durante la duración de la misma.
        
- **Serializable:**
    - Es el nivel más alto de aislamiento. Garantiza que la ejecución concurrente de transacciones produce el mismo resultado que si se ejecutaran en serie, una tras otra. Previene lecturas sucias, lecturas no repetibles y lecturas fantasmas
    - Puede implicar bloqueos sobre rangos completos de filas, afectando la concurrencia del sistema pero asegurando máxima consistencia.

|Nivel de aislamiento|Lecturas sucias|Lecturas no repetibles|Lecturas fantasmas|
|---|---|---|---|
|No comprometidas|Sí|Sí|Sí|
|Comprometidas|No|Sí|Sí|
|Repetibles|No|No|Sí|
|Serializable|No|No|No|

## 2. Problemas de lecturas en transacciones

- **Lecturas sucias (Dirty Reads):**
    - Ocurren cuando una transacción lee datos modificados por otra transacción que aún no ha hecho commit. Si esa transacción se revierte (rollback), los datos leídos no reflejan datos permanentes en la base de datos, provocando inconsistencias
    - Solo posibles con el nivel de aislamiento más bajo (Read Uncommitted).
        
- **Lecturas no repetibles (Non-Repeatable Reads):**
    - Se producen cuando una transacción lee la misma fila dos veces y obtiene valores diferentes porque otra transacción ha modificado o eliminado esa fila entre ambos accesos
    - Posibles en niveles Read Uncommitted y Read Committed.
        
- **Lecturas fantasma (Phantom Reads):**
    - Suceden cuando una transacción ejecuta una misma consulta dos veces (por ejemplo, un SELECT con un criterio de búsqueda), y la segunda vez obtiene un conjunto de resultados diferente porque otra transacción insertó, actualizó o eliminó filas que cumplen con ese criterio
    - Solo el nivel serializable previene realmente este fenómeno, bloqueando rangos de datos y no solo filas individuales.