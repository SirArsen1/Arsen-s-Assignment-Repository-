import random, sys, os

fruits = ['apples', 'bananas', 'oranges']
ran_fruit = random.choice(fruits)
print(ran_fruit)

usernum = input("please write a number: ")

rn = random.randint(2, 10)

usernum, Num2 = int(usernum), int(rn)
answer = usernum * rn

Equation = f"{usernum} {ran_fruit}, * {rn} {ran_fruit} = {answer} {ran_fruit}"
print(Equation)