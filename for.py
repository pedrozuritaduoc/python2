"""
#For 
for variable in elemento_iterable (lista, rango, etc)
   bloque de instrucciones

"""

contador = 0
resultado = 0

for contador in range(0, 5):
    print("Voy por el "+ str(contador))

    resultado = resultado + contador
print(f"El resultado es: {resultado}")    

#ejemplo tablas de multiplicar

print("\n----ejemplo -------")

num_user = int(input("ingresa numero de la tabla: "))

if num_user < 1:
    num_user = 1

for num_tabla in range(1, 11):
    print(f"{num_user}x{num_tabla}= {num_user*num_tabla}")
else:
    print("Tabla finalizada")     


