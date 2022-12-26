## Métodos Numéricos - Matriz inversa
## By:PioneerAsp

def imprimeMatriz(Matriz,d): #imprime una matriz junto con su extención de matriz aumentada
    for f in range(d):
        for c in range(d*2):
            print(Matriz[f][c],end='   ')
        print()
    
def imprimeMatrizD(Matriz,d): #Imprime la matriz que se genero al inicio
    for f in range(d):
        for c in range(d):
            print(Matriz[f][c],end='   ')
        print()

def imprimeListaB(ListaB,d): #Imprime los valores de la lista de resultados
    for i in range(d):
        print("\nResultad de la ecuacion " + str(i+1) + " = " + str(ListaB[i]))

def TransladoM(Matriz,d,B): #Es utilizado para trasladar las filas y detectar errores
    ListaAux=[]
    ListaAuxB=[]
    c=0
    for j in range(d):
        if Matriz[j][j]==0:
            if c>1:
                break
            else :
                #print("Si es igual 0, Trasladenme de fila pls.")
                for i in range(d):
                    if Matriz[i+1][j]!=0:
                        for k in range(d):
                            ListaAux.append(Matriz[j][k])
                            ListaAuxB.append(B[k])
                            #print (ListaAux)
                            #print (ListaAuxB)
                            B[k] = B[i+1]
                            #print (B)
                            B[i+1]= ListaAuxB[k]
                            #print (B)
                        for k in range(d):
                            Matriz[j][k]=Matriz[i+1][k]
                            #print(Matriz[j][k])
                            Matriz[i+1][k] = ListaAux[k]
                            c=c+1
                    else:
                        print("***No es posible resolver este sistema de ecuaciones***")
                    break
    return Matriz

def TransformarUno(MatrizA,d,i,aux): #Método para convertir en 1's
    for k in range(d*2):
        MatrizA[i][k] = MatrizA[i][k]/aux
        #print(str(MatrizA[i][k]))

def TransformarZero(MatrizA,d,i,j,aux): #Método para convertir en 0's
    for k in range(d*2):
        MatrizA[i][k] = ((-1)*aux*MatrizA[j][k]) + MatrizA[i][k]
        #print(str(MatrizA[i][k]))

def generaMatriz(d): #Genera la estructura de la matriz
    Matriz=[]
    ListaB=[]
    for i in range(d):
        print("\n***Ecuación numero "+str(i+1)+ "***" )
        Matriz.append([])
        for j in range(d):
            Matriz[i].append(float(input("\nCoeficiente de la incognita "+str(j+1)+ ": ")))
        ListaB.append(float(input("\nResultado de la ecuación N. " +str(i+1)+ ": ")))
    #imprimeMatriz(Matriz,d)
    #imprimeListaB(ListaB,d)
    return Matriz,ListaB

def Resultado(MatrizF,d,B): #Imprime los resultados finales de las incognitas
    print("\n\t***Resultadossss***")
    for i in range(d):
        sum=0
        for j in range(d,d*2):
            sum= sum + (MatrizF[i][j]*B[j-d])
        print("\n\t***La incognita N."+str(i+1)+" es: "+ str(sum))

def generaMatrizA(Matriz,d): #Genera la matriz Aumentada
    MatrizA=[]
    d2 = 2*d
    for i in range(d):
        MatrizA.append([])
        for j in range(d2):
            if j < d:
                MatrizA[i].append(Matriz[i][j])
            else: 
                if i==(j-d):
                    v=1
                else:
                    v=0
                MatrizA[i].append(v)
    print("\n***La matriz Aumentada***")
    imprimeMatriz(MatrizA,(d))
    return MatrizA

def MetodoMAumentada(MatrizA,B,d): #Todo el proceso en el que se mandan a llamar las demás funciones 
    for j in range(d):
        for i in range(d):
            if i==j:
                if MatrizA[i][j] != 1:
                    aux = MatrizA[i][j]
                    TransformarUno(MatrizA,d,i,aux)
                    #imprimeMatriz(MatrizA,d)
            else:
                if MatrizA[j][j]==1:
                    aux = MatrizA[i][j]
                    TransformarZero(MatrizA,d,i,j,aux)
                    #imprimeMatriz(MatrizA,d)
                else :
                    aux = MatrizA[j][j]
                    TransformarUno(MatrizA,d,j,aux)
                    aux = MatrizA[i][j]
                    TransformarZero(MatrizA,d,i,j,aux)
                    #imprimeMatriz(MatrizA,d)
    return MatrizA

s=0
while s==0: #Menú
    print("\n****Bienvenido al Sistema de Matriz *****")    
    print("\n1-Matriz Inversa (M.M_aumentada). \n2-Salir.")
    opc = int(input())
    if opc==1:
        print("Opcion 1")
        print("De que dimensiones será su Matriz: ")
        d=int(input())
        if d < 0 or  d >10 :
            print("Este programa esta habilitado solo para manejar 10 incognitas...")

        else:
            Matriz,B=generaMatriz(d) 
            TransladoM(Matriz,d,B)
            MatrizA=generaMatrizA(Matriz,d)
            MetodoMAumentada(MatrizA,B,d)
            Resultado(MatrizA,d,B)
    elif opc==2: 
        print("Salida...")
        s=1
        break
print("Fin del programa...")