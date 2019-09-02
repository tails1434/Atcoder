def main():
    A, B = map(int, input().split())
    
    if B == 1:
        print(0)
        exit()
        
    B -= A

    cnt = 1

    
    if B > 0:
        cnt += B // (A-1) + (1 if B % (A-1) > 0 else 0)

    print(cnt)
        

main()