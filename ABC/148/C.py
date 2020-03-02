from fractions import gcd

def lcm(x, y):
    return (x * y) // gcd(x, y)

def main():
    A, B = map(int, input().split())
    print(lcm(A,B))


if __name__ == "__main__":
    main()