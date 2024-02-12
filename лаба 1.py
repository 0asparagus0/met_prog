import pandas as pd
import time
from matplotlib import pyplot as plt

"""This module provides a collection of functions for working with strings."""

# @brief пирамидальная сортировка
# идём снизу вверх 
def sift_up(arr): 
    for i in range(len(arr)): 
        while i>0: 
            j = (i-1)//2  # индекс родителя 
            if arr[i]>arr[j]: 
                arr[i],arr[j] = arr[j],arr[i] 
            else: 
                break 
            i=j 
    return arr
 
# идём сверху вниз 
def sift_down(arr,i,last_index): 
    while True: 
        left_j = 2*i + 1 # левый ребёнок 
        right_j = 2*i + 2 # правый ребёнок 
        j=i # родитель 
        if left_j < last_index and arr[left_j] > arr[j]: 
            j = left_j 
        if right_j < last_index and arr[right_j] > arr[j]: 
            j = right_j 
        if j != i: # если какой-то из ребёнков больше чем родитель 
            arr[i],arr[j] = arr[j],arr[i] 
            i = j 
        else: 
            break 
    return arr
 
def heap_sort(mas): 
    arr=mas.copy()
    sift_up(arr) 
    last_index = len(arr) - 1 
    while last_index > 0: 
        arr[0], arr[last_index] = arr[last_index], arr[0] 
        sift_down(arr, 0, last_index) 
        last_index -=1
    return arr 

# @brief быстрая сортировка
def quick_sort(mas):
    if len(mas)<=1: return mas
    less = []
    equal = []
    more = []
    border = mas[0]
    for x in mas:
        if x < border:
            less.append(x)
        elif x == border:
            equal.append(x)
        else:
            more.append(x)
    return quick_sort(less)+equal+quick_sort(more)
   

# @brief сортировка слиянием
def merge_sort(mas):
    if len(mas)<=1: return mas
    left=merge_sort(mas[:len(mas)//2])
    right=merge_sort(mas[len(mas)//2:])
    res=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            res.append(left[i])
            i+=1
        else:
            res.append(right[j])
            j+=1
    if i<len(left): res+=left[i:]
    if j<len(right): res+=right[j:]
    return res

# @brief Массив данных о членах сборной команды по футболу: страна, ФИО футболиста, название клуба, амплуа (вратарь, защитник, полузащитник, нападающий), количества матчей, проведенных за сборную, количество забитых за сборную мячей (для вратарей – пропущенных со знаком «минус»)
class footballer:
    def __init__(self, country, name, club, role, match_count, goal_count):
        self.country = country
        self.name = name
        self.club = club
        self.role = role
        self.match_count = match_count
        self.goal_count = goal_count

    def __str__(self):
        return "({0},{1},{2},{3},{4},{5})".format(self.country, self.name, self.club, self.role, self.match_count, self.goal_count)

    # @brief Перегрузка операторов для сравнения по полям – количество матчей, ФИО, количество мячей (по убыванию)
    # @brief <
    def __lt__(self, other):
        if self.match_count < other.match_count:
            return True
        elif self.match_count > other.match_count:
            return False
        else:
            if self.name < other.name: 
                return True
            elif self.name > other.name: 
                return False
            else:
                return True if self.goal_count > other.goal_count else False

    # @brief >
    def __gt__(self, other):
        if self.match_count > other.match_count:
            return True
        elif self.match_count < other.match_count:
            return False
        else:
            if self.name > other.name: 
                return True
            elif self.name < other.name: 
                return False
            else:
                return True if self.goal_count < other.goal_count else False
                
    # @brief <=
    def __le__(self, other):
        return False if self > other else True

    # @brief >=
    def __ge__(self, other):
        return False if self < other else True

# @brief Подготовка данных для отправки в функции сортировок
df_1 = pd.read_csv('100_samples.csv')
mas_1 = []
for i in range(len(df_1)):
    mas_1.append(footballer(df_1["Страна"][i], df_1["ФИО"][i], df_1["Клуб"][i], df_1["Амплуа"][i], df_1["Количество матчей"][i], 
                            df_1["Количество мячей"][i]))

df_2 = pd.read_csv('500_samples.csv')
mas_2 = []
for i in range(len(df_2)):
    mas_2.append(footballer(df_2["Страна"][i], df_2["ФИО"][i], df_2["Клуб"][i], df_2["Амплуа"][i], df_2["Количество матчей"][i], 
                            df_2["Количество мячей"][i]))
    
df_3 = pd.read_csv('1000_samples.csv')
mas_3 = []
for i in range(len(df_3)):
    mas_3.append(footballer(df_3["Страна"][i], df_3["ФИО"][i], df_3["Клуб"][i], df_3["Амплуа"][i], df_3["Количество матчей"][i], 
                            df_3["Количество мячей"][i]))
    
df_4 = pd.read_csv('5000_samples.csv')
mas_4 = []
for i in range(len(df_4)):
    mas_4.append(footballer(df_4["Страна"][i], df_4["ФИО"][i], df_4["Клуб"][i], df_4["Амплуа"][i], df_4["Количество матчей"][i], 
                            df_4["Количество мячей"][i]))
    
df_5 = pd.read_csv('10000_samples.csv')
mas_5 = []
for i in range(len(df_5)):
    mas_5.append(footballer(df_5["Страна"][i], df_5["ФИО"][i], df_5["Клуб"][i], df_5["Амплуа"][i], df_5["Количество матчей"][i], 
                            df_5["Количество мячей"][i]))
    
df_6 = pd.read_csv('50000_samples.csv')
mas_6 = []
for i in range(len(df_6)):
    mas_6.append(footballer(df_6["Страна"][i], df_6["ФИО"][i], df_6["Клуб"][i], df_6["Амплуа"][i], df_6["Количество матчей"][i], 
                            df_6["Количество мячей"][i]))
    
df_7 = pd.read_csv('100000_samples.csv')
mas_7 = []
for i in range(len(df_7)):
    mas_7.append(footballer(df_7["Страна"][i], df_7["ФИО"][i], df_7["Клуб"][i], df_7["Амплуа"][i], df_7["Количество матчей"][i], 
                            df_7["Количество мячей"][i]))
    
# @brief Все датасеты в одном списке
common_mas=[mas_1, mas_2, mas_3, mas_4, mas_5, mas_6, mas_7]
# @brief Координаты х для графиков зависимости времени от объема данных
lens=[len(elem) for elem in common_mas]

# @brief Отправка данных для пирамидальной сортировки. Замер времени. Создание файлов с отсортированными данными
heap_sort_times=[]
for elem in common_mas:
    start = time.time()
    mas_heap_sort = heap_sort(elem)
    heap_sort_times.append(time.time() - start)
    with open(f'heap_sort_{len(elem)}.txt', 'w',encoding="utf-8") as f:
        for elem in mas_heap_sort:
            f.write(f'{elem.country} {elem.name} {elem.club} {elem.role} {elem.match_count} {elem.goal_count}\n')

# @brief Отправка данных для быстрой сортировки. Замер времени. Создание файлов с отсортированными данными
quick_sort_times=[]
for elem in common_mas:
    start = time.time()
    mas_quick_sort = quick_sort(elem)
    quick_sort_times.append(time.time() - start)
    with open(f'quick_sort_{len(elem)}.txt', 'w',encoding="utf-8") as f:
        for elem in mas_quick_sort:
            f.write(f'{elem.country} {elem.name} {elem.club} {elem.role} {elem.match_count} {elem.goal_count}\n')

# @brief Отправка данных для сортировки слиянием. Замер времени. Создание файлов с отсортированными данными
merge_sort_times=[]
for elem in common_mas:
    start = time.time()
    mas_merge_sort = merge_sort(elem)
    merge_sort_times.append(time.time() - start)
    with open(f'merge_sort_{len(elem)}.txt', 'w',encoding="utf-8") as f:
        for elem in mas_merge_sort:
            f.write(f'{elem.country} {elem.name} {elem.club} {elem.role} {elem.match_count} {elem.goal_count}\n')

# @brief Построение графиков зависимости времени работы каждой из сортировок от объема данных
plt.plot(lens,heap_sort_times)
plt.plot(lens,quick_sort_times)
plt.plot(lens,merge_sort_times)
plt.legend(['heap_sort', 'quick_sort', 'merge_sort'])
plt.xlabel("Размерность")
plt.ylabel("Секунды")
plt.title("Зависимость времени от размерности массива")
plt.show()