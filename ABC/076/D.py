from itertools import accumulate

def main():
    N = int(input())

    t = list(map(int, input().split()))
    v = list(map(int, input().split()))

    T = sum(t)

    vmax = [0] * (2 * T + 1)

    cnt = 0

    for i in range(1,2*T):
        vmax[i] = v[cnt]
        if i == t[cnt]:
            cnt += 1

    for i in range(1,2*T):
        vmax[i] = min(vmax[i],vmax[i-1]+0.5)
    
    for i in range(2*T-1, -1,-1):
        vmax[i] = min(vmax[i], vmax[i+1]+0.5)

    print(vmax)


main()