for  fila in range(7):
    for columna in range(7):
        if(fila <= columna and fila + columna <= 6 or fila >= columna and fila+columna >=6) :
           
           print('*', end="")
            
        else:
            print(' ', end="")
    
    print()
    
    
    
'''
triangulo abajo


   *   
  ***  
 ***** 
*******

columna >= 6 -fila and columna >= fila





'''