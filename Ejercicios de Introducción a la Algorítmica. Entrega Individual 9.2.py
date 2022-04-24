numero1 = float(input("Introucir numero1= "))
numero2 = float(input("Introucir numero2= "))
numero3 = float(input("Introucir numero3= "))

c1 = float(input("Introucir coeficiente de ponderación de numero1= "))
c2 = float(input("Introucir coeficiente de ponderación de numero2= "))
c3 = float(input("Introucir coeficiente de ponderación de numero3= "))


media_ponderada= ((numero1*c1)+(numero2*c2)+(numero3*c3))/(numero1+numero2+numero3)



print("La media ponderada de los tres numeros es = "+ str(media_ponderada))