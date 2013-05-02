def fibo(n):
    if(n==0):
        return 0
    else:
        if (n==1):
            return 1
        else:
            return (fibo (n-1) + fibo (n-2))


def main():
    

    num=input("Ingrese el numero del termino de la serie fibonacci que desea mostrar ")

    a=fibo(int(num))

    print("El termino",num,"de la serie fibonacci es",a)


    return 0


if __name__ == '__main__':
  main()
