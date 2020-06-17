def main():
    A, V = map(int, input().split())
    B, W = map(int, input().split())
    T = int(input())
    dis = abs(B - A)
    if W >= V:
        print('NO')
        exit()
    dis_V = V - W
    time = dis // dis_V if dis % dis_V == 0 else (dis // dis_V) + 1
    
    if T >= time:
        print('YES')
    else:
        print('NO')



if __name__ == "__main__":
    main()