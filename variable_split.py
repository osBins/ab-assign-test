import random
import matplotlib.pyplot as plt

arr = []
for i in range(10000):
    num = random.random() * 1000000

    mod = num % 10

    if mod >= 3:
        arr.append(1)
    else:
        arr.append(0)
count = [arr.count(0), arr.count(1)]
print(count)
