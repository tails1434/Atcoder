from collections import defaultdict

def main():
    N = int(input())
    D = list(map(int, input().split()))
    MOD = 998244353
    for i, d in enumerate(D):
        if (i == 0 and d != 0) or (i > 0 and d == 0):
            print(0)
            exit()
    set_D = list(set(D))
    set_D.sort()
    cnt = 0
    for i in set_D:
        if cnt == i:
            cnt += 1
        else:
            print(0)
            exit()

    A = defaultdict(int)
    for d in D:
        A[d] += 1

    cnt = 1
    pre = 0
    for key, value in A.items():
        if key == 0 or key == 1:
            pre = value
        else:
            cnt *= pre ** value 
            cnt %= MOD
            pre = value
    print(cnt)

    

    


if __name__ == "__main__":
    main()