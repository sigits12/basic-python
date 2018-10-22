a = ['10', '1', '23', '*', '39', '34']
# ops = [x for x in a if not x.isdigit()]

for x in a:
    if x.isdigit() == False:
        ops = x

for x in range(len(a)):
    if a[x] == ops:
        kiri, kanan = a[:x], a[x + 1:]

print(ops)
print(kiri)
print(kanan)
