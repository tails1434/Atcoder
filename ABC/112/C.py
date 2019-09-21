def main():
    N = int(input())
    p = []
    for i in range(N):
        x,y,h = map(int,input().split())
        p.append([x,y,h])
 
    p.sort(key=lambda x: x[2])
    a,b,c = p[-1]
    for i in range(101):
        for j in range(101):
            H = c + abs(a - i) + abs(b - j)
            for x,y,h in p:
                if h != max(H - abs(x - i) - abs(y - j), 0):
                    break
            else:
                print(i,j,H)
                exit()


main()