def transposeMatrix(matrix):
    transposedMatrix = []
    for col in range(len(matrix[0])):
        newRow = []
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposedMatrix.append(newRow)
    return transposedMatrix


print(transposeMatrix( [ [1,2] ]))

print(transposeMatrix([
    [1, 2, 3]
  ]))




# https://docs.vultr.com/python/examples/transpose-a-matrix

# import numpy as np

# def transposeMatrix(matrix):
#     return np.transpose(matrix)

# def transposeMatrix(matrix):
#     transposed_matrix = list(map(list, zip(*matrix)))
#     return(transposed_matrix)