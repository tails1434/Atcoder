from collections import defaultdict

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        d[a] += 1

    key = list(d.keys())
    key.sort(reverse=True)
    cnt = 0
    ans = 0
    tmp = 0
    flag = False
    for i in key:
        if d[i] >= 4:
            ans = i * i
            flag = True
            break
    for i in key:
        if d[i] >= 2:
            if cnt == 0:
                tmp = i
            elif cnt == 1:
                tmp *= i
                ans = max(ans, tmp)
                print(ans)
                exit()
            cnt += 1

    if not flag:
        print(0)
    else:
        print(ans)

if __name__ == "__main__":
    main()