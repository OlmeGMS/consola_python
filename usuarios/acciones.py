import usuarios.usuario as userModel
import notas.accionesNota

class Acciones:
    def registro(self):
        print("\nOK!! Vamos a registrarte en el sistema...")
        nombre      = input("¿Cuales es tu nombre? ")
        apellido    = input("¿Cual es tu apellido? ")
        correo      = input("Introduce tu correo? ")
        password    = input("Introduce tu contraseña ")

        usuario     = userModel.Usuario(nombre, apellido, correo, password)
        registro    = usuario.registrar() 

        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].correo}")
        else:
            print("No te has registrado correctamente")
    def login(self):
        print("\nPor favor indentificate... ") 
        try:
            correo      = input("Introduce tu correo? ")
            password    = input("Introduce tu contraseña ") 

            usuario     = userModel.Usuario('', '', correo, password) 
            login       = usuario.identificar()  

            if correo == login[3]:
                print(f"\nBienvenido {login[1]}, te has registrado en el sitema {login[5]}")
                self.proximasAcciones(login)
            else:
                print("Al parecer las credenciales no son validas")
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto!! Por favor intentalo más tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles:
        - Crear nota(crear)
        - Mostrar tus notas (mostrar)
        - Eliminar nota (eliminar)
        - Salir (salir)
        """)
        accion = input("¿Que quieres hacer?: ")
        hazEl  = notas.accionesNota.Acciones()

        if accion == "crear":
            #print("Vamos a crear")
            hazEl.crear(usuario )
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            print("Vamos a mostrar")  
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            print("Vamos a eliminar")  
            self.proximasAcciones(usuario)
        elif accion == "salir":
            print(f"Ok {usuario[1]}, hasta pronto!!!")
            exit()
            

        