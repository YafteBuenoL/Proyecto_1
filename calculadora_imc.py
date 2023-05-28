print("Hola calcularemos tu IMC")#se da la bienvenida
nombre = input("Escribe tu nombre: ")#se pide escribir nombre
apellido1 = input("Escribe tu apellido paterno: ")#se pide escribir apellido paterno
apellido2= input("Escribe tu apellido materno: ")#se pide escribir apellido materno
edad = int(input("Escriba su edad: "))#se pide escribir la edad
estatura = float(input("Escriba su estatura: "))#se pide escribir la estatura
peso = float(input("Escriba su peso: "))#se pide escribir peso


print ("Sus datos son: ")
print (f"Nombre: {nombre}")
print (f"Apellido paterno: {apellido1}")
print (f"Apellido materno: {apellido2}")
print (f"Su edad es: {edad}")
print (f"Su estatura es: {estatura}")
print (f"Su peso es: {peso}")
print ("Su Indice de Masa Corporal es: ")

a = (estatura ** 2)
imc = (peso / a)

round(imc)
print(imc)