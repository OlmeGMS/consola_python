import datetime
import hashlib
import usuarios.conexion as conexion

connect     = conexion.conectar()
database    = connect[0]
cursor      = connect[1]

class Usuario:

    def __init__(self, nombre, apellido, correo, password):
        self.nombre     = nombre
        self.apellido   = apellido
        self.correo     = correo
        self.password   = password
    def registrar(self):
        fecha   = datetime.datetime.now()
        # Cifrar la constraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        sql     = "INSERT INTO usuarios VALUES(null, %s,%s,%s,%s,%s)"
        usuario = (self.nombre, self.apellido, self.correo, cifrado.hexdigest(), fecha)
        try:
            cursor.execute(sql, usuario)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]


        return result
    def identificar(self):
        sql = "SELECT * FROM usuarios WHERE email = %s AND password = %s"

        # Cifrar la constraseña
        cifrado = hashlib.sha256()
        cifrado.update(self.password.encode('utf8'))
        # Datos para la consulta
        usuario = (self.correo, cifrado.hexdigest())
        cursor.execute(sql, usuario)
        result = cursor.fetchone()

        return result
