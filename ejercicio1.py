"""
dibujar la siguiente figura. crear una funcion a la que se le pasa como parametro caracter a imprimir
rango a y el espacio entre caracteres

   *   
   **  
   *** 
*******
 ***   
  **   
   * 


"""



def dibujo(caracter,rango, espacio):
    ran = rango - 1
    for columna in range(rango):
        for fila in range(rango):
            if ( (columna >= fila - ran/2) and (columna <= ran/2 + fila)  and columna >= ran/2 - fila and fila >= ran/2 and columna <= ran/2  or
                 (columna >= fila - ran/2) and (columna <= ran/2 + fila)  and columna >= ran/2 - fila and fila <= ran/2 and columna >= ran/2
    ):
                 
           
      
                print(' ','*', end="")
      

            else:
                print(' ',' ', end="")
        print()
        
def main():
    

    dibujo('*', 13 , ' ')

main()



'''


ok (columna >= fila - 6/2) and (columna <= 6/2 + fila)  and columna >= 6/2 - fila


parte de  abajo????  (columna >= fila - 6/2) and (columna <= 6/2 + fila)  and columna >= 6/2 - fila and fila <= 6/2 and columna = 6/2

parte de arriba ???  (columna >= fila - 6/2) and (columna <= 6/2 + fila)  and columna >= 6/2 - fila and fila >= 6/2 and columna <= 6/2
cruz
columna == 6/2 or fila == 6/2

.........................
columna == 6/2 + fila -- diagonal inferior izquierda

   -     
  -
 -
-
*
 *
  *
   *
    *   
.....................................

(columna == fila - 6/2) diagonal superio derecha

            *
             *
              *
               *
   -            *
    -
     -
      -
       -
------------------------------
fila superior izquierda

   *     columna == 6/2 - fila
  *
 *
*
-
 -
  -
   -
    -  
--------------------
fila inferior derecha

         -
          -
           -
            -
             -
             *                   
            *
           *
          * 
         *
columna + fila  == 6  + 6/2 



'''







        
        
# if(fila == columna or columna + fila == ran or columna == 0 or columna == ran):
'''
 


'''
        


        
   
   
   
   #fila >= columna and fila + columna <=6
