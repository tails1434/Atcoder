def main():
    N, M = map(int, input().split())
    
    left = 0
    right = float('inf')
    
    for i in range(M):
        L, R = map(int, input().split())
        left = max(left, L)
        right = min(right, R)
    
    if left <= right:
        print(right - left + 1)
    else:
        print(0)

main()