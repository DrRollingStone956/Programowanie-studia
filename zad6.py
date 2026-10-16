def fun(list1,list2):
    list3 = (set(list1+list2))
    return [x ** 3 for x in list3]
print(fun([4,2,3],[3,4,5,1,2]))