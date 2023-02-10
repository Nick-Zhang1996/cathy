# product practice test
import random
from time import time


def problem(prompt : str, answer : int, correct_count, total_count):
    correct = False
    while (not correct):
        try:
            val = int(input(prompt))
        except ValueError:
            continue

        total_count += 1
        if (int(val) == answer):
            correct_count += 1
            print(f'correct! ({correct_count}/{total_count}/{count})')
            break
        else:
            print(f'wrong! ({correct_count}/{total_count}/{count})')
    return correct_count, total_count

def product(correct_count, total_count):
    val1 = random.randrange(1,9)
    val2 = random.randrange(1,9)

    prompt = f'{val1} X {val2} = ?'
    answer = val1*val2
    return problem(prompt, answer, correct_count, total_count)

def multiXone(correct_count, total_count):
    val1 = random.randrange(111,999)
    val2 = random.randrange(3,9)

    prompt = f'{val1} X {val2} = ?'
    answer = val1*val2
    return problem(prompt, answer, correct_count, total_count)

def multiXmulti(correct_count, total_count):
    val1 = random.randrange(111,999)
    val2 = random.randrange(22,199)

    prompt = f'{val1} X {val2} = ?'
    answer = val1*val2
    return problem(prompt, answer, correct_count, total_count)

random.seed()
correct_count = 0
total_count = 0
count = 50

t0 = time()

for i in range(35):
    correct_count, total_count = product(correct_count, total_count)
for i in range(10):
    correct_count, total_count = multiXone(correct_count, total_count)
for i in range(5):
    correct_count, total_count = multiXmulti(correct_count, total_count)


dt = time()-t0
print(f'complete!')
print(f'({correct_count}/{total_count}/{count})')
print(f'accuracy {correct_count/total_count*100:.2f}%')
print(f'duration {dt:.2f}s')
print(f'Average each question {dt/total_count:.2f}s')
