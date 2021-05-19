def my_function(lst):
    final = 0
    finallst = []
    for i in lst:
        final = final +i
        finallst.append(final)
    return finallst

lst2 = my_function([1,-1,3])
print(lst2)
