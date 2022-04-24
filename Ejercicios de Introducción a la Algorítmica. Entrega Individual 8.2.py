invertido = input("Introducir cantidad de euros invertida: ")
intereses = input("Introducir intereses mensuales(en porcentaje): ")
tiempo = input("Introducir meses pasados: ")




importe= (float(invertido)*(float(intereses)/100))*float(tiempo)



print("Importe generado en los "+ str(tiempo) +" meses es igual a "+ str(importe))

