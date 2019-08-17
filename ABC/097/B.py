import math

def main():
    X = int(input())

    ans = 1
    for i in range(1,X):
        for j in range(2,X):
            if i ** j <= X:
                ans = max(ans, i ** j)
            else:
                break

    print(ans)

main()