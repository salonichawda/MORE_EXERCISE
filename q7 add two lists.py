list1 = [1, 5, 10, 12, 16, 20]

list2 = [1, 2, 10, 13, 16]

list3=list1+list2

print(list3)

i=0

a=[]

while i<len(list3):

    if list3[i] not in a:
    
        a.append(list3[i])
    
    i+=1

print(a)

