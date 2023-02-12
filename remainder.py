# product practice test
import random
from time import time

def problem2(prompt : str, answer1 : int, answer2 : int, correct_count, total_count):
    correct = False
    while (not correct):
        try:
            val_vec = [int(val) for val in input(prompt).split(',')]
            val_vec[1]
        except (IndexError,ValueError):
            continue

        total_count += 1
        if (val_vec[0] == answer1 and val_vec[1]== answer2):
            correct_count += 1
            print(f'correct! ({correct_count}/{total_count}/{count})')
            break
        else:
            print(f'wrong! ({correct_count}/{total_count}/{count})')
    return correct_count, total_count

def remainder(correct_count, total_count):
    val1 = random.randrange(2,9)
    val2 = random.randrange(1,9)
    remainder = random.randrange(0,val1-1)
    product = val1*val2+remainder

    prompt = f'{product} / {val1} = ? ... ?'
    answer1 = val2
    answer2 = remainder
    return problem2(prompt, answer1, answer2, correct_count, total_count)

random.seed()
correct_count = 0
total_count = 0
count = int(input('how many problems? '))

t0 = time()

for i in range(count):
    correct_count, total_count = remainder(correct_count, total_count)


dt = time()-t0
print(f'complete!')
print(f'({correct_count}/{total_count}/{count})')
print(f'accuracy {correct_count/total_count*100:.2f}%')
print(f'duration {dt:.2f}s')
print(f'Average each question {dt/total_count:.2f}s')
