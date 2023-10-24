def non_div():
    s = [19, 10, 12, 10, 24, 25, 22]
    k = 4 
    subset = []
    count = 0
    for element in (s):
        for index in range (len(s) - 1):
            print (element, s[index + 1])
            if element + s[index + 1] % 4 != 0:
                x = element
                y = s[index + 1]
                if len(subset) < 2:
                    subset.append(element)
                    subset.append(s[index + 1])
                if len(subset) > 2:
                    subset.clear()
                    
    print (subsets)



non_div()
