O = input()
E = input()

if len(O) - len(E) == 0:
    for i in range(len(O)):
        print(O[i]+E[i],end="")
else:
    print(O[0],end="")
    for i in range(1,len(O)):
        print(E[i-1]+O[i],end="")