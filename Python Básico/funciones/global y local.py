def global_change():
    global variable1 #* para hacer saber q es global
    variable1 +=5
    return variable1


def local_var():
    variable2=5


variable1= 15

print(variable1)
global_change()
print(variable1)
local_var()
## print(variable2)  #** Al ser local da error acceder ya que sale como no definida, aún después de activar la función