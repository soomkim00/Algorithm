w = 0
for i in range(8):
    l = input()
    line = list(l)
    for j in range(8):
        if line[j] == 'F' and (i + j) % 2 == 0:
            w += 1
print(w)