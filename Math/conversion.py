def add_binary(a,b):
    n = a+b
    if n == 0:
        return 0
    result = []
    while n > 0:
        result.append(str(n%2))
        n //=2
    return ''.join(result[::-1])