import os
libros=[]
usuarios=[]

def registrar():
    try:
        titulo = input("Ingrese el Título del libro a registrar: ")
        autor = input("Ingrese el Autor del libro a registrar: ")
        anno_publicacion = int(input(("Ingrese el Año de publicación del libro a registrar: ")))
        sku = str(input("Ingrese el SKU del libro a registrar: "))
        libro = {
            'Título':titulo,
            'Autor':autor,
            'Año de Publicación':anno_publicacion,
            'SKU':sku
        }

        if titulo == "" or autor == "" or anno_publicacion <=-2000 or sku == "":    
            print("Alguno de los datos ingresados está incompleto, intentelo nuevamente")
        else:
            print("El libro se ha registrado con éxito")
            libros.append(titulo)
            
            
    except ValueError:
        print("Dato erroneo")

def prestar():
    prestado = False
    usuario = input("Ingrese su nombre de usuario: ")
    sku = input ("Ingrese el SKU del libro")


def listar():
        for libro in libros:
            print(f"TÍTULO\t\tAUTOR\t\tAÑO DE PUBLICACIÓN\t\tSKU")
            print(f"{libro['titulo']}\t\t{libro['autor']}\t\t{libro['anno_publicacion']}\t\t{libro['sku']}\t\t")
 

def menu():
    while True:
        try:
            print("* * * * M E N Ú * * * *")
            print("1. Registrar libro\n2. Prestar Libro\n3. Listar todos los libros\n4. Imprimir reporte de prestamos\n5. Salir del programa")
            op = int(input("Seleccione una de las opciones: "))
            if op == 1:
                registrar()
            elif op == 2:
                prestar()
            elif op == 3:
                listar()
            elif op ==4:
                imprimir()
            elif op ==5:
                print("Programa finalizado...\nDesarrollado por Daniel Abarzúa\nRUN: 19.639.324-2")
                break
            else:
                print("La opción ingresada no existe")
        except ValueError:
            print("La opción ingresada no es válida")
