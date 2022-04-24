numero1 = float(input("Introducir el dinero que tiene en la cuenta este usuario: "))

print("Las acciones que puede realizar son las siguientes: \n1: Retirar dinero de la cuenta \n2: Ingresar dinero en la cuenta")
print("Cual de estas opciones desea escoger? : (1 o 2)")

opcion = input()

if(opcion=="1"):
    if(numero1<0):
        print("Posee la autorización de un descubierto? (1=si / 2=no): ")
        permiso = input()

        if(permiso=="1"):
            retirar = float(input("Cuanto dinero desea retirar?: "))
            numero1 = numero1 - retirar
            print("Dinero en cuenta es igual a: " + str(numero1))

        if(permiso=="2"):
            print("Lo siento, no puede retirar dinero ya que su cuenta esta en numeros rojos ") 

    else:
        retirar = float(input("Cuanto dinero desea retirar?: "))
        numero1 = numero1 - retirar
        print("Dinero en cuenta es igual a: " + str(numero1))

        
       





if(opcion=="2"):
    ingresar = float(input("Cuanto dinero desea ingresar?: "))
    numero1 = numero1 + ingresar
    print("Dinero en cuenta es igual a: " + str(numero1))


