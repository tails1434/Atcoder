from collections import defaultdict

def main():
    N = int(input())
    d = defaultdict(int)
    for _ in range(N):
        S = input()
        d[S] += 1

    max_d = max(d.values())
    ans = []
    for key, value in d.items():
        if value == max_d:
            ans.append(key)
    ans.sort()
    for a in ans:
        print(a)
    
    



if __name__ == "__main__":
    main()