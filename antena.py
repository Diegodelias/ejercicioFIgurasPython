def dibujar(caracter,b, espacio):

    for fila in range(b):
        for columna in range(b):
            if(columna <= fila and fila + columna >=  b-1 and columna <= (b-1)/2 or 
columna+fila == (b-1)  or fila <= (b-1)/2 and columna == fila):
                print(espacio , caracter, end=""   )
            else:
                print(espacio, ' ', end="")
                
        print()
        
def main():
    
    dibujar('*',11, ' ' )
    
    
main()


'''

columna+fila == (b-1)  or fila <= (b-1)/2 and columna == fila

fila <= (b-1)/2 and columna == fila 
'''