#Cree un decorador que haga print de los parámetros y retorno de la función que decore.
import math

def print_all(func):
    def wrapper(*args, **kwargs):
        result= func(*args, **kwargs)
        print(f"Function parameters:{args}, {kwargs} \nFunction result: {result}")
        return result
    return wrapper


@print_all
def calculate_perimeter(radius):
    perimeter=2*math.pi*radius
    return perimeter


calculate_perimeter(5)