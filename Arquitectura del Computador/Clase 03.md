# Circuito Secuencial
La definición de circuito secuencial es que va uno detras de otro, podemos ver un contador como un circuito secuencial, ya que esta es la manera más simple de verlo con un ejemplo
## Síncrono:
Su comportamiento se defino por el conocimiento de sus señales en instantes discretos de tiempo, quiere decir que todos los elementos reciben la misma señal de reloj (Todos están sincronizados mediante el tiempo)
## Asíncrono: 
Su comportamiento depende tanto de las entradas en cualquier instante de tiempo como el orden en que cambian las entradas a lo largo del tiempo, uno de los componentes recibe las señales de reloj, y todos los demás se coordinan en base a la salida del anterior o de otro (redes conectadas una con otra)

## Compuertas lógicas
![[Pasted image 20250714104028.png]]

## Latch
Almacena 1 bit mientras la señal está activa
**Definición**: Un **latch** es un circuito secuencial **nivel-sensible**. Su salida depende del estado actual de la entrada **y** del nivel del control (por ejemplo, una señal de habilitación).
**Ejemplo**: Latch SR (Set-Reset)
- Entradas: S (Set), R (Reset)
- Salidas: Q, Q'
- Se activa mientras una señal de control está en un nivel alto (por ejemplo, ENABLE = 1).
**Aplicación**:
- Memorias simples
- Retención temporal de datos mientras una línea de control esté activa
## Flip-Flop
Unidades de almacenamiento utilizado en la computación, almacena 1 bit al detectar un cambio (flanco)

**Definición**: Un **flip-flop** es un circuito secuencial **activado por flanco de reloj** (edge-triggered). Cambia su salida solo en el **flanco de subida (↑)** o **bajada (↓)** del reloj.
    
**Tipos comunes**:
- **D Flip-Flop**: Captura el valor de D en el flanco del reloj.    
- **T Flip-Flop**: “Togglea” (invierte) su salida si T = 1.        
- **JK Flip-Flop**: Versión mejorada del SR.        
- **SR Flip-Flop**: Similar al latch, pero activado por flanco.


**Basculación (Toggle):** En términos generales se aprendió que basculación es el cambio de estado entre 0 y 1 o de 1 a 0 
**BTG** - ByteToggle, operaciones a nivel bit (hablando de contadores se toma en cuenta el acarreo)
**BS** - Bit set, Poner un bit en 1
**BC** - Bit clear, Poner un bit en 0





