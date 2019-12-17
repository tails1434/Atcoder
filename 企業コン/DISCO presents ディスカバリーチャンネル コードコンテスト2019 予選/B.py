def func1(x, N):
    return -x + (N / 2)

def func2(x, N):
    return -x + 3 * (N / 2)

def func3(x, N):
    return x + (N / 2)

def func4(x, N):
    return x - (N / 2)

def check(x, y, N):
    if func1(x, N) <= y and func4(x, N) <= y and func3(x, N) >= y and func2(x, N) >= y:
        return True
    else:
        return False

def main():
    N = int(input())
    cnt = 0
    for x in range(N + 1):
        for y in range(N + 1):
            if check(x, y, N) and check(x + 1, y, N) and check(x, y+1, N) and check(x+1,y+1,N):
                cnt += 1

    print(cnt)
    



if __name__ == "__main__":
    main()