s = input()
output = ""
cnt = 0
for i in s:
    if i == "0":
        output += "0"
        cnt += 1
    elif i == "1":
        output += "1"
        cnt += 1
    elif i == "B":
        if output != "":
            output = output[:-1]

print(output)