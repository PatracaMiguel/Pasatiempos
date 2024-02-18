# Programa que calcule cuantos dias tienes de nacido

from datetime import datetime

nombre = str(input("Ingresa tu nombre completo "))
fechaN = input("Ingresa el año que naciste ")
fecha2 = input("Ingresa el año actual ")
fecha = datetime.strptime(fechaN,"%Y-%m-%d") 
fechaActual = datetime.strptime(fecha2,"%Y-%m-%d")

dias = fechaActual - fecha
edad = dias / 365
print(nombre)
print("Naciste en ",fecha)
print("Estamos a ",fechaActual)
print("Por lo tanto tienes ",edad,dias,"de nacido")