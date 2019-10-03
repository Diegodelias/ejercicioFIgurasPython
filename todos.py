def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if( columna == fila or fila + columna  == ran or fila == 0 or fila  == ran or  fila >= (int(ran * 0.80)) and columna + fila >= ran and fila >= columna
               or columna == ran/2  and fila >= ran /2 or fila <= int(0.25 *ran) and columna+fila <= ran and fila <= columna ):
                 print('*' , end=" ")
            else:
                print(' ', end=" ")
        print()
   


def main():


    dibujar('*', 15)

main()




'''
temp  columna == fila or fila + columna  == ran or fila == 0 or fila  == ran or 

1/2

1/2 de ran
3/4 de ran
def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if(  columna == fila or fila + columna  == ran or columna == 0 or columna == ran

):
                print('*' , end=" ")
            else:
                print(' ', end=" ")
        print()
   




triangulo arriba

            *             
            * *           
            * * *         
            * * * *       
            * * * * *     
            * * * * * *   
            * * * * * * *
            
triangulo abajao

                          
* * * * * * *             
  * * * * * *             
    * * * * *             
      * * * *             
        * * *             
          * *             
            *  

columna >=  fila - ran/2   and columna <= ran /2 and fila >= ran/2
            
triangulo abajo
            
            

columna == ran /2  and fila == ran /2  or columna  <= ran  /2 + fila and fila <= ran /2 and columna >= ran /2


ok  columna >= fila - ran  /2  and  columna  <= ran  /2 + fila  

>

            *             
            * *           
            *   *         
            *     *       
            *       *     
            *         *   
* * * * * * * * * * * * * 
            *             
            *             
            *             
            *             
            *             
            *          columna  == ran  /2 + fila
 ):














  or columna + fila <= ran + ran/2
               
               or columna >=  fila - ran/2









cruz columna == ran /2  or fila == ran /2  

lineas rombo

           *         

        *  *         

     *     *         

  *  *  *  *  *  *  *

           *         

           *         

           *         
 columna+fila == ran /2

        *      

        *  *   

  *  *  *  *  *

        *      

        *
        
        columna == ran /2 + fila


            *             
            *             
            *             
            *             
            *             
            *             
* * * * * * * * * * * * * 
  *         *             
    *       *             
      *     *             
        *   *             
          * *             
            *
                        
columna ==  fila - ran/2   
            
            
            *
            
            *             
            *             
            *             
            *             
            *             
* * * * * * * * * * * * * 
            *         *   
            *       *     
            *     *       
            *   *         
            * *           
            *        
columna + fila == ran + ran/2


cuadrado vacio


  *  *  *  *  *  *  *  *
  *                    *
  *                    *
  *                    *
  *                    *
  *                    *
  *                    *
  *  *  *  *  *  *  *  *
  
  

columna == 0  or columna == ran or fila == 0 or fila == ran

triangulito


 *  *  *  *  *

    *  *  *  *

        *  *  *

           *  *

              *
              
def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if(fila <= columna):
                print(' ','*' , end="")
            else:
                print(' ',' ', end="")
        print()
        print()


def main():


esta cosa



  *  *  *  *  *  *  *

     *  *  *  *  *   

        *  *  *      

           *         

        *  *  *      

     *  *  *  *  *   

  *  *  *  *  *  *  *
  
  def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if(fila <= columna and fila + columna <= ran or fila >= columna and fila + columna >= ran):
                print(' ','*' , end="")
            else:
                print(' ',' ', end="")
        print()
        print()
    
    
    esto
    
           *         

           *         

           *         

  *  *  *  *  *  *  *

        *  *  *      

     *  *  *  *  *   

  *  *  *  *  *  *  *

        
def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if(fila == ran /2 or columna == ran /2 or  fila >= columna and  fila + columna >= ran):
                print(' ','*' , end="")
            else:
                print(' ',' ', end="")
        print()
        print()




esta otra cosa


  *  *  *  *  *  *  *

     *           *   

        *     *      

           *         

        *     *      

     *           *   

  *  *  *  *  *  *  *

>>> 


def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if(fila == columna  or fila + columna == ran or fila == 0 or fila == ran):
                print(' ','*' , end="")
            else:
                print(' ',' ', end="")
        print()
        print()
        


    *     
  *   *   
*       * 
  *   *   
    *     

def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if( columna+fila == ran /2  or  columna == ran /2 + fila or columna + fila == ran + ran/2
               
               or columna ==  fila - ran/2
 ):
                print('*' , end=" ")
            else:
                print(' ', end=" ")
        print()



      *      
     ***     
    *****    
   *******   
  *********  
 *********** 
*************
 *********** 
  *********  
   *******   
    *****    
     ***     
      *
      
      def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if( columna+fila >= ran /2  and  columna<=ran /2 + fila  and columna + fila <= ran + ran/2
               
               and columna >=  fila - ran/2
 ):
                print('*' , end="")
            else:
                print(' ', end="")
        print()
        

*************
****** ******
*****   *****
****     ****
***       ***
**         **
*           *
**         **
***       ***
****     ****
*****   *****
****** ******
*************

def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if( columna+fila <= ran /2  or  columna>=ran /2 + fila or columna + fila >= ran + ran/2 or  columna <=  fila - ran/2
 ):
                print('*' , end="")
            else:
                print(' ', end="")
        print()
   
   


            *             
            * *           
            *   *         
            *     *       
            *       *     
            *         *   
* * * * * * * * * * * * * 
  *         *             
    *       *             
      *     *             
        *   *             
          * *
            *         
   
   def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if( columna == ran /2  or fila == ran /2 or columna == fila - ran  /2  or  columna  == ran  /2 + fila
 ):
                print('*' , end=" ")
            else:
                print(' ', end=" ")
        print()
   
            *             
            * *           
            * * *         
            * * * *       
            * * * * *     
            * * * * * *   
* * * * * * * * * * * * * 
  * * * * * *             
    * * * * *             
      * * * *             
        * * *             
          * *             
            *    
def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if(  columna >=  fila - ran/2   and columna <= ran /2 and fila >= ran/2  or columna  <= ran  /2 + fila and fila <= ran /2 and columna >= ran /2

):
                print('*' , end=" ")
            else:
                print(' ', end=" ")
        print()
   

esta cosa

* * * * * * * * * * * * * * * 
  * * * * * * * * * * * * *   
    * * * * * * * * * * *     
      * * * * * * * * *       
        *           *         
          *       *           
            *   *             
              *               
            * * *             
          *   *   *           
        *     *     *         
      * * * * * * * * *       
    * * * * * * * * * * *     
  * * * * * * * * * * * * *   
* * * * * * * * * * * * * * *

def dibujar(caracter,rango):
    ran = rango -1
    
    for fila in  range(rango):
        for columna in range(rango):
            if( columna == fila or fila + columna  == ran or fila == 0 or fila  == ran or  fila >= (int(ran * 0.80)) and columna + fila >= ran and fila >= columna
               or columna == ran/2  and fila >= ran /2 or fila <= int(0.25 *ran) and columna+fila <= ran and fila <= columna ):
                 print('*' , end=" ")
            else:
                print(' ', end=" ")
        print()
   


'''
