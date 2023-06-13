def generate_rows(rows: int) -> list:
    pascal = [[1] * (i + 1) for i in range(rows)]
    for i in range(rows):
        for j in range(1, i):
            pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
    return pascal
