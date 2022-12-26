## Métodos Numéricos
## Método de Jacobi y Gauss Seidel.
## By: PioneerAsp

def imprimeMatriz(Matriz,d): #imprime la matriz generada
    for f in range(d):
        for c in range(d):
            print(Matriz[f][c],end='   ')
        print()

def imprimeListaB(ListaB,d): #Imprime los valores de la lista de resultados
    for i in range(d):
        print("\nResultad de la ecuacion " + str(i+1) + " = " + str(ListaB[i]))

def generaMatriz(d): #Genera la estructura de la matriz
    Matriz=[]
    ListaB=[]
    for i in range(d):
        print("\n***Ecuación numero "+str(i+1)+ "***" )
        Matriz.append([])
        for j in range(d):
            Matriz[i].append(float(input("\nCoeficiente de la incognita "+str(j+1)+ ": ")))
        ListaB.append(float(input("\nResultado de la ecuación N. " +str(i+1)+ ": ")))
    imprimeMatriz(Matriz,d)
    #imprimeListaB(ListaB,d)
    return Matriz,ListaB

def FormX(M,B,y,z): #Formula despejada de X
    Xn =(B[0]-(M[0][1]*y)-(M[0][2]*z))/M[0][0]
    return Xn

def FormY(M,B,x,z): #Formula despejada de Y
    Yn =(B[1]-(M[1][0]*x)-(M[1][2]*z))/M[1][1]
    return Yn

def FormZ(M,B,x,y): #Formula despejada de Z
    Zn =(B[2]-(M[2][0]*x)-(M[2][1]*y))/M[2][2]
    return Zn

def MetodoJacobi(Matriz,B): #Procedimiento para calcular las incognitas x,y,z por M.Jacobi
    lim = int(input("\nLimite de iteraciones deseadas: "))
    Xn= FormX(Matriz,B,0,0)
    Yn= FormY(Matriz,B,0,0)
    Zn= FormZ(Matriz,B,0,0)
    print("\nIteracion: "+str(0) +"\tX: "+str(Xn)+"\tY: "+str(Yn)+"\tZ: "+str(Zn))
    for i in range(lim):
        Xn_1= FormX(Matriz,B,Yn,Zn)
        Yn_1= FormY(Matriz,B,Xn,Zn)
        Zn_1= FormZ(Matriz,B,Xn,Yn)
        print("\nIteracion: "+str(i+1) +"\tX: "+str(Xn_1)+"\tY: "+str(Yn_1)+"\tZ: "+str(Zn_1))
        Xn= Xn_1
        Yn= Yn_1
        Zn= Zn_1

def MetodoGSaidel(Matriz,B): #Procedimiento para calcular las incognitas x,y,z por M.Gauss Seidel
    lim = int(input("\nLimite de iteraciones deseadas: "))
    Xn= FormX(Matriz,B,0,0)
    Yn= FormY(Matriz,B,0,0)
    Zn= FormZ(Matriz,B,0,0)
    print("\nIteracion: "+str(0) +"\tX: "+str(Xn)+"\tY: "+str(Yn)+"\tZ: "+str(Zn))
    for i in range(lim):
        Xn= FormX(Matriz,B,Yn,Zn)
        Yn= FormY(Matriz,B,Xn,Zn)
        Zn= FormZ(Matriz,B,Xn,Yn)
        print("\nIteracion: "+str(i+1) +"\tX: "+str(Xn)+"\tY: "+str(Yn)+"\tZ: "+str(Zn))

def validacionMatriz(Matriz,d): #Procedimiento para validar que no haya 0 en la diagonal
    for i in range(d):   
        if Matriz[i][i] == 0:
            return False
    return True

s=0
while s==0: #Menú
    print("\n****Bienvenido al Sistema de Jacobi y G.Seidel *****")    
    print("\n1-Jacobi. \n2-Gauss Saidel. \n3-Salir")
    opc = int(input())
    d=3
    if opc==1:
        Matriz,B=generaMatriz(d) 
        v = validacionMatriz(Matriz,d)
        if v == False:
            print("No es posible reaizar este método mientras haya una incoginita en la diagonal con 0")
        else:
            MetodoJacobi(Matriz,B)
        
    elif opc==2:
        Matriz,B=generaMatriz(d) 
        v = validacionMatriz(Matriz,d)
        if v == False:
            print("No es posible reaizar este método mientras haya una incoginita en la diagonal con 0")
        else:
            MetodoGSaidel(Matriz,B)
    elif opc==3: 
        print("Salida...")
        s=1
        break
print("Fin del programa...")