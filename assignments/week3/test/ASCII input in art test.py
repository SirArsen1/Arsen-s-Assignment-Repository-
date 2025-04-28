import random

count = 0

print("please, answer the questions:\n")

for n in range(1,10):
    for u in range(1,10):
        print(f"please, solve this equation:\n{n} * {u}", end=' = ')
        count += 1
        if count == 1:
            break
    if count == 1:
        break
