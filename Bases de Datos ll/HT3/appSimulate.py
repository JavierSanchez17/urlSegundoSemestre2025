from flask import Flask, request, jsonify, send_from_directory, session
import mysql.connector
from mysql.connector import Error
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Configuración de la base de datos
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "S@nchez695313",  
    "database": "transacciones_demo"
}

def get_db_connection():
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def init_session():
    if 'transaction_active' not in session:
        session['transaction_active'] = False
        session['pending_inserts'] = []

@app.route("/")
def servir_html():
    return send_from_directory(".", "index.html")

@app.route("/styles.css")
def servir_css():
    return send_from_directory(".", "styles.css")

@app.route("/api", methods=["POST", "GET", "OPTIONS"])
def api():
    print(f"[DEBUG] API called with method: {request.method}, action: {request.values.get('action')}")
    
    if request.method == "OPTIONS":
        return '', 200

    init_session()
    action = request.values.get("action")

    try:
        if action == "start_transaction":
            session['transaction_active'] = True
            session['pending_inserts'] = []
            session.permanent = True
            
            return jsonify({
                "success": True,
                "message": "Transacción iniciada.",
                "transaction_id": session.get('_id', 'default')
            })

        elif action == "insert_data":
            if not session.get('transaction_active', False):
                return jsonify({"success": False, "message": "No hay transacción activa"})
            
            nombre = request.values.get("nombre", "").strip()
            
            if not nombre:
                return jsonify({"success": False, "message": "El campo nombre es obligatorio"})
            
            # Simular inserción pendiente
            fake_id = len(session['pending_inserts']) + 1000  # ID temporal
            session['pending_inserts'].append({
                'nombre': nombre,
                'temp_id': fake_id
            })
            session.modified = True
            
            print(f"[DEBUG] Datos pendientes en transacción: {session['pending_inserts']}")
            
            return jsonify({
                "success": True,
                "message": f"Nombre guardado (pendiente de confirmación). Total pendientes: {len(session['pending_inserts'])}",
                "inserted_id": fake_id,
                "pending_count": len(session['pending_inserts'])
            })

        elif action == "commit_transaction":
            if not session.get('transaction_active', False):
                return jsonify({"success": False, "message": "No hay transacción activa"})
            
            pending_count = len(session.get('pending_inserts', []))
            if pending_count == 0:
                return jsonify({"success": False, "message": "No hay datos pendientes para confirmar"})
            
            connection = get_db_connection()
            if not connection:
                return jsonify({"success": False, "message": "No se pudo conectar a la base de datos"})
            
            cursor = None
            try:
                cursor = connection.cursor()
                connection.start_transaction()
                print(f"[DEBUG] Iniciando transacción real para {pending_count} registros")
                
                inserted_ids = []
                # Insertar todos los datos pendientes
                for insert_data in session['pending_inserts']:
                    query = "INSERT INTO persona (nombre) VALUES (%s)"
                    cursor.execute(query, (insert_data['nombre'],))
                    inserted_ids.append(cursor.lastrowid)
                    print(f"[DEBUG] Insertado: {insert_data['nombre']} con ID real: {cursor.lastrowid}")
                
                connection.commit()
                print(f"[DEBUG] Transacción confirmada. IDs reales: {inserted_ids}")
                
                # Limpiar sesión
                session['transaction_active'] = False
                session['pending_inserts'] = []
                session.modified = True
                
                return jsonify({
                    "success": True, 
                    "message": f"Transacción confirmada. {pending_count} persona(s) guardada(s) permanentemente.",
                    "inserted_count": pending_count,
                    "real_ids": inserted_ids
                })
                
            except Error as e:
                if connection:
                    connection.rollback()
                print(f"[DEBUG] Error en transacción, haciendo rollback: {e}")
                return jsonify({"success": False, "message": str(e)})
            finally:
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()

        elif action == "rollback_transaction":
            if not session.get('transaction_active', False):
                return jsonify({"success": False, "message": "No hay transacción activa"})
            
            pending_count = len(session.get('pending_inserts', []))
            pending_names = [item['nombre'] for item in session.get('pending_inserts', [])]
            
            print(f"[DEBUG] Haciendo rollback de {pending_count} registros: {pending_names}")
            
            # Simplemente limpiar la sesión
            session['transaction_active'] = False
            session['pending_inserts'] = []
            session.modified = True
            
            return jsonify({
                "success": True, 
                "message": f"Transacción cancelada. {pending_count} operación(es) descartada(s): {', '.join(pending_names) if pending_names else 'ninguna'}",
                "discarded_count": pending_count,
                "discarded_names": pending_names
            })

        elif action == "get_data":
            print(f"[DEBUG] get_data request received")
            connection = get_db_connection()
            if not connection:
                print(f"[DEBUG] Database connection failed")
                return jsonify({
                    "success": False,
                    "message": "No se pudo conectar a la base de datos",
                    "data": []
                })
            
            cursor = None
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT id, nombre FROM persona ORDER BY id DESC")
                rows = cursor.fetchall()
                print(f"[DEBUG] Found {len(rows)} records")
                return jsonify({
                    "success": True,
                    "data": rows,
                    "total_records": len(rows)
                })
            except Error as e:
                print(f"[DEBUG] Database error: {e}")
                return jsonify({
                    "success": False,
                    "message": str(e),
                    "data": []
                })
            finally:
                if cursor:
                    cursor.close()
                if connection:
                    connection.close()

        return jsonify({"success": False, "message": "Acción no válida"})

    except Exception as e:
        return jsonify({"success": False, "message": f"Error inesperado: {str(e)}"})

@app.after_request
def aplicar_cors(respuesta):
    respuesta.headers["Access-Control-Allow-Origin"] = "http://localhost:5500"
    respuesta.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    respuesta.headers["Access-Control-Allow-Headers"] = "Content-Type"
    respuesta.headers["Access-Control-Allow-Credentials"] = "true"
    return respuesta

if __name__ == "__main__":
    app.run(debug=True)