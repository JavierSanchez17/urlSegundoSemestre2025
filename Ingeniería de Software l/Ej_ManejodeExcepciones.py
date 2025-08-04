# USAR EXCEPCIONES EN LUGAR DE CODIGOS DE ERROR
# USO INCORRECTO
def abrir_archivo(nombre):
    if nombre != "datos.txt":
        return -1 # código de error
        return 1 # éxito

resultado = abrir_archivo("archivo.txt")
if resultado == -1:
    print("Error: archivo no encontrado")
        
# USO CORRECTO 
def abrir_archivo(nombre):
    if nombre != "datos.txt":
        raise FileNotFoundError("El archivo no existe.")
    return "Archivo abierto"

try:
    abrir_archivo("archivo.txt")
except FileNotFoundError as e:
    print("Error:", e)
        
        
# SEPARAR LÓGICA DEL MANEJO DE ERRORES
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: división entre cero"

print(dividir(10, 2)) # 5.0
print(dividir(10, 0)) # Error: división entre cero


# USAR EXCEPCIONES NO COMPROBADAS
def obtener_precio(producto):
    if producto != "pan":
        raise ValueError("Producto no disponible")
    return 3.5

try:
    print(obtener_precio("leche"))
except ValueError as e:
    print("Error:", e)
    

# INCLUIR CONTEXTO EN EL MENSAJE DE EXCEPCION
def cargar_usuario(nombre):
    if nombre == "":
        raise ValueError("No se puede cargar un usuario con nombre vacío.")
    return {"nombre": nombre}

try:
    cargar_usuario("")
except ValueError as e:
    print("Error:", e)
    

# NO DEVOLVER NI PASAR NULL
# MAL USO
def buscar_producto(codigo):
    return None # Devolviendo Null

producto = buscar_producto("123")
if producto is not None:
    print(producto.nombre)

# USO CORRECTO
class ProductoNulo:
    nombre = "Producto desconocido"

def buscar_producto(codigo):
    return ProductoNulo()

producto = buscar_producto("123")
print(producto.nombre)