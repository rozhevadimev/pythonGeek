#Задача 2: Найдите сумму цифр трехзначного числа. 123 -> 6 (1 + 2 + 3)
n = input("Enter a three-digit number: ")
n = int(n)
m1 = n % 10
m2 = n % 100 // 10
m3 = n // 100
print("The sum of the digits of a three-digit number:", m1 + m2 + m3)
