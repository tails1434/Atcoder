from collections import defaultdict

def main():
    H, W, N = map(int, input().split())
    d = defaultdict(int)
    dt = [-1,0,1]
    for _ in range(N):
        a, b = map(int, input().split())
        for i in dt:
            if 2 <= a + i <= H-1:
                for j in dt:
                    if 2 <= b + j <= W-1:
                        # 正方形の中点をkeyとして持つ
                        d[(a+i,b+j)] += 1
    
    ans = [0] * 10
    ans[0] = (H-2) * (W-2)
    for i in d.values():
        ans[i] += 1
        ans[0] -= 1

    for a in ans:
        print(a)
    

if __name__ == "__main__":
    main()