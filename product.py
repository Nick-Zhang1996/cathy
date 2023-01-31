# product practice test
import random
from time import time

def normal(correct_count, total_count):
    val1 = random.randrange(1,9)
    val2 = random.randrange(1,9)

    correct = False

    while (not correct):
        try:
            val = input(f'{val1} X {val2} = ? \n')
            total_count += 1
            if (int(val) == val1*val2):
                correct_count += 1
                print(f'correct! ({correct_count}/{total_count}/{count})')
                break
            else:
                print(f'wrong! ({correct_count}/{total_count}/{count})')
        except ValueError:
            continue
    return correct_count, total_count

def reverse(correct_count, total_count):
    val1 = random.randrange(1,9)
    val2 = random.randrange(1,9)

    correct = False

    while (not correct):
        try:
            val = input(f'? X {val2} = {val1*val2} \n')
            total_count += 1
            if (int(val) == val1):
                correct_count += 1
                print(f'correct! ({correct_count}/{total_count}/{count})')
                break
            else:
                print(f'wrong! ({correct_count}/{total_count}/{count})')
        except ValueError:
            continue
    return correct_count, total_count

def reverse_alt(correct_count, total_count):
    val1 = random.randrange(1,9)
    val2 = random.randrange(1,9)

    correct = False

    while (not correct):
        try:
            val = input(f'{val2} X ? = {val1*val2} \n')
            total_count += 1
            if (int(val) == val1):
                correct_count += 1
                print(f'correct! ({correct_count}/{total_count}/{count})')
                break
            else:
                print(f'wrong! ({correct_count}/{total_count}/{count})')
        except ValueError:
            continue
    return correct_count, total_count

count = 50
correct_count = 0
total_count = 0

random.seed()
input(f'total {count} problems, ready? (press Enter)')
t0 = time()
while correct_count < count:
    val = random.random()
    if (val < 1/2):
        correct_count, total_count = normal(correct_count, total_count)
    if (val < 3/4):
        correct_count, total_count = reverse(correct_count, total_count)
    else:
        correct_count, total_count = reverse_alt(correct_count, total_count)

dt = time()-t0
print(f'complete!')
print(f'({correct_count}/{total_count}/{count})')
print(f'accuracy {correct_count/total_count*100:.2f}%')
print(f'duration {dt:.2f}s')
print(f'Average each question {dt/total_count:.2f}s')
