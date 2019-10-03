
'''
dibujar rectangulo rectangulo pintado por la mitad. hacer funcion y pasarle  como argumento caracter a imprimir , espacio y cantidad de caracteres

  *  *  *  *  *  *  *
  *  *  *  *        *
  *  *  *  *        *
  *  *  *  *  *  *  *
                     
                     
                     
'''







def dibujar(caracter,rango):
    
    ran = rango -1
    ranfila = ran / 2
   
    for fila in range(rango):
        for columna in range(rango):
            if(fila == 0  or fila == ranfila  or  columna == 0  and columna >= fila - ranfila or columna == ran and columna >= columna + fila - ranfila or columna ==
               ranfila and columna >= columna + fila - ranfila  or columna <= ranfila and fila <= ranfila):    
                print(' ','*' , end="")
            
            else:
                print(' ',' ', end="")
        print()


def main():
    
    dibujar('*', 31)
    
main()



    
'''

linea horizontal superior

--------------------
columna == 0

linea horizontal inferior
columna == 12/3

????????????????????



--------------------


linea vertical izquierda:


-                         ?
-                         ?
-                         ?
-                         ?
-                         ? 
-                         ?
-

 fila == 0 and fila >= columna - 12/3
 
 
 linea vertical derecha
 
 ?                          -         fila == 12 and fila >= columna +fila - 12/3    
 ?                          -
 ?                          -
 ?                          -
 ?                          -



'''