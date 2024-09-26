def in_array(array1, array2):
    arr = []
    for x in array1:
        for y in array2:
            if x in y:
                arr.append(x)
                pass
    return sorted(set(arr))