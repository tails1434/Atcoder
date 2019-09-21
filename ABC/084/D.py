from itertools import accumulate

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def main():
    Q = int(input())
    N = 10 ** 5
    num_list = [0] * (N + 5)

    for i in range(1,N+1):
        if is_prime(i) and is_prime((i+1)//2):
            num_list[i] = 1

    sum_num = [0] * (N + 5)

    for i in range(N+1):
        sum_num[i+1] = sum_num[i] + num_list[i]

    for _ in range(Q):
        l, r = map(int, input().split())
        print(sum_num[r+1]-sum_num[l])



main()