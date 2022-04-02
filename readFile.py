with open('puzzle.txt', 'r') as f:
    l = [[int(num) for num in line.split(',')] for line in f if line.strip() != "" ]
print(l)