import csv
import os
import time

def save_games_list(saved, games):
        
        with open(saved, 'w', encoding='utf-8', newline='') as csvfile:
            headers = games[0].keys()

            writer = csv.DictWriter(csvfile, fieldnames=headers, delimiter='\t') #**\t es tab

            writer.writeheader()

            writer.writerows(games)

        time.sleep(5)

        print("ヽ(*⌒▽⌒*)ﾉ : Yippie! \n(〃＾▽＾〃) : Ya quedo guardada tu lista de juegos! Busca el archivo 'list of games.csv'")

        time.sleep(7)
        exit()  #! Si no se sale se devuelve a list_games y da error


def list_games(number_of_games):
    os.system('cls' if os.name == 'nt' else 'clear')
    games=[]

    print(f"(⌒ω⌒) : Ahora listemos los {number_of_games} juegos que escojiste \n\n")

    for i in range(0, number_of_games):
        print(f"(｡•ᴗ•｡) : Juego número {i+1} \n")

        one_game={}
        esrb=""

        one_game['name']= input("<(￣︶￣)> : Dime el nombre del juego \n -")
        one_game['genre']= input("\n<(￣︶￣)> : Dime el género del juego \n -")
        one_game['developer']= input("\n<(￣︶￣)> : Dime el desarrollador del juego: \n -")

        try:
            esrb= input("\n<(￣︶￣)> : Dime la clasificación del juego (solo: E, E +10, T, M, A): \n -").upper()
            if esrb=="E" or esrb=="E +10" or esrb=="E+10" or esrb=="T" or esrb=="M" or esrb=="A":
                one_game['esrb']=esrb
            else:
                raise ValueError()
        except ValueError as error:
            print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no es alguno de los siguientes: E, E +10, T, M, A ٩(ఠ益ఠ)۶ --- \n---  DETALLES: SOLO puede ingresar E, E +10, T, M, A \n---  Reiniciando (`ー´)")
            time.sleep(5)
            list_games(number_of_games)

        games.append(one_game)

    print(f"(o˘◡˘o) : Esta bien! Ahora voy a guardar tus {number_of_games} juegos!")
    save_games_list('list of games.csv', games)

    

def main():
    os.system('cls' if os.name == 'nt' else 'clear')

    number_of_games=0

    print("ヽ(・∀・)ﾉ : Vamos a guardar una lista de juegos que te interesen ")
    print("╮(￣ω￣)╭ : Primero, ¿cuantos juegos quieres guardar? ")
    try:
        number_of_games=int(input(" - Quiero guardar... "))
    except ValueError as error:
            print(f"------------  ERROR ヽ(≧Д≦)ノ ------------- \n-- El valor ingresado no cuenta como número ٩(ఠ益ఠ)۶ --- \n---  DETALLES: {error} \n---  Reiniciando (`ー´)")
            time.sleep(5)
            main()
    list_games(number_of_games)

if __name__=='__main__':
    main()