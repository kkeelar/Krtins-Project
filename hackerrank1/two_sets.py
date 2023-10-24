

def two_sets():
    a = [2, 3]
    b = [2, 4]
    integer = []
    final_integer = []
    for index in range(1, 101):
        for element in range (len(a)):
            for element_1 in range(len(b)):
                if index % a[element] == 0 and b[element_1] % index == 0:
                    integer.append(index)

    for x in integer:
        if x not in final_integer:
            final_integer.append(x)

    print (len(final_integer))

two_sets()
