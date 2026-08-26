####  Variables  ####
str1= "hola"
str2= "papa"
int1= 15
list1=["bicho", "huevo", 25, "caracol"]
list2= ["manzana", "naranja", 35, "ojo"]
eyes= True
hair= False
floats= 12.33

####   Sumas   ####
print(str1+str2)          # Se unen como si fueran una sola palabra/str
print(str2 + str(int1))   # No se pueden combinar a menos de que ambos sean str
print(str(int1)+str2)     # No se pueden combinar a menos de que ambos sean str
print(list1+list2)        # Se unen como si fueran una sola lista
list1.append(str2)        # El append añade el str dentro de la lista, como si se estuvieran sumando
print(list1)              # Enseña la lista con el str nuevo
print(floats+int1)        # Automaticamente convierte ambos en un float
print(eyes+hair)          # Los convierte a ambos a positivo; osea 1s

#* Si no se hiciera así, darían error al simplemente sumar
#* Aún así tecnicamente sí se estan sumando, ya que sumar es UNIR valores
#* Dan error ya que no son valores compatibles para un simple "+"; por ende hay que buscar otros métodos