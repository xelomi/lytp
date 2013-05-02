#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#


def ambos_extremos(n):
    vacio=""
    if len(n)<2:
        return vacio
    else:
        return n[0:2] + n[-2] + n[-1]

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funcion principal
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
       

def main():

    palabra=input("INGRESE PALABRA: ")

    aux=ambos_extremos(palabra)

    print (aux)

    return 0

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Identificador del main
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
if __name__ == '__main__':
  main()
#~~~~~~~~~~~~~~~~~~~~~~~~~~#
