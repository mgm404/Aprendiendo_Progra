keys=['comida', 'origen', 'dificultad_de_hacer']
values=['Pie', 'Egipto', '7/10']

baking_guide={}

for i in range(0, len(keys)):
    baking_guide[keys[i]]=values[i]

print(baking_guide)