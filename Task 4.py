# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# *Пример:*

# 6 -> 1  4  1
# 24 -> 4  16  4
#     60 -> 10  40  10

sum = int(input('Введите сколько всего журавликов сделали дети: '))
a = sum - (sum // 3)
b = c = (sum - a) // 2
print(f"Катя сделала {a} журавликов, Петя сделал {b} журавликов, Сережа сделал {c} журавликов")
