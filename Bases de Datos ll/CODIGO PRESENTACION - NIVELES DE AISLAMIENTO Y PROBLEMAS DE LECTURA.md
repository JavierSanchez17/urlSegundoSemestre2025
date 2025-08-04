<HR>

# NIVELES DE AISLAMIENTO
## Lecturas no Comprometidas:
Permite leer datos no confirmados (sin hacer commit)
Permite lecturas sucias, no repetibles y fantasmas

![[Pasted image 20250804085531.png]]

## Lecturas repetibles
Solo lee datos confirmados (Commit)
Permite lecturas no repetibles y fantasmas
![[Pasted image 20250804085559.png]]
## Lecturas Comprometidas
Evita lecturas sucias y no repetibles
Permite lecturas fantasma 
Es el nivel por defecto de mysql
![[Pasted image 20250804085621.png]]

## Serializable
Es el máximo nivel de aislamiento
Menor rendimiento debido a bloqueos
![[Pasted image 20250804085635.png]]

# PROBLEMAS DE LECTURA
## Lecturas Sucias
Lee datos modificados por otra transacción que aún no ha confirmado los cambios.

![[Pasted image 20250804085730.png]]

## Lecturas Fantasmas
Obtiene diferentes resultados al ejecutar la misma consulta dentro de una transacción debido a inserciones/eliminaciones de otras transacciones.
Cambia: La cantidad de registros que cumplen una condición
![[Pasted image 20250804085749.png]]

## Lecturas no repetibles
Obtiene diferentes valores al leer el mismo registro dentro de una transacción.
Cambia los valores de registros que ya existen
![[Pasted image 20250804085809.png]]
