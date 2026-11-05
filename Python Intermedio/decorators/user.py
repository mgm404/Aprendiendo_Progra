from datetime import date

class User:
    date_of_birth: date

    def __init__(self, name, date_of_birth):
        self.date_of_birth = date_of_birth
        self.name = name

    @property
    def age(self):
        today = date.today()
        return (
            today.year
            - self.date_of_birth.year
            - (
                (today.month, today.day)
                < (self.date_of_birth.month, self.date_of_birth.day)
            )
        )


def is_of_age(func):
    def wrapper(user):
        if user.age<18:
            raise ValueError(
                f"{user.name} no tiene permitido accesar esta función, tiene que tener 18 o más años para accesarla"
            )
        return func(user)
    return wrapper

@is_of_age
def eighteen_plus_horror(user):
    print(f"Recomendation for {user.name}:Resident Evil (2026)")

user1 = User("Don Señor",date(1990, 1, 1))
user2=User("Don bebé",date(2020, 5, 9))

try:
    eighteen_plus_horror(user1)

except ValueError as error:
    print(error)