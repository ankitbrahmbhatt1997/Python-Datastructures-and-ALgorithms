def permute(s):
    out = []
    if len(s) == 1:
        return [s]

    else:

        for i in range(0, len(s)):

            perm = permute(s[:i]+s[i+1:])

            for j in perm:
                out += [s[i]+j]

    return out


print(permute("abc"))
