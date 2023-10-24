def grader():
    grades = [4, 73, 67, 38, 33]
    for index in range (1, len(grades)):
        if grades[index] > 37:
            if((grades[index]%5)!=0):
                if (5 - grades[index] % 5) < 3:
                    grades[index]+= 5 - (grades[index] % 5)

    grades.pop(0)

    print (grades)




grader()
            
            
