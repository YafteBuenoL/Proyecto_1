
# calculadora de IMC

print ("Hola calcularemos tu IMC")#se da la bienvenida
nombre = input("Escribe tu nombre: ")#se pide escribir nombre
apellido1 = input("Escribe tu apellido paterno: ")#se pide escribir apellido paterno
apellido2= input("Escribe tu apellido materno: ")#se pide escribir apellido materno

edad = int(input("Escriba su edad: "))#se pide escribir la edad
estatura = float(input("Escriba su estatura en cm: "))#se pide escribir la estatura
peso = float(input("Escriba su peso en kg: "))#se pide escribir peso


#Se imprimen los datos
print ("Sus datos son: ")
print (f"Nombre: {nombre}")
print (f"Apellido paterno: {apellido1}")
print (f"Apellido materno: {apellido2}")
print (f"Su edad es: {edad}")
print (f"Su estatura es: {estatura}")
print (f"Su peso es: {peso}")

imc = round(peso/(estatura ** 2),2) #se imprime el valor de imc

#Se identifica si el usuario tiene o no la mayoria de edad
if edad > 18:
    print("Usted tiene la mayoria de edad")
else:
    print("Usted aun no tiene la mayoria de edad")
print ("Su indice de masa corporal es de:",imc)

#Aqui se identifica que tipo que tipo de condicion tiene la persona dependiendo del valor de imc
if imc <= 18.9:
    print("Usted tiene bajo peso")
elif imc >= 19 and imc <= 24.99:
    print("Usted tiene peso normal")
elif imc >= 25 and imc <= 29.99:
    print("Usted tiene sobrepeso")
elif imc >= 30 and imc <= 34.99:
    print("Usted tiene obesidad leve")
elif imc >= 35 and imc <= 39.99:
    print("Usted tiene obesidad media")
elif imc >= 40:
    print("Usted tiene obesidad morbida")

exit()
