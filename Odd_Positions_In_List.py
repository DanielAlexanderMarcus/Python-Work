def my_function(lst):
    final = []
    length=len(lst)-1
    while length>=0:
        if length%2!=0:
            final.append(lst[length]) 
        length=length-1
    return final

lst2 = my_function([1,-1,2,-2])
print(lst2)
