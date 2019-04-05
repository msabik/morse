from functools import reduce
from random import randint

#number = randint(11,10000)
number = 234567
numbers = []
numbers2 = []
for n in str(number):
    numbers.append(int(n))
    numbers2.append(int(n))
spawn = len(numbers)
index = 0
indexx = spawn -1

while spawn >0:
    for x in numbers:
        numbers3 = numbers[index:]
        numbers4 = numbers[:indexx]
        print(numbers3, index)
        print(numbers4, f'hh {indexx}')
        #print(f'spawn {spawn}')
        if index < spawn + 1:
            numbers2.append(reduce(lambda a, b: a * b, numbers3))
            numbers2.append(reduce(lambda a, b: a * b, numbers4))
            spawn -= 1
            index += 1
            indexx -= 1
        else:
            spawn -= 1

print(numbers2)
