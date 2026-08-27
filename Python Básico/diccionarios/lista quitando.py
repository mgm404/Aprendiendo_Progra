eliminate=['dueño', 'home', 'number',]

pets={
    'name':'Perla',
    'species': 'Gato',
    'owner':'Carlos',
    'home':'San José',
    'number':152,
    'diet':'comida suave',
    'age':10
}

print(f"Antes: \n{pets}")

for k in eliminate: #** Pasa por cada elemento de eliminate y los pone en k
    pets.pop(k, None) #** Si k se encuentra en pets, lo elimina, si no, no hace nada
    #* Pasa por cada key de pets, verificando si sí se encuentra

print(f"Después: \n{pets}")


#** Código que me encontre en Stack OverFlow

#* d = {'some': 'data'}}
#* entries_to_remove = ('any', 'iterable')
#* for k in entries_to_remove:
#*     d.pop(k, None)