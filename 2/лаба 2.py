import timeit
import pandas as pd
from matplotlib import pyplot as plt
from collections import defaultdict

# @brief вершина бинарного дерева
class Node: 
    def __init__(self, data):
        self.key=data.get_name()
        self.data = data 
        self.left = self.right = None 

# @brief бинарное дерево
class Tree:  
    def __init__(self):
        self.root = None 

    def __find(self, node, value):# ищем к какой вершине добавить ребенка (обход в глубину)

        #сравниваем значение вершины, которую хотим добавить, со значением текущей вершины
        if value <= node.key:
            if node.left: #если существует левый потомок
                return self.__find(node.left, value)
 
        if value > node.key:
            if node.right:
                return self.__find(node.right, value)
 
        return node #вершина к которой прикрепляем лист
 
    def append(self, obj):# добавление новой вершины
        if self.root is None: 
            self.root = obj 
            return obj 

        #передаем корень дерева(тк вершину искать от корня), значение вершины(которую хотим добавить)
        s = self.__find(self.root, obj.key)
 
        if obj.key <= s.key: #если значение в текущей вершине меньше значения вершины, к которой прикрепляем лист
            s.left = obj
        else:
            s.right = obj
 
        return obj
    
    def for_find_elem(self, node, value):
        if node is None:
            return False
 
        if value == node.key:
            return True
 
        if value < node.key:
            if node.left:
                return self.for_find_elem(node.left, value)
 
        if value > node.key:
            if node.right:
                return self.for_find_elem(node.right, value)
 
        return False

    def find_elem(self, elem):
        return self.for_find_elem(self.root, elem)




# @brief вершина красно-черного дерева
class RBNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.colour = 'R'
        self.parent = None
        self.key=data.get_name()

# @brief красно-черное дерево
class RedBlackTree:

    def __init__(self):
        self.root = None
        self.ll = False  # Left-Left Rotation flag
        self.rr = False  # Right-Right Rotation flag
        self.lr = False  # Left-Right Rotation flag
        self.rl = False  # Right-Left Rotation flag
 
    def rotateLeft(self, node):
        # Perform Left Rotation
        x = node.right
        y = x.left
        x.left = node
        node.right = y
        node.parent = x
        if y is not None:
            y.parent = node
        return x
 
    def rotateRight(self, node):
        # Perform Right Rotation
        x = node.left
        y = x.right
        x.right = node
        node.left = y
        node.parent = x
        if y is not None:
            y.parent = node
        return x
 
    def insertHelp(self, root, key, obj):
        f = False  # Flag to check RED-RED conflict
 
        if root is None:
            return obj # возвращаем созданную новую вершину
        elif key < root.key:
            root.left = self.insertHelp(root.left, key, obj)
            root.left.parent = root
            if root != self.root:
                if root.colour == 'R' and root.left.colour == 'R':
                    f = True
        else:
            root.right = self.insertHelp(root.right, key, obj) #правый сын
            root.right.parent = root #добавили указатель на отца
            if root != self.root: #если отец добавленной вершины не корень дерева
                if root.colour == 'R' and root.right.colour == 'R':
                    f = True
 
        # Perform rotations
        if self.ll:
            root = self.rotateLeft(root)
            root.colour = 'B'
            root.left.colour = 'R'
            self.ll = False
        elif self.rr:
            root = self.rotateRight(root)
            root.colour = 'B'
            root.right.colour = 'R'
            self.rr = False
        elif self.rl:
            root.right = self.rotateRight(root.right)
            root.right.parent = root
            root = self.rotateLeft(root)
            root.colour = 'B'
            root.left.colour = 'R'
            self.rl = False
        elif self.lr:
            root.left = self.rotateLeft(root.left)
            root.left.parent = root
            root = self.rotateRight(root)
            root.colour = 'B'
            root.right.colour = 'R'
            self.lr = False
 
        # Handle RED-RED conflicts
        if f:
            if root.parent.right == root: #текущая вершина справа от предыдущей (отец правее деда)
                if root.parent.left is None or root.parent.left.colour == 'B':#дядя черный или пустой (те тоже черный)
                    if root.left is not None and root.left.colour == 'R': # левый сын отца красный (4й случай)
                        self.rl = True
                    elif root.right is not None and root.right.colour == 'R': # правый сын отца красный (3й случай)
                        self.ll = True
                else: #дядя красный
                    root.parent.left.colour = 'B'
                    root.colour = 'B'
                    if root.parent != self.root:
                        root.parent.colour = 'R'
            else:# отец левее деда
                if root.parent.right is None or root.parent.right.colour == 'B':#дядя черный или пустой (те тоже черный)
                    if root.left is not None and root.left.colour == 'R': #1й случай
                        self.rr = True
                    elif root.right is not None and root.right.colour == 'R': #2й случай
                        self.lr = True
                else:#дядя красный
                    root.parent.right.colour = 'B'
                    root.colour = 'B'
                    if root.parent != self.root:
                        root.parent.colour = 'R'
            f = False
        return root #вернули отца добавленной вершины (или корень)
    
    # вставка элемента
    def insert(self, obj):
        if self.root is None:
            self.root = obj #корень это ссылка на первый добавленный объект(вершину)
            self.root.colour = 'B' #корень всегда черный
        else:
            self.root = self.insertHelp(self.root, obj.key,obj)

    def for_find_elem_2(self, node, value):
        if node is None:
            return False
 
        if value == node.key:
            return True
 
        if value < node.key:
            if node.left:
                return self.for_find_elem_2(node.left, value)
 
        if value > node.key:
            if node.right:
                return self.for_find_elem_2(node.right, value)
 
        return False

    def find_elem_2(self, elem):
        return self.for_find_elem_2(self.root, elem)



# @brief один элемент хэш-таблицы
class HTNode:
    def __init__(self, data):
        self.data=data
        self.key=data.get_name()

# @brief хэш-таблица
class HashTable:

    def __init__(self, size):
        self.size = size
        self.nodes = [None]*size
    
    #вычисляем значение хэша (rot13)
    def calc_hash(self, key):
        hash_val = 0
        for char in key:
            hash_val = (hash_val + ord(char)) & 0xFFFFFFFF
            hash_val  = (hash_val - ((hash_val << 13) | (hash_val >> 19))) & 0xFFFFFFFF
        return hash_val % self.size
    
    def insert_2(self, obj):
        key = obj.key
        index = self.calc_hash(key)
        #так разрешаем коллизии
        if self.nodes[index] is None:
            self.nodes[index] = [obj]
        else:
            self.nodes[index].append(obj)
    
    def find(self, key):   
        hash_val = self.calc_hash(key)   
        index = hash_val   
        if self.nodes[index] is not None: 
            for node in self.nodes[index]: 
                if node.key == key: 
                    return True 
        return False

# @brief Массив данных о членах сборной команды по футболу: страна, ФИО футболиста, название клуба, амплуа (вратарь, защитник, полузащитник, нападающий), количества матчей, проведенных за сборную, количество забитых за сборную мячей (для вратарей – пропущенных со знаком «минус»)
class footballer:
    def __init__(self, country, name, club, role, match_count, goal_count):
        self.country = country
        self.name = name
        self.club = club
        self.role = role
        self.match_count = match_count
        self.goal_count = goal_count

    def get_name(self):
        return self.name
    



# @brief функция для подсчета числа коллизий
def collisions_count(mas):
    size=len(mas)
    hashes=[]
    collisions_tmp=0

    def calc_hash(key,size):
        hash_val = 0
        for char in key:
            hash_val = (hash_val + ord(char)) & 0xFFFFFFFF
            hash_val  = (hash_val - ((hash_val << 13) | (hash_val >> 19))) & 0xFFFFFFFF
        return hash_val % size
    
    for x in mas:
        h = calc_hash(x.get_name(), size)
        if h in hashes:
            collisions_tmp += 1
        else:
            hashes.append(h)

    return collisions_tmp



# @brief Подготовка данных для отправки 
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
# @brief данные которые будем искать
keys=['Рогов Демьян Гаврилович','Цветков Кузьма Ильич','Щукин Климент Федотович','Кудряшов Всеволод Чеславович','Смирнов Ратибор Авдеевич','Мишин Павел Григорьевич','Блохин Селиверст Чеславович']

# @brief Отправка данных в бинарное дерево. Замер времени. 
BiTree_times=[]
for elem in common_mas:
    t = Tree() #просто создали объект дерева
    for x in elem:
        t.append(Node(x)) 
    def c():
        t.find_elem(keys[common_mas.index(elem)])
    BiTree_times.append(timeit.timeit(c,number=1))

# @brief Отправка данных в красно-черное дерево. Замер времени. 
RedBlackTree_times=[]
for elem in common_mas:
    t = RedBlackTree()
    for x in elem:
        t.insert(RBNode(x))
    def b():
        t.find_elem_2(keys[common_mas.index(elem)])
    RedBlackTree_times.append(timeit.timeit(b,number=1))

# @brief Отправка данных в хэш-таблицу. Замер времени. Посчет числа коллизий
HashTable_times=[]
collisions=[]
for elem in common_mas:
    t=HashTable(len(elem))
    for x in elem:
        t.insert_2(HTNode(x))
    collisions.append(collisions_count(elem))
    def a():
        t.find(keys[common_mas.index(elem)])
    HashTable_times.append(timeit.timeit(a,number=1))

plt.plot(lens,collisions)
plt.legend(["Collisions_count"])
plt.xlabel("Размерность")
plt.ylabel("Количество коллизий")
plt.title("Зависимость количества коллизий от размерности массива")
plt.show()

# @brief реаализация подобия мультимепа
Multimap_times=[]
for elem in common_mas:
    futb = defaultdict(list)
    for x in elem:
        futb[x.get_name()].append(x)
    def f():
        keys[common_mas.index(elem)] in futb
    Multimap_times.append(timeit.timeit(f,number=1))

# @brief Построение графиков зависимости времени работы каждого поиска от объема данных
plt.plot(lens,BiTree_times)
plt.plot(lens,RedBlackTree_times)
plt.plot(lens,HashTable_times)
plt.plot(lens,Multimap_times)
plt.legend(['BiTree', 'RedBlackTree', 'HashTable','Multimap'])
plt.xlabel("Размерность")
plt.ylabel("Секунды")
plt.title("Зависимость времени от размерности массива")
plt.show()