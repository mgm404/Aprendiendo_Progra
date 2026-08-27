import time

start = time.time()
print(f'Start time: {start}')
time.sleep(5) #! El código solo continua después de ese tiempo (en segundos)
print("hola mundo")
print(1234567)
print(1234567789)
end = time.time()
print(f'Elapsed: {end - start:.2f} seconds')