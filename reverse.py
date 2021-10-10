l =[[1, 2], [3, 4], [5, 6, 7]]

def reverseList(l):
    l.reverse()
    for x in l:
        if type(x) == list:
            reverseList(x)
        else:
            pass
reverseList(l)
print(l)
