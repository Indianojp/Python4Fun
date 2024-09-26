def sort_array(source_array):
    odd = sorted([])
    for x in source_array:
        if x % 2 == 1:
            odd.append(x)
    odd = sorted(odd)
    i = 0
    j = 0
    for x in source_array:
        if x % 2 == 1:
            source_array[j] = odd[i]
            i += 1
        j += 1
    return source_array