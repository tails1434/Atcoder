import datetime

def main():
    H1, M1, H2, M2, K = map(int,input().split())
    start = H1 * 60 + M1
    end = H2 * 60 + M2
    
    ans = end - start - K
    print(ans)
    


if __name__ == "__main__":
    main()