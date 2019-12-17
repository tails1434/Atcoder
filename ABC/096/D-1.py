def is_prime(n):
    if n == 1:
        return False

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    if n % 5 == 1:
        return True
    else:
        return False

def main():
    N = int(input())
    ans = []
    
    for i in range(1, 55556):
        if is_prime(i):
            ans.append(i)
            if len(ans) == N:
                print(*ans)
                exit()
    



if __name__ == "__main__":
    main()