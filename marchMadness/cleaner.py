with open('accountsList.txt', 'r') as f:
    lines = f.readlines()

lines = list(set(lines))

with open('FinalAccountList2.txt', 'a') as f:
    for line in lines:
        f.write(line)
        
