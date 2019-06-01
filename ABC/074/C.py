A, B, C, D, E, F = map(int, input().split())

sugar_water = -1
sugar = -1
concentration = -1

for i in range(F//(A*100)+1):
    for j in range((F-A*100*i)//(B*100)+1):
        for k in range((F-A*i*100-B*100*j)//C+1):
            for l in range((F-A*i*100-B*100*j-C*k)//D+1):
                x = i * A + j * B
                y = k * C + l * D
                if x == 0:
                    continue
                if x * E >= y and concentration < (100 * y)/(x*100+y):
                    sugar_water = 100 * x + y
                    sugar = y
                    concentration = (100 * y)/(x*100+y)

print(sugar_water,sugar)