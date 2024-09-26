def narcissistic( value ):
    n = 0
    for x in str(value):
        n += int(x)**(len(str(value)))
    if n == value:
        return True
    else: return False