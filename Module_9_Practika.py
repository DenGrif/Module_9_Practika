# -*- coding: utf-8 -*-
# 1 Написать функцию, которая возвращает функцию повторения двух первых символов n количество раз
# 2 Создать массив функций и применить все функции поочерёдно к аргументу
# 3 Применить все функции поочерёдно к массиву аргументов

animal = 'мишка'
animals = ['зайка, мишка, бегемотик']

def gen_repeat(n):
    def repeat(animals):
        return (animals[:2] + '-') * n + animals
    return repeat

test_1 = gen_repeat(1)
test_2 = gen_repeat(2)

print(test_1(animal))
print(test_2(animal))

print(2)# 2
#
repetitions = [gen_repeat(n) for n in range(1, 4)]
print(repetitions)

result = [func(animal) for func in repetitions]
print(result)

print(3)# 3

fin_result1 = [func(x) for func in repetitions for x in animals]
fin_result2 = [func(x) for x in animals for func in repetitions ]

print(fin_result1)
print(fin_result2)