N = input()
operation_cnt = len(N) - 1

for i in range(1 << operation_cnt):
    operation = ["-"] * operation_cnt
    for j in range(operation_cnt):
        if ((i >> j) & 1):
            operation[j] = "+"

    formula = ""
    for num,operator in zip(N, operation + [""]):
        formula += (num + operator)
    if eval(formula) == 7:
        print(formula + "=7")
        exit()