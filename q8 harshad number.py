def is_my_function(num):

    i=num
    
    sum=0
    
    check=False
    
    while num>0:
    
        a=num%10
    
        sum+=a
    
        num//=10
    
    if i%sum==0:
    
        check=True
    
        print(i,"is harshad number",check)
    
    else:
    
        print(i,"is not harshad number",check)

        return False
    
is_my_function(num=int(input("enter the number:")))    