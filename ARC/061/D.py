from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    H, W, N = map(int, input().split())
    j = [0] * 10
    ans = [0] * 10
    ans[0] = (H - 2) * (W - 2)
    d = defaultdict(int)
    dt = [-1,0,1]
    for i in range(N):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        for i in dt:
            if 0 <= a + i <= H - 1:
                for j in dt:
                    if 0 <= b + j <= W - 1:
                        tmp = d[(a + i, b + j)]
                        d[(a + i, b + j)] += 1
                        if 1 <= a + i <= H - 2 and 1 <= b + j <= W - 2:
                            ans[tmp] -= 1
                            ans[tmp + 1] += 1
    print(d)
    
    for a in ans:
        print(a)


if __name__ == "__main__":
    main()