def get_middle(s):
    a = int(len(s) / 2)
    if len(s) <= 2:
        return(s)
    else:
        if len(s) % 2 == 0:
            return(s[a - 1: -(a - 1)])
        return(s[a: -(a)])

# membuat s baru sampai len(s) <= 2
# def get_middle(s):
#     while len(s) > 2:
#         s = s[1:-1]
#     return s


get_middle("vFo")
