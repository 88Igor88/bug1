print("Выбор сортировки")
import random
from algh import *
data = [random.randint(-100, 100) for n in range(100)]
res = {}
print(f"Нужно отсортировать: {data}")



algh = input("Выберите функцию сортировки(по умолчанию sort_ch):")
if algh == "h":
    print("sort_ch bubble quick_sort")
    algh = input("Выберите функцию сортировки(по умолчанию sort_ch):")

if algh == "sort_ch":
    res = sort_ch(data)
if algh == "bubble":
    res = bubble(data)
if algh == "quick_sort":
    res = quick_sort(data)

print("Обработка....")

print("Список:")
for x in res:
    print(x, end=" ")
