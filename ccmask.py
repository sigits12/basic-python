def maskify(w):
    word = list(w)
    for i in range(len(w) - 4):
        word[i] = '#'
    return ''.join(word)


print(maskify("assdk4"))
