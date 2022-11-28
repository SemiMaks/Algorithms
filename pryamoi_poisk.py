"""
Прямой поиск (сдвиг образца по одному символу) .
Алгоритм КМП Кнута-Морриса-Пратта.
Число операций: O(n*m) n-количество символов в строке, m- количество символов в образце.

Оптимизация алгоритма: Сдвиг образца по максимальному префиксу.
Этапы КМПЖ
1. формирование массива пи (для сдвига по префиксам) - (ли, л-префикс, и-сцффикс)
2. поиска образца в строке
Число операций: O(n+m)
"""

t = "лилила"
p = [0]*len(t)
j = 0
i = 1

while i < len(t):
    if t[j] == t[i]:
        p[i] = j+1
        i += 1
        j += 1
    else:
        if j == 0:
            p[i] = 0
            i += 1
        else:
            j = p[j-1]
print(p)

a = "лолилолилалилилал"
n = len(a)
m = len(t)

i = 0
j = 0

while i < n:
    if a[i] == t[j]:
        i += 1
        j += 1
        if j == m:
            print("Образ найден")
            break
    else:
        if j > 0:
            j = p[j-1]
        else:
            i += 1
            if i == n:
                print("Образ не найден")