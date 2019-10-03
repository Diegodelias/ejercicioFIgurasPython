def dibujar(caracter,rango):
    ran = rango-1
    for  fila in range(rango):
        for columna in range(rango):
            if(fila <= columna and fila + columna <= ran or fila >= columna and fila+columna >=ran) :
               
               print('*', end="")
                
            else:
                print(' ', end="")
        
        print()
    
    

def main():
    
    dibujar('*',21)
    
main()  



