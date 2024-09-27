def pig_it(text):
    rtxt = text.split()
    lat = ""
    for x in rtxt:
        if x.isalpha():
            lat += x[1:] + x[0] + 'ay' + ' '
        else: lat += x + ' '
    return lat[:len(lat)-1]