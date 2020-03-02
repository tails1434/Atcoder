def main():
    a, b = map(int, input().split())
    word = [str(a) * b, str(b) * a]
    word.sort()
    print(word[0])


if __name__ == "__main__":
    main()