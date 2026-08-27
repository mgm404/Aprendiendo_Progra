numbers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
index=0

new_numbers=[]

print(numbers)

for num in numbers:
    divisible=num%2
    if divisible==0:
        new_numbers.append(numbers[index])
    index+=1

print(new_numbers)