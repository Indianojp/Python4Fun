def divisors(integer):
    div = []
    i = 2
    while i < integer:
        if integer % i == 0:
            div.append(i)
        i += 1
    if div == []:
        return '{} is prime'.format(integer)
    return div