#Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.

list1=[1, 2, 3, 4, 5, 66, 7, 8, 9, 5, 5, 8, "pera"]

first=list1[0]
last=list1[len(list1)-1] #El -1 quita error de fuera de rango

print(list1)

list1.pop(0)
list1.pop(len(list1)-1) #El -1 quita error de fuera de rango

list1.append(first)
list1.insert(0, last)

print(list1)