import math

def main():
    a, b = input().split()

    ab = int(a + b)
    if math.sqrt(ab).is_integer():
        print('Yes')
    else:
        print('No')

main()