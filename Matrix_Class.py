class Matrix:
    
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def get_diagonal(self) -> list:
        return [value[index] for index, value in enumerate(self.matrix)]
    
    def get_counter_diagonal(self) -> list:
        return [value[-1 + (-index)] for index, value in enumerate(self.matrix)]
    
    def rotate_rows(self, number: int) -> list:
        if self.matrix == []:
            return []
        for _ in range(number):
            self.matrix.append(self.matrix.pop(0))
        return self.matrix
    
    def rotate_columns(self, number: int) -> list:
        for k in self.matrix:
            for i in range(number):
                k.append(k.pop(0))
        return self.matrix

matrix = Matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


print("",matrix.get_diagonal(),'\n', matrix.get_counter_diagonal(),'\n',
    matrix.rotate_columns(1),'\n', matrix.rotate_rows(1))

##### M #####

class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def get_diagonal(self) -> list:
        return [self.matrix[i][i] for i in range(len(self.matrix))]

    def get_counter_diagonal(self) -> list:
        return [self.matrix[i][-i - 1] for i in range(len(self.matrix))]

    def rotate_rows(self, number: int) -> None:
        if not self.matrix:
            return
        num = number % len(self.matrix)
        self.matrix = self.matrix[num:] + self.matrix[:num]

    def rotate_columns(self, number: int) -> None:
        if not self.matrix:
            return
        num = number % len(self.matrix)
        for i in range(len(self.matrix)):
            self.matrix[i] = self.matrix[i][num:] + self.matrix[i][:num]
