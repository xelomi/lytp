#Nombre: Marcelo Minay
#Actividad: Realizar una función que calcule el factorialde un numero


def factorial(n):   #funcion que calcula el factorial.
    resultado=1
    if n==0:
        return 1
    else:
        while n!=0:
            resultado=resultado*n
            n=n-1
    return resultado

def main():
    fact=input("Ingrese el numero ")

    factresult=factorial(int(fact))

    print("El factorial de",fact,"es",factresult)

    return 0

if __name__ == '__main__':
    main()
