def my_function(lst):
    num=0
    length=len(lst)-1
    while length>=0:
        if length!=len(lst)-1 and length!=0:
            num=num+lst[length]
        length=length-1               
    num = int(num/(len(lst)-2))
    return num

lst2 = my_function([-10,-4,-2,-4,-2,0])
print(lst2)
