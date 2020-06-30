def num_divisors_table(n):
    table = [0] * (n + 1)
    
    for i in range(1, n+1):
        for j in range(i, n + 1, i):
            table[j] += 1
    
    return table
def main():
    N = int(input())
    tmp = num_divisors_table(N)
    ans = 0
    for i in range(1,N+1):
        ans += i * tmp[i]

    print(ans)





if __name__ == "__main__":
    main()