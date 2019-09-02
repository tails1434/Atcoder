def main():
    N = input()
    
    if int(N) <= int(N[0]*3):
        print(N[0]*3)
    else:
        print(str(int(N[0]) + 1) * 3)



main()