#13) 13, д, е, ж 
'''
д) Пирамидальная сортировка 
е) Быстрая сортировка 
ж) Сортировка слиянием

Массив данных о членах сборной команды по футболу: страна, ФИО футболиста, название клуба, амплуа (вратарь,  защитник, полузащитник, нападающий), 
количества матчей,  проведенных за сборную, количество забитых за сборную  мячей (для вратарей – пропущенных со знаком «минус»)  
(сравнение по полям – количество матчей, ФИО,  количество мячей (по убыванию))

1) Реализовать на высокоуровневом языке программирования сортировки для массива объектов в  соответствии с вариантом. 
2) Перегрузить операторы сравнения (>, <, >=, <=) для сравнения  объектов. Правила сравнения указаны в варианте.
3) Входные данные для сортировки массива обязательно считывать из  внешних источников: текстовый файл, файлы MS Excel, MS Access, 
данные из СУБД (любое на выбор). Выходные данные (отсортированный массив) записывать в файл.
4) Выбрать 7-10 наборов данных для сортировки размерности от 100 и  более (но не менее 100000). 
Засечь (программно) время сортировки  каждым алгоритмом. По полученным точкам построить графики зависимости времени сортировки от 
размерности массива для каждого  из алгоритмов сортировки на одной оси координат. Сделать вывод о  том, в каком случае, какой из методов 
лучше применять.
5) Сделать отчет, состоящий из:
    -документации к коду работы, сгенерированную с помощью case средства (doxygen, sphinx, etc);
    -ссылку на исходный код программы в репозитории;
    -графики времени сортировок. 
'''

import pandas as pd
import time
from matplotlib import pyplot as plt

# пирамидальная сортировка
'''
Преобразует список в бинарное дерево, где самый большой элемент является вершиной дерева.
Помещает этот элемент в конец списка.
Перестраивает дерево и помещает новый наибольший элемент перед последним элементом в списке.
Повторяет этот алгоритм, пока все вершины дерева не будут удалены.'''

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
        #print(arr) 
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
        #print(arr) 
    return arr
 
def heap_sort(mas): 
    arr=mas.copy()
    sift_up(arr) 
    last_index = len(arr) - 1 
    while last_index > 0: 
        arr[0], arr[last_index] = arr[last_index], arr[0] 
        #print(arr) 
        sift_down(arr, 0, last_index) 
        last_index -=1
    return arr 

# быстрая сортировка
'''Идея: Выбрать опорный элемент - любой из списка. Разделить список на 3 части: 1) меньше опорного 2)равные опорного 3) больше опорного.
Далее с 1) и 3) сделать то же самое. Рекурсия, пока длина списка >1. Все это сложить.'''

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
   

# сортировка слиянием
'''Идея: взять список, разделить его пополам, затем еще пополам и еще, пока у вас не окажется куча списков с длиной, равной единице. 
После этого нужно выстроить элементы в пары, располагая их в отсортированном порядке, а затем соединять эти пары вместе, образуя все большие 
упорядоченные группы, до тех пор, пока не получите целый отсортированный список.'''

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

    #<
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
                return True if self.goal_count < other.goal_count else False

    #>
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
                return True if self.goal_count > other.goal_count else False
                
    #<=
    def __le__(self, other):
        return False if self > other else True

    #>=
    def __ge__(self, other):
        return False if self < other else True


df_1 = pd.read_csv('100_samples.csv')
mas_1 = []
for i in range(len(df_1)):
    mas_1.append(footballer(df_1["Страна"][i], df_1["ФИО"][i], df_1["Клуб"][i], df_1["Амплуа"][i], df_1["Количество матчей"][i], 
                            df_1["Количество мячей"][i]))
'''
for elem in mas_1:
    print(elem)'''

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
    
common_mas=[mas_1, mas_2, mas_3, mas_4, mas_5, mas_6, mas_7]
lens=[len(elem) for elem in common_mas]

heap_sort_times=[]
for elem in common_mas:
    start = time.time()
    mas_heap_sort = heap_sort(elem)
    heap_sort_times.append(time.time() - start)
    with open(f'heap_sort_{len(elem)}.txt', 'w',encoding="utf-8") as f:
        for elem in mas_heap_sort:
            f.write(f'{elem.country} {elem.name} {elem.club} {elem.role} {elem.match_count} {elem.goal_count}\n')

quick_sort_times=[]
for elem in common_mas:
    start = time.time()
    mas_quick_sort = quick_sort(elem)
    quick_sort_times.append(time.time() - start)
    with open(f'quick_sort_{len(elem)}.txt', 'w',encoding="utf-8") as f:
        for elem in mas_quick_sort:
            f.write(f'{elem.country} {elem.name} {elem.club} {elem.role} {elem.match_count} {elem.goal_count}\n')

merge_sort_times=[]
for elem in common_mas:
    start = time.time()
    mas_merge_sort = merge_sort(elem)
    merge_sort_times.append(time.time() - start)
    with open(f'merge_sort_{len(elem)}.txt', 'w',encoding="utf-8") as f:
        for elem in mas_merge_sort:
            f.write(f'{elem.country} {elem.name} {elem.club} {elem.role} {elem.match_count} {elem.goal_count}\n')
print(heap_sort_times, quick_sort_times, merge_sort_times)
plt.plot(lens,heap_sort_times)
plt.plot(lens,quick_sort_times)
plt.plot(lens,merge_sort_times)
plt.legend(['heap_sort', 'quick_sort', 'merge_sort'])
plt.xlabel("Размерность")
plt.ylabel("Секунды")
plt.title("Зависимость времени от размерности массива")
plt.show()