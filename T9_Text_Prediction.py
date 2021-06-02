def t9_to_words(numbers, key_map, valid_words):
    lst=[]
    lst_final=[]
    length=0
    pre=''
    for i in valid_words:
        if len(i)==len(numbers):
            while length<=len(i)-1:
                pre=pre+i[length]
                num=numbers[length]
                key=key_map[int(num)]
                if pre[length] in key:
                    lst.append(i)
                length=length+1
            length=0 
            lst_final.append(lst) 
            lst=[]
    for i in lst_final:
        for j in i:
            if j not in lst:
                lst.append(j)
    print(lst)
    return lst
