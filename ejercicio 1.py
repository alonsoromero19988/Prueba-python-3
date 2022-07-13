# Escribir un programa que escriba 20 numeros aleatorios entre 100 y 1000 en un archivo 
# llamado numeros_prueba.txt. Luego debe leer desde el archivo esos números y agregarlos
# a una lista, modifique o cree una nueva lista que contenga solo los numeros impares. 
# Finalmente con numpy determinar la dimensión de la lista. Imprimir por consola la lista
# final y su dimensión.
import numpy as np
import random
 
def escribir_archivo():
     nombre_fichero = "archivo/numeros_prueba.txt"
     with open(nombre_fichero, "w", encoding="utf-8") as file:   
         for i in range(20):
             numero_aleatorio = random.randint(100, 1000)
             linea = str(numero_aleatorio)
             
             file.write(linea)
             file.write("\n")
 




def leer_numeros():
    numeros=[]
    with open("numeros_prueba.txt", "r") as file:
        for linea in file:
           numeros.append(int(linea))
    num_imp=[]
    for n in numeros:
        if n%2!=0:
            num_imp.append(n) 
    return num_imp                        



def main(): 
     escribir_archivo()
     num_imp=leer_numeros()
     print(num_imp)
     arreglo = np.array(num_imp)
     print(arreglo.ndim)

    
if __name__ == '__main__':
    main()    

