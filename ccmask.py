def maskify(w):
    a = []
    for i in range(len(w)):
        if i < len(w) - 4:
            a.append("#")
        else:
            a.append(w[i])
    a = ''.join(a)
    return a


print(maskify("assdk4"))
