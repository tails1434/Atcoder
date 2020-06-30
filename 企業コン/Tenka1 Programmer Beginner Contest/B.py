def main():
    A, B, K = map(int, input().split())
    cnt = 0
    while K > 0:
        if cnt % 2 == 0:
            if A % 2 == 0:
                A //= 2
                B += A
            else:
                A -= 1
                A //= 2
                B += A
        else:
            if B % 2 == 0:
                B //= 2
                A += B
            else:
                B -= 1
                B //= 2
                A += B
        cnt += 1
        K -= 1

    print(A, B)

if __name__ == "__main__":
    main()