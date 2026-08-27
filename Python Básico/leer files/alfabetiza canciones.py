def organized_playlist(songs_sorted):
    with open('canciones/canciones organizadas.txt', 'w') as file:
        for song in songs_sorted:
            file.writelines(song.strip()+"\n")

def alphabetize(songs_list):
    songs_list.sort()
    organized_playlist(songs_list)

def open_playlist(songs):

    with open(songs, 'r') as file:
        songs_list = file.readlines()
        alphabetize(songs_list)

        

songs_list=open_playlist('canciones/musica.txt') #Hay que ponerlo en un folder, pq si no da error el open_playlist si esta en el mismo folder
#Daría error de file no encontrado
