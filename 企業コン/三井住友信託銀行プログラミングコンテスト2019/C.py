def main():
    X = int(input())
    for a in range(X // 100 + 1):
        for b in range((X - a * 100) // 101 + 1):
            for c in range((X - a * 100 - b * 101) // 102 + 1):
                for d in range((X - a * 100 - b * 101 - c * 102) // 103 + 1):
                    for e in range((X - a * 100 - b * 101 - c * 102 - d * 103) // 104 + 1):
                        for f in range((X - a * 100 - b * 101 - c * 102 - d * 103 - e * 104) // 105 + 1):
                            if X - a * 100 - b * 101 - c * 102 - d * 103 - e * 104 - f * 105 == 0:
                                print(1)
                                exit()

    print(0)




if __name__ == "__main__":
    main()