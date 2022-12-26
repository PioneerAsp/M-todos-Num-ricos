## Métodos Numéricos
## Aplicar los métodos de Integración numérica de la regla del trapecio.
## Tipo de método Trapecio simple y multiple
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

def Sumatoria(Lista,e,xi,n,h): #Retorna el resultado de la sumatoria de la función evaluada en xi + h hasta n-1 veces
    sum=0
    for i in range(n-1):
        sum = sum + evaluaFuncion(Lista,e,xi)
        xi= xi + h
    return sum

def TrapecioS(Lista,e,a,b): #Función que contiene el procedimiento de Trapecio Simple
    print("\n***Trapecio Simple***")
    Fa = evaluaFuncion(Lista,e,a)
    Fb = evaluaFuncion(Lista,e,b)
    I  = (b-a)*((Fa+Fb)/2)
    print("\tEl valor de la integral es: "+str(I))

def TrapecioM(Lista,e,a,b,n): #Función que contiene el procedimiento de Trapecio Multiple
    print("\n***Trapecio Multiple***")
    h  = (b-a)/n
    Fa = evaluaFuncion(Lista,e,a)
    Fb = evaluaFuncion(Lista,e,b)
    S  = Sumatoria(Lista,e,(a+h),n,h)
    #print(str(S)) #Imprimir el valor de la sumatoria
    I  = (b-a)*((Fa + (2*S) + Fb)/(2*n))
    print("\tEl valor de la integral es: "+str(I))

def Trapecio(Lista,e,a,b): #Función para tomar la decición de por cual metodo hacer el procedimiento en base al valor de n (segmentos)
    n=int(input("\nNumero de segmentos: "))
    if n==1:
        TrapecioS(Lista,e,a,b)
    elif n > 1:
        TrapecioM(Lista,e,a,b,n)
    else : print("el numero de segmentos debe ser mayor a 0")

s=0
while s==0: #Menu principal
    print("\n****Bienvenido al Sistema de Integracion*****")
    opc= int(input("\n1-Metodo del Trapecio \n2-Salir \n"))
    
    if opc==1:
        print("De que grado sera su ecuacion: ")
        exponente=int(input())
        if exponente < 0 or  exponente > 10 : #Esto es ajustable, el exponente podemos dejar que sea mayor a 10
            print("utilice una ecuacion de grado entre 0 y 10")

        else:
            Lista=generaEcuacion(exponente)
            a = float(input("Lim inferior: "))
            b = float(input("Lim superior: "))
            if b > a:
                Trapecio(Lista,exponente,a,b)
            else:
                print("El valor del limite superior no puede ser menor al inferior")
    
    elif opc==2: 
            print("Salida...")
            s=1
            break
print("Fin del programa...")
