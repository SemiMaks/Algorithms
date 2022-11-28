a = [1, 5, 7, 3, 2, 9, 4, 8, 6]
a_n = []
N = len(a)

for i in range(0, N - 1):
    for j in range(0, N - 1 - i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            print(a)

print(a_n)
