import numpy as np
import struct
#用python列表生成元素序列，再转为numpy定义的矩阵类型numpy.ndarray
def createMatrixList(num, rows, cols):
    matrix_list = []
    for i in range(num):
        matrix = []
        for j in range(rows * cols):
            matrix.append((i + 1) * 10 + (j + 1))
        matrix = np.reshape(matrix, (rows, cols))
        matrix_list.append(matrix)
    matrix_list = np.array(matrix_list, dtype='ubyte')
    return matrix_list


def createMatrix(num: int, rows: int, cols: int) -> np.ndarray:
    matrix_list = np.zeros((num, rows, cols), 'uint8')
    for i in range(num):
        matrix = np.arange(1, rows * cols + 1).astype('ubyte')
        matrix += (i + 1) * 10
        matrix_list[i] = matrix.reshape((rows, cols))
    return matrix_list

if __name__ == '__main__':
    matrix_list = createMatrixList(5, 2, 3)
    print(type(matrix_list), '\n', matrix_list.dtype, '\n', matrix_list)
    matrix_list = createMatrix(5, 2, 3)
    print(type(matrix_list), '\n', matrix_list.dtype, '\n', matrix_list)
