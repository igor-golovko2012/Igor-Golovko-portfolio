56# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 19:40:57 2024

@author: igorg
"""

numbers = []
indexes = []
total = 0
lowest = None
highest = None

while True:
    try:
        digit = input("Введите число или 'Enter', чтобы завершить: ")
        if not digit:
            break
        indexes.append(len(numbers))
        number = int(digit)
        numbers.append(number)
        total += number
        if lowest is None or lowest > number:
            lowest = number
        if highest is None or highest < number:
            highest = number
    except ValueError:
        print("ВВОДИТЬ ТОЛЬКО ЧИСЛА!")

swapped = True
while swapped:
    swapped = False
    for index in indexes:
        if index + 1 == len(numbers):
            break
        if numbers[index] > numbers[index + 1]:
            temp = numbers[index]
            numbers[index] = numbers[index + 1]
            numbers[index + 1] = temp
            swapped = True

index = int(len(numbers) / 2)
median = numbers[index]
if index and index * 2 == len(numbers):
    median = (median + numbers[index - 1]) / 2

print()
print("Числа:", numbers)
print("Количество чисел =", len(numbers))
print("Общая сумма =", total)
print("Самое маленькое =", lowest)
print("Самое большое =", highest)
print("Среднее арифметическое =", total / len(numbers))
print("Медиана =", median)
