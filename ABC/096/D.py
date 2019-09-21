import math

def is_prime(n):
    if n == 1:
        return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    # 素数判定を5で割ったら1余るものだけ返すように変更
    if n % 5 == 1:
        return True
    else:
        return False

def main():
    N = int(input())
    num_list = []
    for i in range(1, 55556):
        if is_prime(i):
            num_list.append(i)
            if len(num_list) == N:
                print(*num_list)
                exit()

main()