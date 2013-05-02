#Nombre: 		Marcelo Minay
#Actividad: 	Se debe realizar un programa que cálcule el valor de una combinatoria


def factorial(n):				#funcion que determina el factorial de un numero.
    resultado=1
    if n==0:
        return 1
    else:
        while n!=0:
            resultado=resultado*n
            n=n-1
    return resultado

#Funcion que retorna el resultado del coeficiente binominal
def combinatoria(n,k):
	#factorial n-k
    parentesis=factorial(n-k)

    #Calcula el factorial de n
    facn=factorial(n)
        
    #Calcula el factorial de k
    fack=factorial(k)
    #Retorna el resultado de n!/((n-k)!*k)
    return facn/(parentesis*fack)

def main():

    #Ingreso de los valores de n y k
    n=input("Ingrese el termino 'n' del numero combinatorio ")
    k=input("Ingrese el termino 'k' del numero combinatorio ")

    #Comprueba que k sea mayor que 0
    if int(k)<0:
        print("el termino 'k' tiene que ser mayor a 0")
    
    else:
        #Comprueba que k sea menor que n
        if int(k)>int(n):
            print("el termino 'k' debe ser menor o igual al termino 'n'")

        #Imprime el resultado de la operacion solo si las condiciones de arriba de cumplen
        else:
            print("El numero combinatorio es",combinatoria(int(n),int(k)))



    return 0


if __name__ == '__main__':
  main()
