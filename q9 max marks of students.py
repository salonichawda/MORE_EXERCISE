marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
def max_marks(marks):
    i=0

    while i<len(marks):

        j=0

        max=marks[i][j]
        
        while j<len(marks[i]):
        
            if marks[i][j]>max:
        
                max=marks[i][j]
        
            j+=1
        
        i+=1
        
        print(max)

max_marks(marks)

# words = "navgurukul is great"
# counter = 0
# while counter < len(words):
#     print (words[counter])
#     counter+=1




marks = [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]

def students_no(marks):

    for i in range(len(marks)):
        max1=0
        for j in range(len(marks[i])):
            if marks[i][j]>max1:
                max1=marks[i][j]

        print(max1)

students_no(marks)