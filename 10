#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
#решкой, а некоторые – гербом. Определите минимальное число
#монеток, которые нужно перевернуть, чтобы все монетки были
#повернуты вверх одной и той же стороной. Выведите минимальное
#количество монет, которые нужно перевернуть.
import random
nul = 0
one = 0
while 1:
    enter = input('кол-во монет: ')
    for i in range(int(enter)):
        x = random.randint(0, 1)
        if x == 0:
            nul += 1
        elif x == 1:
            one += 1
        print(x)
    print('орлы: ', nul)
    print('решки: ', one)
    break 
def minimum(nul, one):  
    if nul <= one:
        return nul
    else:
        return one
print("минимум, необходимый для перевёртывания = " ,minimum(nul, one),"монет")
