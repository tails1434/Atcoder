def main():
    X, Y = map(int, input().split())

    cnt = 0
    tmp = X
    for i in range(10**8):
        if tmp > Y:
            break 
        tmp = tmp * 2
        cnt += 1
    
    print(cnt)

main()
