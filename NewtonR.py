## Métodos Numéricos - Newton Raphson
## By:PioneerAsp

def generaEcuacion(n):
    m=n
    Lista =[]
    for i in range(n+1):
        Lista.append(float(input("Coeficiente de x^"+str(m)+": ")))
        m= m-1
        print(i)
    return Lista

def derivaEcuacion(lista,n):
    m=n
    ListaD =[]
    #auxD=0
    for i in range(n):
        ListaD.append(float(Lista[i]*(m-i)))
        print(i)
    return ListaD

def evaluaFuncion(Lista,exponente,a):
    n=exponente
    sum=0
    for i in range(exponente+1):
        aux=Lista[i]
        sum= sum + (aux*(a**(n-i)))
        #print (sum)
    return sum

def NewtonR(Lista, exponente):
    m=exponente
    xi=float(input("Valor de Xi: "))
    fxi=evaluaFuncion(Lista,exponente,xi)
    ListaD=derivaEcuacion(Lista,m)
    print(ListaD)
    m=m-1
    fxid=evaluaFuncion(ListaD,m,xi)
    lim=int(input("Limite de iteracion: "))
    print("Iteracion: "+str(0) +"\tXi: "+str(xi)+"\tfxi: "+str(fxi)+"\tf(xi)d: "+str(fxid)+"\n")
    for i in range(lim):
        xia=xi
        xi=(xi-(fxi/fxid))
        fxi=evaluaFuncion(Lista,exponente,xi)
        fxid=evaluaFuncion(ListaD,m,xi)
        ea=(abs((xi-xia)/xi)*1)  #Error aproxima = (|(Aprox.actual-Aprox.atnerior)/Aprox.actual|*1) 1=100%
        print("Iteracion: "+str(i+1) +"\tXi: "+str(xi)+"\tfxi: "+str(fxi)+"\tf(xi)d: "+str(fxid)+"\tea: "+str(ea)+"\n")
        if ea ==0:
            break
    print("\nXi calculada (aproximacion)= "+str(xi))

#Inicia#
s=0
while s==0:
    print("****Bienvenido al Sistema de raices*****")
    print("De que grado sera tu ecuacion: ")
    exponente=int(input())

    if exponente < 0 or  exponente > 10 :
        print("utilice una ecuacion de grado entre 0 y 10")

    else:
        Lista=generaEcuacion(exponente)
        
    print("\nQue tipo de metodo utilizara \n 1-NewtonR  \n 2-Salir")
    opc = int(input())
    if opc==1:
        print("Opcion 1")
        NewtonR(Lista, exponente)

    elif opc==2: 
        print("Salida...")
        s=1
        break
print("Fin del programa...")
