def square_digits(num):
    y = ''
    for x in str(num):
        y += str(int(x)**2)
    return int(y)