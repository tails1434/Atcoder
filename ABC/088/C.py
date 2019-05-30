c = [[int(i) for i in input().split()] for i in range(3)] 

for a1 in range(101):
    b1 = c[0][0] - a1
    b2 = c[0][1] - a1
    b3 = c[0][2] - a1
    a2_1 = c[1][0] - b1
    a2_2 = c[1][1] - b2
    a2_3 = c[1][2] - b3
    a3_1 = c[2][0] - b1
    a3_2 = c[2][1] - b2
    a3_3 = c[2][2] - b3
    if (a2_1 == a2_2 == a2_3) and (a3_1 == a3_2 == a3_3):
        print('Yes')
        exit()

print('No')