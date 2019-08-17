def main():
    A, B, K = map(int, input().split())
    
    for i in range(A, min(B+1, A+K)):
        print(i)
    for j in range(max(B-K+1, A+K), B+1):
        print(j)
main()