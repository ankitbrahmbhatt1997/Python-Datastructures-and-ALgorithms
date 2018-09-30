from sys import stdin

t = int(stdin.readline())

for i in range(t):
    symbols = list(stdin.readline())
    check_set = set(("<", ">"))
    helper_stack = []
    counter = 0
    longest_prefix = 0
    for k in symbols:

        if k == "<":

            helper_stack.append(k)
        elif k == ">":

            if len(helper_stack) == 0:
                break
            closing = helper_stack.pop()
            counter += 2
        if(len(helper_stack) == 0):
            longest_prefix = counter
    print(longest_prefix)
