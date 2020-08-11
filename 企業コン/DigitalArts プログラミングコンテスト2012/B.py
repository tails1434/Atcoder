from collections import Counter

def main():
    C = input()
    ans = ''    
    N = len(C)
    if C == 'a' or C == 'z' * 20:
        print('NO')
        exit()

    if N == 1:
        ans += chr(ord(C[0]) - 1) + 'a'
        print(ans)
        exit()

    if C.count('z') == N:
        for i in range(N-1):
            ans += C[i]
        ans += 'y' + 'a'
        print(ans)
        exit()

    if C.count('a') == N:
        for i in range(N-2):
            ans += C[i]
        ans += 'b'
        print(ans)
        exit()


    A = sorted(C)
    B = sorted(C, reverse=True)
    if A == B:
        ans += chr(ord(C[0]) + 1)
        for i in range(1,N-1):
            ans += C[i]
        ans += chr(ord(C[N-1]) - 1)
        print(ans)
        exit()
    if list(C) == A:
        print(''.join(B))
    else:
        print(''.join(A))

if __name__ == "__main__":
    main()