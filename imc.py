print("Hola calcularemos tu IMC")
nombre = input("Escribe tu nombre: ")
apellido1 = input("Escribe tu apellido paterno: ")
apellido2= input("Escribe tu apellido materno: ")
edad = int(input("Escriba su edad: "))
estatura = float(input("Escriba su estatura: "))
peso = float(input("Escriba su peso: "))


print ("Sus datos son: ")
print (f"Nombre: {nombre}")
print (f"Apellido paterno: {apellido1}")
print (f"Apellido materno: {apellido2}")
print (f"Su edad es: {edad}")
print (f"Su estatura es: {estatura}")
print (f"Su peso es: {peso}")
print ("Su Indice de Masa Corporal es: ")

a = (estatura**2)
imc = (peso / a)

print(imc)