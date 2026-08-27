def alphabetize(text):
    text_split=text.split("-") #Corta el str en cada -, y cada corte es un item nuevo de la lista
    text_split.sort() #Ordena alfabéticamente la lista
    new_text="-".join(text_split) #Une la lista con un - en medio de cada elemento (lo une como str)
    print(new_text) 

epic_text="gato-peluca-arroz-basurero-perro-máscara"
print(epic_text)
alphabetize(epic_text)