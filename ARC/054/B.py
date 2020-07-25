def f(p,x):
    return x + p/(2**(x/1.5))

def main():
    P = float(input())
    high = 1000
    low = 0
    while high - low > 0.000000001:
        mid_left = high / 3 + low * 2 / 3
        mid_right = high * 2 / 3 + low / 3
        if f(P,mid_left) >= f(P,mid_right):
            low = mid_left
        else:
            high = mid_right

    print(f(P,high))


if __name__ == "__main__":
    main()