def my_function(lst):
    final=[]
    lst = str(lst)
    for i in lst:
        final.append(int(i))
    return final

lst2 = my_function(400)
print(lst2)
