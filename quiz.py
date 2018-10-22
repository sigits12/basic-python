# kodi = 20
# gross = 144
# lusin = 12
# pcs = 1

# print(int(15 / 4)) ->> 3

z = [300, 10000]
for t in z:
    a = [[144, " gross", 0], [20, " kodi", 0], [12, " lusin", 0], [1, " pcs", 0]]
    px = ""
    for x in range(0, 4):
        a[x][2] = int(t / a[x][0])
        t = t % a[x][0]
        if a[x][2] > 0:
            px += str(a[x][2]) + a[x][1] + " "
    print(px)
