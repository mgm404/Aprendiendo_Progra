str1=" Pan con queso" #Tiene un espacio al inicio si no a la hora de imprimirlo da error

for i in range(len(str1)-1, 0, -1): #El -1 del len es para que no de error y a la vez quita el espacio del str
    print(str1[i])