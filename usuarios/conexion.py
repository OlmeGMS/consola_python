import mysql.connector
from mysql.connector import errorcode

def conectar() :
    # Conexión
    try: 
        database = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="root",
            port="8889",
            database="master_python"
        )
    except mysql.connector.Error as e:
        if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("el usuario o la contraseña son incorrectos")
        elif e.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de datos no exite")
        else:
            print(e)   

    cursor = database.cursor(buffered=True)
    return [database, cursor]