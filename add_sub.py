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


def subtraction(correct_count, total_count):
    val1 = random.randrange(0,9999)
    val2 = random.randrange(0,9999)

    prompt = f'{max(val1,val2)} - {min(val1,val2)} = ?'
    answer = abs(val1-val2)
    return problem(prompt, answer, correct_count, total_count)

def addition(correct_count, total_count):
    val1 = random.randrange(0,9999)
    val2 = random.randrange(0,9999)

    prompt = f'{val1} + {val2} = ?'
    answer = val1 + val2
    return problem(prompt, answer, correct_count, total_count)


random.seed()
correct_count = 0
total_count = 0

count = int(input('how many problems? '))
input(f'total {count} problems, ready? (press Enter)')
t0 = time()
problem_fun = [subtraction,addition]
problem_weight = [1,1]

while correct_count < count:
    val = random.random()
    this_problem = random.choices(problem_fun,problem_weight)[0]
    correct_count, total_count = this_problem(correct_count, total_count)

dt = time()-t0
print(f'complete!')
print(f'({correct_count}/{total_count}/{count})')
print(f'accuracy {correct_count/total_count*100:.2f}%')
print(f'duration {dt:.2f}s')
print(f'Average each question {dt/total_count:.2f}s')
