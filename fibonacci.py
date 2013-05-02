#Nombre: Marcelo Minay
#Actividad: Realizar una función que calcule el termino enesimo de fibonacci.

def fibonacci(n):				#funcion calcula el termino enesimo de forma recursiva
    if(n==0):
        return 0
    else:
        if (n==1):
            return 1
        else:
            return (fibonacci (n-1) + fibonacci (n-2))


def main():
    

    numero=input("Ingrese el termino enesimo de la serie de fibonacci que desea mostrar ")

    a=fibonacci(int(numero))

    print("El termino",numero,"de la serie fibonacci es",a)


    return 0


if __name__ == '__main__':
  main()
