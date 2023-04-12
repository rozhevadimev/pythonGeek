#Задача №19. Решение в группах
#Дана последовательность из N целых чисел и число 
#K. Необходимо сдвинуть всю последовательность 
#(сдвиг - циклический) на K элементов вправо, K – 
#положительное число.
steps = (int(input('Введите шаг сдвига: ')))
from random import randint
N = 10
a = []
for i in range(N):
    a.append(randint(1, 99))
print(a)
for i in range(N - 1):
    for i in range(N - steps):
        a.insert(0, a.pop())
print(a)
