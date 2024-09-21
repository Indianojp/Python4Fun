def solution(s):
    list = []
    i = 1
    if s == "":
        return []
    while i < len(s):
        list.append(s[i-1] + s[i])
        i += 2
    if len(s) % 2 == 1:
        list.append(s[-1:]+'_')
    return list