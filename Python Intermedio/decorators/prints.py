#Cree un decorador que haga print de los parámetros y retorno de la función que decore.
import math

def print_all(func):
    def wrapper(*args, **kwargs):
        print(f"Function parameters:{args}, {kwargs} \nFunction result: {func(*args, **kwargs)}")
    return wrapper


@print_all
def calculate_perimeter(radius):
    perimeter=2*math.pi*radius
    return perimeter


calculate_perimeter(5)