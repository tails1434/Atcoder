def divisor(n):
    ass = float('inf')
    for i in range(1,int(n**0.5)+1):
        tmp = 0
        if n%i == 0:
            tmp += i
            tmp += n//i
            ass = min(ass, tmp)
    return ass

def main():
    N = int(input())
    tmp = divisor(N)
    print(tmp-2)

  

if __name__ == "__main__":
    main()