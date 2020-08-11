def main():
    A, B, C, D = list(input())
    for i in ['+','-']: 
        for j in ['+','-']:
            for k in ['+','-']:
                tmp = A + i + B + j + C + k + D
                if eval(tmp) == 7:
                    print(tmp+'=7')
                    exit()

if __name__ == "__main__":
    main()