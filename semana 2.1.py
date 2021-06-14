num = 10
num= "20"
if type(num)== int:
    num= num+2
else:
    print("El valor no es numerico")

def mensaje(pr):
    print(pr)

mensaje("Esto es Python")
mensaje("¡Sorprendente!, ¿Verdad?")

class sintaxis:
    # __init__ Metodo constructor se ejecuta cuando se instancia la clase cuyo objetivo es crear
    # e inicializar los atributos de la clase. Self es un objeto que representa la clase creada
    def __init__(self, dato="instancia de la clase "):
        self.frase=dato

    def usoVariable(self):
        edad, pesoo = 19, 65
        nombres = "Alan Flores"
        Sexo = "M"
        estadoC = False
        print ("estado civil= {} y de sexo: {}".format(estadoC,type(estadoC)))
        #tuplas= () son colecciones de datos de cualquier tipo inmutables

        usuario= ()
        usuario= ("afloresr3", "1234", "afloresr3@unemi.edu.ec", False)
        #               0         1                 2              3 
        # usuario[4]="Naranjito"
        x = usuario[0]
        # listas = [] colecciones multiples
        materias = ["Programacion web", "Php", "POO"]
        #                    0            1      2
        materias[1]= "Python"
        materias.append("Go")
        # diccionario = {} colecciones de objetos clave: valor tipo json
        persona= {}
        persona= {"nombre": "Alan", "edad": 19, "fac": "faci"}
        persona["edad"]= 19
        persona["cargo"]= "Estudiante"
        print(nombres,nombres[0],nombres[0:2],nombres[-1])
        print(usuario,usuario[0],usuario[0:2],usuario[-1])

                    
    def mostrar(self):
        print("mostrar")
        print(self.frase)

primero = sintaxis() #instancia la clase(ejecuta __init___) y se crea el metodo uno con todas las clases
primero.usoVariable()
print(primero.frase)
primero.mostrar()