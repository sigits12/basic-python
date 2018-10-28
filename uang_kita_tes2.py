def foo(x, a, b, i, j):
    k = j
    ct = 0
    while(k > i - 1):
        if (x[k] <= b and not (x[k] <= a)):
            ct = ct + 1
        k = k - 1
    return ct


y = []
m = 0
while(m < 100):
    y.append(m)
    m = m + 1

print(foo(y, 1, 9, 2, 90))
