print ("1. tambah")
print ("2. kurang")
print ("3. kali")
print ("4. bagi")
pilih = int(input("masukkan pilihan : "))
if pilih == 1:
    a = int(input("nilai A : "))
    b = int(input("nilai B : "))
    c = int(input("nilai C : "))
    d = int(input("nilai D : "))
    ad = a * d
    bd = b * d
    cb = c * b
    e = ad + cb
    f = bd
    hasil = e / f

    print(a, ('/'), b, ('+'), c, ('/'), d, ('='), e, ('/'), f, ('='), hasil)
elif pilih == 2:
    a = int(input("nilai A : "))
    b = int(input("nilai B : "))
    c = int(input("nilai C : "))
    d = int(input("nilai D : "))
    ad = a * d
    bd = b * d
    cb = c * b
    e = ad - cb
    f = bd

    print(a, ('/'), b, ('-'), c, ('/'), d, ('='), e, ('/'), f)
elif pilih == 3:
    a = int(input("nilai A : "))
    b = int(input("nilai B : "))
    c = int(input("nilai C : "))
    d = int(input("nilai D : "))
    ac = a * c
    bd = b * d

    print(a, ('/'), b, ('+'), c, ('/'), d, ('='), ac, ('/'), bd)
elif pilih == 4:
    a = int(input("nilai A : "))
    b = int(input("nilai B : "))
    c = int(input("nilai C : "))
    d = int(input("nilai D : "))
    ad = a * d
    bc = b * c

    print(a, ('/'), b, ('+'), c, ('/'), d, ('='), ad, ('/'), bc)
