#27) Codificar un programa que solicite la carga de un valor positivo y nos muestre desde 1 hasta el 
#valor ingresado de uno en uno.
print("###############################################")
print("####\tWalter Santillán ######################")
print("###############################################")

print("Solicito la carga de un valor\n")

valor = int(input("Ingresar un valor positivo: "))

x = 1

while x < valor:
    print(x) 
    x = x + 1