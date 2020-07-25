from collections import defaultdict

def main():
    A = list(input())
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    ans = 1
    for i in range(97,123):
        for j in range(i+1,123):
            ans += d[chr(i)] * d[chr(j)]

    print(ans)



if __name__ == "__main__":
    main()