def determinant(m):
    if len(m) == 1:
        return m[0][0]
    if len(m) == 2:
        i = 0
        j = len(m) - 1
        return m[i][i] * m[j][j] - m[i][j] * m[j][i]
    elif len(m) > 2:
        det = 0
        for c in range(len(m)):
            sub = [row[:c] + row[c+1:] for row in m[1:]]
            det += ((-1) ** c) * m[0][c] * determinant(sub)
    return det