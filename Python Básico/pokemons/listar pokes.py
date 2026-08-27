import json
import os
import time
from pathlib import Path #** Ayuda a importar archivos

def saving(pokemon, pokedex):
    print(f"(o˘◡˘o) : Esta bien! Ahora voy a guardar tu pókemon en la pokedex!")

    pokemons=read_pokedex(pokedex)

    pokemons.append(pokemon)

    with pokedex.open('w') as file:
        json.dump(pokemons, file, indent=4)
    
    time.sleep(3)

    print(f"ヽ(*⌒▽⌒*)ﾉ : Yippie! \n(〃＾▽＾〃) : Ya quedo guardado tu {pokemon["name"]}")
    
    time.sleep(5)
    exit()  #! Si no se sale se devuelve a poke_stats y da error

def poke_stats(pokemon, pokedex):
    stats={}

    try:
        stats['hp']= int(input("\n<(￣︶￣)> : ¿Cúanta vida(hp) tiene? \n -"))
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no es un número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        poke_stats(pokemon, pokedex)

    try:
        stats['attack']= int(input("\n<(￣︶￣)> : ¿Cúanto ataque tiene? \n -"))
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no es un número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        poke_stats(pokemon, pokedex)

    try:
        stats['defense']= int(input("\n<(￣︶￣)> : ¿Cúanta defensa tiene? \n -"))
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no es un número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        poke_stats(pokemon, pokedex)

    try:
        stats['sp_attack']= int(input("\n<(￣︶￣)> : ¿Cúanto ataque especial tiene? \n -"))
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no es un número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        poke_stats(pokemon, pokedex)

    try:
        stats['sp_defense']= int(input("\n<(￣︶￣)> : ¿Cúanta defensa especial tiene? \n -"))
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no es un número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        poke_stats(pokemon, pokedex)

    try:
        stats['speed']= int(input("\n<(￣︶￣)> : ¿Cúanta velocidad tiene? \n -"))
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no es un número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        poke_stats(pokemon, pokedex)
    
    pokemon["stats"]=stats

    saving(pokemon, pokedex)


def poke_skills(pokemon, pokedex):
    skills=[]
    skill_num=0 #El número de habilidades que tenga el pókemon

    try:
        skill_num= int(input(f"\n(・u・) ? : Cuantos movimientos tiene tu {pokemon["name"]} \n -"))

        if skill_num<0 or skill_num>4:
            raise ValueError()
    except ValueError as error: #* Sale si no esta entre 0-4 y si no es num
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no cuenta como número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        poke_skills(pokemon, pokedex)

    if skill_num>0: #*Mientras haya mínimo un movimiento, si no crashea
        for i in range(0, skill_num):
            skill=input(f"(｡•ᴗ•｡) : Movimiento {i+1}\n -")
            skills.append(skill)

    pokemon["skills"]=skills

    poke_stats(pokemon, pokedex)


def pokemon_to_save(pokedex):
    os.system('cls' if os.name == 'nt' else 'clear')
    pokemon={}
    types=[]
    
    print(f"(｡•ᴗ•｡) : Ahora voy a registrar tu pókemon \n")

    pokemon['name']= input("<(￣︶￣)> : Dime el nombre de tu pókemon \n -")

    poke_type=input("\n(・u・) ? : ¿Tiene más de un solo tipo? (S/N) \n -").lower()
    try:
        if poke_type=="si" or poke_type=="s" or poke_type=="sí":

            type1=input("\n<(￣︶￣)> : Dime el primer tipo del pókemon \n -")
            type2=input("\n<(￣︶￣)> : Dime el segundo tipo del pókemon \n -")
            types.append(type1)
            types.append(type2)
            pokemon['type']=types

        elif poke_type=="no" or poke_type=="n":
            pokemon['type']= input("\n<(￣︶￣)> : Dime el tipo del pókemon \n -")
        else:
            raise ValueError()
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- Solo se puede sí o no!! ٩(ఠ益ఠ)۶ --- \n---  DETALLES: Tu respuesto no fue sí, ni no; pusiste {is_shiny} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        pokemon_to_save(pokedex)


    try:
        pokemon['level']= int(input("\n<(￣︶￣)> : Dime su nivel \n -"))
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no es un número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        pokemon_to_save(pokedex)

    try:
        pokemon['weight_kg']= float(input("\n<(￣︶￣)> : Dime su peso en kg \n -"))
    except ValueError as error:
            print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no es un número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
            time.sleep(5)
            pokemon_to_save(pokedex)


    is_shiny= input("\n(・u・) ? : ¿Es shiny? (S/N) \n -").lower()
    try:
        if is_shiny=="si" or is_shiny=="s" or is_shiny=="sí":
            pokemon['is_shiny']=True
        elif is_shiny=="no" or is_shiny=="n":
            pokemon['is_shiny']=False
        else:
            raise ValueError()
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- Solo se puede sí o no!! ٩(ఠ益ఠ)۶ --- \n---  DETALLES: Tu respuesto no fue sí, ni no; pusiste {is_shiny} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        pokemon_to_save(pokedex)

    has_item= input("\n(・u・) ? : ¿Tiene algún objeto en la mano? (S/N)\n -")
    try:
        if has_item=="si" or has_item=="s" or has_item=="sí":
            pokemon['held_item']=input("\n(・u・) ? : ¿Cúal es el objeto?\n -")
        elif has_item=="no" or has_item=="n":
            pokemon['held_item']=None
        else:
            raise ValueError()
    except ValueError as error:
        print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- Solo se puede sí o no!! ٩(ఠ益ఠ)۶ --- \n---  DETALLES: Tu respuesto no fue sí, ni no; pusiste {is_shiny} \n---  Reiniciando (`ー´)")
        time.sleep(5)
        pokemon_to_save(pokedex)

    poke_skills(pokemon, pokedex)



def read_pokedex(pokedex):
    with pokedex.open('r') as file:
        pokemons= json.load(file)
    return pokemons



def main(pokedex):
    os.system('cls' if os.name == 'nt' else 'clear')

    pokemons=read_pokedex(pokedex)

    print("(>ᴗ<) : Vamos a gurdar un pókemon nuevo a tu equipo, de momento tienes a:")
    for pokemon in pokemons:
        print(f"° {pokemon["name"]}, nivel {pokemon["level"]}")

    time.sleep(10)
    pokemon_to_save(pokedex)

if __name__=='__main__':
    pokedex= Path(__file__).parent / 'pokedex.json' #** importa el archivo al estar separado
    main(pokedex)

