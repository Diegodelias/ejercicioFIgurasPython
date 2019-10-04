def dibujo(caracter,rango):
    ran = rango -1

    for fila in range (rango):
        for columna in range(rango):
            if(  fila == 0 or fila == ran or columna == 0 or columna == ran or columna <= ran /2 and fila >= ran/2 or columna >= ran / 2  and fila <= ran /2
):
                print('*' , end=" ")
            else:
                print(' ', end=" ")
                
        print()
        

def main():
    
    dibujo('*' , 11)
    
main()


'''
     columna >= ran / 2  and fila <= ran /2  
     
     




     
'''