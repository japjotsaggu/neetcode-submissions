[
    [1, 2], 
    [3, 4]
]

[
    [3, 1], 
    [4, 2]
]
# (0, 0) --> (0, 1)
# (1, 0) --> (0, 0)
# (1,1) --> (1, 0)
# (0, 1) -->(1, 1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        visited = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if (i, j) in visited:
                    continue 
                else:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                    visited += ((i,j), (j,i))

        for i in range(len(matrix)):
            start, end = 0, len(matrix[0])-1 
            while start < end:
                matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
                start +=1 
                end -= 1

    
        