## Métodos Numéricos
## Métodos de Integración numérica de la regla del Simpson 1/3 y Simpson 3/8
## Tipo de método: Simpson 1/3, Simpson 1/3 multiple y Simpson 3/8
## By: PioneerAsp

def generaEcuacion(n): #Guarda el valor de los coeficientes de la ecuacion por numero de exponente de manera decendente
    m=n
    Lista =[]
    for i in range(n+1):
        Lista.append(float(input("Coeficiente de x^"+str(m)+": ")))
        m= m-1
        #print(i)
    return Lista

def evaluaFuncion(Lista,exponente,a): #Retorna la función evaluada
    n=exponente
    sum=0
    for i in range(exponente+1):
        aux=Lista[i]
        sum= sum + (aux*(a**(n-i)))
        #print (sum)
    return sum

def SumatoriaIP(Lista,e,xi,n,h): #Retorna el resultado de la sumatoria de la función evaluada en xi + h hasta n-1 veces de impares y pares
    sumI=0
    sumP=0
    for i in range(1,n):
        if i%2!=0:
            #print("Xi impar"+str(xi))
            sumI = sumI + evaluaFuncion(Lista,e,xi)
        else:
            #print("Xi Par"+str(xi))
            sumP = sumP + evaluaFuncion(Lista,e,xi)
        xi= xi + h
    return sumI,sumP

def Simpson3_8(Lista,e,a,b,h): #Función que contiene el procedimiento para calcular la integral por medio de Simpson 3/8
    xi = a+h
    F0 = evaluaFuncion(Lista,e,a)
    F1 = evaluaFuncion(Lista,e,xi)
    xi = xi + h
    F2 = evaluaFuncion(Lista,e,xi)
    F3 = evaluaFuncion(Lista,e,b)
    Resultado = (b-a)*((F0+(3*F1)+(3*F2)+F3)/8)
    return Resultado

def Simpson1_3M(Lista,e,a,b,n,h): #Función que contiene el procedimiento para calcular la integral por medio de Simpson 1/3 Multiple
    F0 = evaluaFuncion(Lista,e,a)
    Fn = evaluaFuncion(Lista,e,b)
    Si,Sp = SumatoriaIP(Lista,e,(a+h),n,h)
    #print("\nSuma impar:"+str(Si)+"\nSuma par:"+str(Sp))
    Resultado = (b-a)*((F0+(4*Si)+(2*Sp)+Fn)/(3*n))
    return Resultado

def Simpson1_3(Lista,e,a,b): #Función que contiene el procedimiento para calcular la integral por medio de Simpson Simple
    F0=evaluaFuncion(Lista,e,a)
    F1=evaluaFuncion(Lista,e,(b+a)/2)
    F2=evaluaFuncion(Lista,e,b)
    Resultado= ((b-a)*(F0+(4*F1)+F2))/6
    return Resultado

def Simpson(Lista,e,a,b,n): #Reglas de simpson de aplicación multiple para segmentos pares e impares
    if n==1: #Simpson 1/3 Simple
        h = (b-a)/2
        I = Simpson1_3(Lista,e,a,b)
        print("\n\t**Metodo Simpson 1/3 simple**")
        print("\n\tEl valor de la integral es: "+str(I))
    elif n%2 ==0: #Par Simpson 1/3 Multiple
        h = (b-a)/n
        I = Simpson1_3M(Lista,e,a,b,n,h)
        print("\n\t**Metodo Simpson 1/3 Multiple**")
        print("\n\tEl valor de la integral es: "+str(I))
    else: #Impar Simpson 3/8
        h = (b-a)/3
        I = Simpson3_8(Lista,e,a,b,h)
        print("\n\t**Metodo Simpson 3/8**")
        print("\n\tEl valor de la integral es: "+str(I))
s=0
while s==0: #Menu principal
    print("\n****Bienvenido al Sistema de Integracion*****")
    opc= int(input("\n1-Metodo Simpson \n2-Salir \n"))
    if opc==1:
        print("De que grado sera su ecuacion: ")
        exponente=int(input())
        if exponente < 0 or exponente > 10 : #Esto es ajustable, el exponente podemos dejar que sea mayor a 10
            print("utilice una ecuacion de grado entre 0 y 10")
        else:
            Lista=generaEcuacion(exponente)
            a = float(input("Lim inferior: "))
            b = float(input("Lim superior: "))
            if b > a:
                n=int(input("\nNumero de segmentos: "))
                if n<1:
                    print("El numero de segmentos debe ser mayor a 0")
                else:
                    Simpson(Lista,exponente,a,b,n)
            else:
                print("El valor del limite superior no puede ser menor al inferior")
    elif opc==2: 
            print("Salida...")
            s=1
            break
print("Fin del programa...")
