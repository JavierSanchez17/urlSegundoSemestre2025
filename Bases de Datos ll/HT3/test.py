import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="S@nchez695313",  
    database="transacciones_demo"
)
print("Conexión exitosa!" if connection.is_connected() else "Error de conexión")