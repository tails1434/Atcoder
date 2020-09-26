from collections import defaultdict

def prime_factor(n):
    ass = []
    for i in range(2,int(n**0.5)+1):
        while n % i==0:
            ass.append(i)
            n = n//i
    if n != 1:
        ass.append(n)
    return ass

def main():
    N = int(input())
    d = defaultdict(int)
    for i in range(1,N+1):
        for j in prime_factor(i):
            d[j] += 1
    # 1 * 75
    # 3 * 25
    # 5 * 15
    # 3 * 5 * 5
    e = defaultdict(int)
    for i, j in d.items():
        if j >= 2:
            e[2] += 1
        if j >= 4:
            e[4] += 1
        if j >= 14:
            e[14] += 1
        if j >= 24:
            e[24] += 1
        if j >= 74:
            e[74] += 1
    ans = 0
    ans += (e[2] - 1) * e[24]
    ans += (e[4] - 1) * e[14]
    ans += e[74]
    ans += (e[2] - 2) * e[4] * (e[4] - 1) // 2
    print(ans)

if __name__ == "__main__":
    main()