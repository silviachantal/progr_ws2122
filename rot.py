def rotated (lst, n):
    for elem in lst:
        if n > 0:
            i = lst.index(elem)
            newlist = lst[i:i+(- n)]
            print(newlist)
        else:
            print(lst)              

rotated([1,2,3], 2)