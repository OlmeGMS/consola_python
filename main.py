"""
Proyecto Python y Mysql
- Abrir asistente
- Login o registro
- Si eleimos registro, creará un usuario en la bd
- Si elegimos login, identifica al usuario y nos preguntará
- Creamos nota, mostrar nota, borrarlas
"""
#from usuarios import acciones
import usuarios.acciones as acciones

print("""
Acciones disponibles:
    -Registro
    -Login
""")

hazEl   = acciones.Acciones()
accion  = input("¿Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
else:
    print("Lo sentimos no has ingresado una opción valida")