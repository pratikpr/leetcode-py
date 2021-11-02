def cipher(col, order, str):
    col = int(col)
    order = [int(x) for x in order.split()]

    l = len(str)//col
    if len(str) % col != 0:
        l += 1

    cm = [['*' for x in range(col)] for y in range(l)]
    print(col, order)
    k = 0
    for i in range(l):
        for j in range(0, col):
            if (k < len(str)):
                cm[i][j] = str[k]
                k += 1

    ans = []
    for j in order:
        for i in range(l):
            if cm[i][j-1] != '*':
                ans.append(cm[i][j-1])
    print("".join(ans))
    return

col = input()
order = input()
str = input()
print(cipher(col, order, str))