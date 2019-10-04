def dibujar(caracter,b):

    for fila in range(b):
        for columna in range(b):
            if(columna <= fila and fila + columna >=  b-1 and columna <= (b-1)/2 or 
columna+fila == (b-1)  or fila <= (b-1)/2 and columna == fila):
                print(caracter, end=""   )
            else:
                print(' ', end="")
                
        print()
        
def main():
    
    dibujar('*',11 )
    
    
main()


'''

columna+fila == (b-1)  or fila <= (b-1)/2 and columna == fila

fila <= (b-1)/2 and columna == fila 
'''