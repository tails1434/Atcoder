from itertools import chain

def main():
    N = int(input())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))

    vmax = list(chain.from_iterable([i] * (2 * j) for i, j in zip(v, t)))
    vmax = [min(v1,v2) for v1, v2 in zip([0] + vmax, vmax + [0])]

    now = 0
    for i in range(1,len(vmax)):
        vmax[i] = min(vmax[i], now + 0.5)
        now = vmax[i]
    
    now = 0
    for i in range(len(vmax)-1,0,-1):
        vmax[i] = min(vmax[i], now + 0.5)
        now = vmax[i]

    ans = 0
    for i in range(len(vmax)-1):
        if vmax[i] == vmax[i+1]:
            ans += 0.5 * vmax[i]
        else:
            ans += (vmax[i] + vmax[i+1]) * 0.5 / 2

    print(ans)


if __name__ == "__main__":
    main()