from math import gcd
import sys
sys.setrecursionlimit(1000000)

def main():
    N = int(input())
    A = list(map(int, input().split()))
    tmp = gcd(A[0],A[1])
    set_A = set(A)
    for i in range(2,N):
        tmp = gcd(tmp, A[i])

    if tmp != 1:
        print('not coprime')
        exit()
    max_A = max(A)
    ans = [False] * (max_A + 1)
    flag = True
    def divisor(n):
        ass = []
        for i in range(1,int(n**0.5)+1):
            if n%i == 0:
                ass.append(i)
                if ans[i]:
                    return False
                if i != 1:
                    ans[i] = True
                if i**2 == n:
                    continue
                if ans[n//i]:
                    return False
                ans[n//i] = True
                ass.append(n//i)
        if n != 1:
            ans[n] = True
        return True #sortされていない
    for a in A:
        if not divisor(a):
            flag = False
            break

    if flag:
        print('pairwise coprime')
    else:
        print('setwise coprime')
    






if __name__ == "__main__":
    main()