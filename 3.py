#Задача №3. #В некоторой школе решили набрать три новых
#математических класса и оборудовать кабинеты для
#них новыми партами. За каждой партой может сидеть
#два учащихся. Известно количество учащихся в
#каждом из трех классов. Выведите наименьшее
#число парт, которое нужно приобрести для них.
a = int(input('Введите количество учеников в первом классе '))
b = int(input('Введите количество учеников в втором классе '))
c = int(input('Введите количество учеников в третьем классе '))
print('Количество парт необходимо закупить: ', a // 2 + b // 2 + c // 2 + a % 2 + b % 2 + c % 2, 'парт')