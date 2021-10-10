liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
liste2 = []
def flatList(l):
    for x in l:
        if type(x) == list:
            flatList(x)
        else:
            liste2.append(x)
    
flatList(liste)
print(liste2)

