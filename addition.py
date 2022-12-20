# addition practice test
import random
from time import time

count = 10
correct_count = 0
total_count = 0

random.seed()
input('ready? (press Enter)')
t0 = time()
while correct_count < count:
    val1 = random.randrange(11,88)
    val2 = random.randrange(11,88)
    val = input(f'{val1} + {val2} = ')
    total_count += 1
    if (int(val) == val1+val2):
        correct_count += 1
        print(f'correct! ({correct_count}/{total_count}/{count})')
    else:
        print(f'wrong! ({correct_count}/{total_count}/{count})')

dt = time()-t0
print(f'complete!')
print(f'({correct_count}/{total_count}/{count})')
print(f'accuracy {correct_count/total_count*100}%')
print(f'duration {dt}s')
print(f'Average each question {dt/total_count}s')
