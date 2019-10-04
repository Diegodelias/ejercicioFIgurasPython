def dibujo(caracter,rango):
    ran = rango -1

    for fila in range (rango):
        for columna in range(rango):
            if(fila == columna or fila + columna == ran or fila <= columna and fila + columna <= ran):
                
                print('*' , end=" ")
            else:
                print(' ', end=" ")
                
        print()
        

def main():
    
    dibujo('*' , 11)
    
main()


'''
triangulo de arriba
fila <= ran /2  and columna + fila >= ran /2  and  columna <= ran /2 + fila
          *           
        * * *         
      * * * * *       
    * * * * * * *     
  * * * * * * * * *   
* * * * * * * * * * * 


     columna >= ran / 2  and fila <= ran /2  
     

rectangulo abajo

columna ==0 and  fila > ran /2 and columna <= ran /2  or columna == ran and fila > ran/2 or fila == ran /2 or fila == ran
     
     



          *           
          * *         
          *   *       
          *     *     
          *       *   
* * * * * * * * * * * 
          *           
          *           
          *           
          *
          
           columna == ran /2 + fila
          *           
     
               *           
        * *           
      *   *           
    *     *           
  *       *           
* * * * * * * * * * * 
          *           
          *           
          *           
          *    
     
    columna + fila == ran /2   
'''