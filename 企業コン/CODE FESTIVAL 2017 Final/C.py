from collections import Counter

def main():
    N = int(input())
    D = list(map(int, input().split()))
    d = Counter(D)
    # 前処理
    d[0] += 1
    for i in range(13):
        if (i == 0 or i == 12) and d[i] == 2:
            print(0)
            exit()
        elif d[i] >= 3:
            print(0)
            exit()
    ans = 0
    for i in range(2**11):
        time = [0, 24]
        if d[12] == 1:
            time.append(12)
        for j in range(1,12):
            if d[j] == 1:
                if i >> j & 1:
                    time.append(24-j)
                else:
                    time.append(j)
            elif d[j] == 2:
                time.append(24-j)
                time.append(j)
        time.sort()
        ret = 25
        for i in range(1,len(time)):
            ret = min(ret, time[i]-time[i-1])
        ans = max(ans, ret)

    print(ans)


if __name__ == "__main__":
    main()