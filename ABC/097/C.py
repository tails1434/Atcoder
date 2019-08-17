def main():
    s = input()
    K = int(input())

    S = set()

    for i in range(len(s)):
        for j in range(1, K+1):
            S.add(s[i:i+j])
    
    sort_S = sorted(list(S))

    print(sort_S[K-1])
main()