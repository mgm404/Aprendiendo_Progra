import os

start="si"

while start=="si" or start=="s" or start=="sí":

    os.system('cls' if os.name == 'nt' else 'clear') #** Borra la terminal cuando se inicia

    #** Ingreso de información
    print(" ---- Verificación de etapa de vida ----")
    name=input(" -- ¿Cúal es tu primer nombre? \n -- ")
    last_name=input(" -- ¿Y tu primer appelido? \n -- ")
    age=int(input(" -- ¿Cúal es tu edad? \n -- "))

    life_stage=""

    #** Verificaciones
    if age>=0 and age<=3:
        life_stage="bebé"
    elif age>=4 and age<=10:
        life_stage="niñ@"
    elif age>=11 and age<=13:
        life_stage="preadolecente"
    elif age>=14 and age<=17:
        life_stage="adolecente"
    elif age>=18 and age<=29:
        life_stage="adult@ joven"
    elif age>=30 and age<=59:
        life_stage="adult@"
    elif age>=60:
        life_stage="adult@ mayor"
    else:
        print(" ---- Error -- Edad incalculable ----")
    #** Fin verificaciones

    print(f" ---- ¡{name} {last_name} es un {life_stage}! ----")
    start=input(" -- ¿Desea volver a verificar?(s/n) \n -- ").lower() #** El .lower() hace que el input se vuelva lowercase