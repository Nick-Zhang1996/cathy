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

def combined(correct_count, total_count):
    val1 = 100
    val2 = 100
    while (val1+val2 > 10):
        val1 = random.randrange(1,9)
        val2 = random.randrange(1,9)

    val3 = random.randrange(1,10)

    prompt = f'( {val1} + {val2} ) X {val3} = ?'
    answer = (val1+val2)*val3
    return problem(prompt, answer, correct_count, total_count)

def combined2(correct_count, total_count):
    val1 = random.randrange(1,10)
    val2 = random.randrange(1,10)

    val3 = random.randrange(1,99-val1*val2)

    prompt = f'{val1} X {val2} + {val3} = ?'
    answer = val1*val2+val3
    return problem(prompt, answer, correct_count, total_count)

def combined3(correct_count, total_count):
    val1 = 100
    val2 = 100
    while (val1+val2 > 10):
        val1 = random.randrange(1,9)
        val2 = random.randrange(1,9)

    val3 = random.randrange(1,10)

    prompt = f'{val3} X ( {val1} + {val2} ) = ?'
    answer = (val1+val2)*val3
    return problem(prompt, answer, correct_count, total_count)

def subtraction(correct_count, total_count):
    val1 = random.randrange(1,100)
    val2 = random.randrange(1,100)

    prompt = f'{max(val1,val2)} - {min(val1,val2)} = ?'
    answer = abs(val1-val2)
    return problem(prompt, answer, correct_count, total_count)

def addition(correct_count, total_count):
    val1 = random.randrange(11,88)
    val2 = random.randrange(11,88)

    prompt = f'{val1} + {val2} = ?'
    answer = val1 + val2
    return problem(prompt, answer, correct_count, total_count)

def normal(correct_count, total_count):
    val1 = random.randrange(1,9)
    val2 = random.randrange(1,9)

    prompt = f'{val1} X {val2} = ?'
    answer = val1 * val2
    return problem(prompt, answer, correct_count, total_count)

def reverse(correct_count, total_count):
    val1 = random.randrange(1,9)
    val2 = random.randrange(1,9)

    prompt = f'? X {val2} = {val1*val2} \n'
    answer = val1
    return problem(prompt, answer, correct_count, total_count)

def reverse_alt(correct_count, total_count):
    val1 = random.randrange(1,9)
    val2 = random.randrange(1,9)
    prompt = f'{val2} X ? = {val1*val2} \n'
    answer = val1
    return problem(prompt, answer, correct_count, total_count)

random.seed()
correct_count = 0
total_count = 0

count = int(input('how many problems? '))
input(f'total {count} problems, ready? (press Enter)')
t0 = time()
problem_fun = [combined, combined2, combined3,subtraction,addition,normal,reverse,reverse_alt]
problem_weight = [2,2,2,2,2,1,1,1]

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
