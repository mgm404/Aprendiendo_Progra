numbers=[]

for i in range(10):
    number=int(input("\nIntrodusca un número \n"))
    numbers.append(number)

num1=0
num2=0
big=0

for i in range(len(numbers)):
    num1=numbers[i]
    if num1>big:
        big=num1

print(f"Estos fueron sus números: \n{numbers} \nEste es el número más grande de la lista: \n{big}")