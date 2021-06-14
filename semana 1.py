"""Numero entero"""
x=int(input("Ingresa un número entero: "))
if x < 0 :
    x = 0
    print("Negativo cambiado a cero",)
elif x == 0 :
    print ("Cero")
elif x == 1 :
    print ("Uno")
else :
    print ("Ninguna opción")

print ("Ok") if type (x) == int else print ("-")  


"""Uso de While infinito"""
c=1
while True:
 print(c)
 break


# While Validacion
vocal = input ("Ingrese Vocal: ")
while vocal.lower() not in ("a", "e", "i", "o", "u"):
    if vocal =="." :
        break
    vocal = input ("Vocal: ")
print ("Su vocal o punto es : {}".format(vocal))


# for range(v) - range(vi,vf) - range(vi,vf,inc)
frase= input("ingrese frase: ")
for indice in range (len(frase)):
    print(indice, "=", frase [indice])

#for in cadena - in(tupla) - in[lista]
cvoc=0
for car in frase:
    if car in ("a","e","i","o","u","A","E","I","O","U"):
        if car in ["A","E","I","O","U"]:
            continue
        else:
            cvoc=cvoc+1
print("cantidad vocales:{}".format(cvoc))

#Comprehension - [var for in datos condicion]
[car for car in ["a","e","i","o","u"] if car not in ("a","i","o")]


"""Funciones sin retorno"""
def vocales(frase):
    for car in frase:
        if car in ("a","e","i","o","u"):
            print(car)

"""Llamada a función"""
oracion=input("Ingrese oración: ")
vocales(oracion.lower())


"""Función con retorno de valor"""
def promedio(notas):
    summ=0
    for n in notas:
        summ+=n
    return summ/len(notas)

#Llamada a función
listanotas=[2,4,6,8,10]
prom=promedio(listanotas)
print("Pomedio: {} = {}".format(listanotas,prom))


"""Funciones matematicas"""
import math
num1, num2,num,men=12.572, 15.4, 4, "1234"
print(math.ceil(num1),"\t", math.floor(num1))
print(round(num1,1),"\t", type(num),"\t", type(men))

#Funciones de cadenas
mensaje = "Hola"+"mundo"+"Python"
men1=mensaje.split()
men2="".join(men1)
print(mensaje[0], mensaje[0:4], men1, men2)
print (mensaje.find("mundo"),mensaje.lower())

#Funciones de fecha
from datetime import datetime, timedelta, date
hoy, fdia= datetime.now(), date.today()
futuro=hoy + timedelta(days=30)
dif, aa, mm, dd= futuro- hoy, hoy.year, hoy.month, hoy.day
fecha= date(aa,mm,dd+2)
print(hoy, fdia, futuro, dif, fecha)



#Tuplas - Listas - Diccionarios
usuario= ("dchiki", "1234", "chiki@gmail.com")
materias= ["Python", "PHP", "POO", "Go"]
docente= {"nombre" : "Daniel", "edad" : 50, "fac" : "faci"}
print (usuario[0], materias[1], docente["nombre"])
print(usuario[0:2], docente.keys(), docente.values())
materias.append("Programacion Movil")
docente["sexo"], docente["edad"]= "M", 51
print(materias, docente)
tupla, lista, diccionario= (), [], {}

#Recordatorio tuplas y listas con in
for valor in usuario: print(valor)

#Recorridos listas con enumerante
for i, c in enumerate(materias): print(i, ": ", c)

#Recorridos diccionario con items
for c, v in docente.items(): print(c, ": ", v)