import sys


def greenLine(inputs):
    sol = []
    inps = [i.split() for i in inputs]
    # print(inputs)
    for i in range(len(inps)):
        if '  '.join(inputs[i].split()) == inputs[i].strip():
            sol.append(str(i+1))
            continue
        for c in inps[i]:
            if c == inps[i][0] and (ord(c[0]) < 65 or ord(c[0]) > 90):
                sol.append(str(i + 1))
                break
            if c == ',' or c == ' ':
                sol.append(str(i+1))
                break
            if c == inps[i][len(inps[i])-1] and c[-1] != '.':
                sol.append(str(i+1))
                break
    print(sol)
    if len(sol) > 0:
        return " ".join(sol)
    else:
        return "No Problems"

inputs = []
# for i in range(100):
#     line = input()
#     if line:
#         inputs.append(line)
#     else:
#         break
s = sys.stdin.readlines()
# s = s.split('\n')
print(greenLine(s))