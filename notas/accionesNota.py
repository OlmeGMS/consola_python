#import notas.nota as modelo
from ..notas import nota as modelo


class Acciones:
    def crear(self, usuario):
        print(f"\nOk {usuario[1]}!! Vamos a crear una nueva nota...")
        titulo      = input("Por favor digita el titulo de tu nota: ")
        descripcion = input("Digita el contenido de tu nota: ")
        
        nota        = modelo.Nota(usuario[0], titulo, descripcion)
        guardar     = modelo.guardar()

        if guardar[0] >= 1:
            print(f"Perfecto has guardado la nota: {nota.titulo}")
        else:
            print(f"No se ha guardado la nota, lo sentimos {usuario[1]}")