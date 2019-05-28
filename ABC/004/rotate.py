l=list(input() for i in range(4))

for i in range(4):
    print(l[3-i][::-1])