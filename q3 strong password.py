pas=str(input("enter the password:"))
length=len(pas)==6

for i in pas:

        if "$" in pas:

            if "2" or "8" in pas:

                # if pas[i]>="A" and pas[i]<="Z" or pas[i]>="a" and pas[i]<="z":

                    if "A" or "Z" in pas:

                        print("strong password")
                    else:
                        print("A or Z is not present weak password")
                # else:
                    # print("alph is wrong")
            else:
                print("8 is not present weak password")
        else:
            print("$ is not present weak password")
    
