def find_smallest_int(arr):
    y = arr[0]
    for x in arr:
        if x < y:
            y = x
    return y