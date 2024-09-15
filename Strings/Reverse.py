def solution(string):
    reverse = ""
    for i in range(len(string) -1, -1, -1):
        reverse += str(string[i])
    pass