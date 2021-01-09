def helper(curr, code):
    if curr == 0:
        if code[curr] == '0':
            return 0
        else:
            return 1

    if curr == -1:
        return 1

    ways = 0
    if code[curr] == '0':
        if code[curr-1] == '1' or code[curr-1] == '2':
            return helper(curr-2, code)
        else:
            return 0

    if ((code[curr - 1] == '1') or (code[curr - 1] == '2') and (int(code[curr]) < 7)):
        ways = helper(curr-1, code) + helper(curr-2, code)
    else:
        ways = helper(curr-1, code)

    return ways


def decode_ways(code):
    return helper(len(code)-1, code)


print(decode_ways("1212"))
