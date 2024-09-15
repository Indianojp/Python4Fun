def longest(a1, a2):
    a3 = list(set(a1 + a2))
    sort = ""
    for x in range(97,123):
        if chr(x) in a3:
            sort += chr(x)
    return sort