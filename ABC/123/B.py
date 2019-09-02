import itertools

def main():
    cnt = 0
    mod = 10
    for i in range(5):
        A = int(input())
        if A % 10 == 0:
            cnt += A
        else:
            cnt += 10 - (A % 10)
            cnt += A
            mod = min(mod, A % 10)

    if mod == 10:
        print(cnt)
    else:
        print(cnt - (10 - mod))

main()