def dibujar(caracter,rango):
    ran = rango -1
    for fila in range(rango):
        for columna in range(rango):
            if (fila == columna or fila + columna == ran or fila == 0 or fila == ran):
                print('*' , end="")
            
            else:
                print(' ', end="")
        print()



def main():

    dibujar('*',11)

main()