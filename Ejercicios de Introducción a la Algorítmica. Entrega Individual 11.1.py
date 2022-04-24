importe_normal_empleado = float(input("Introucir el importe normal de este empleado: "))

importe_horasext=0




for x in range(52):
    horas = float(input("Introucir horas trabajadas la semana "+str(x+1)+": "))
    if(horas>35 and horas<44):
        importe_horasext=float(importe_horasext) + ((horas-35)*importe_normal_empleado*1.25)
        

    if(horas>44):
        importe_horasext=float(importe_horasext) + ((8)*importe_normal_empleado*1.25)
        importe_horasext=float(importe_horasext) + ((horas-43)*importe_normal_empleado*1.5)

    
    

print("El importe por horas extra trabajadas por este empleado es: "+ str(importe_horasext))

