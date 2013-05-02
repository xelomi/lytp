#Nombre: 	Marcelo Minay
#Actividad: Realizar un programa que dado un arreglo de caracteres tome las dos primeras y dos ultimas letras 
#			genere una nueva palabra con estas.

#~~~~~~~~~~~~~~~~~~~~~~~~~~#
#Declaración de funciones
#~~~~~~~~~~~~~~~~~~~~~~~~~~#


def ambos_extremos(n):
    vacio=""
    if len(n)<2:         #verifico si el largo del arreglo es mayor a 2 en caso de ser menor retorno un string vacio
        return vacio
    else:
        return n[0:2] + n[-2] + n[-1]		#Tomar las 2 primeras letras y luego concatenar con las dos últimas

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
