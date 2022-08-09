a = [1, 2, 3, 0, 4, 5]
k = int(input())
for i in range(k + 1, len(a)):
    a[i - 1] = a[i]
a.pop()
print(" ".join([str(i) for i in a]))
