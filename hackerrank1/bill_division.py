def billdivision():
    bill = [3, 10, 2, 9]
    anna = 12
    b = (sum(bill))
    print (b)
    brian = (b / 2)
    owed = (brian - anna)
    if owed == 0:
        print ("Bon Appetit")
    else:
        print (owed)


billdivision()


