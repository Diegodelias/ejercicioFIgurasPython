def dibujar(c,b):

    for fila in range(b):
        for columna in range(b):
            if( fila >= (b-1)/2 and
 fila >= columna  and fila + columna >=  b-1  and  columna <= (b-1)/2
                or fila == columna or columna + fila == (b-1)  and columna >= (b-1)/2 and fila <= (b-1)/2
                
              and  fila <= (b-1)/2): 
                print('*',end="")   
            else:
                print(' ', end="")
        
        print()



def main():
    
    dibujar('*', 19)

main()


'''


 fila >= columna  and fila + columna >=  b-1  and  columna <= (b-1)/2
                or fila == columna or columna + fila == (b-1)  and columna >= (b-1)/2 and fila <= (b-1)/2
                
              and  fila <= (b-1)/2

'''