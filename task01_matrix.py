import os
import numpy as np
import struct


# 用 Python 列表生成元素序列，再转为 numpy 矩阵
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


def writeMatrixToFile(filename, matrix_list):
    # 如果目录不存在，自动创建
    dirname = os.path.dirname(filename)
    if dirname:
        os.makedirs(dirname, exist_ok=True)

    shapes = matrix_list.shape

    with open(filename, 'wb') as f:
        # IDX 文件头：magic number 0，dtype=8 表示 uint8，维度数
        f.write(struct.pack('>HBB', 0, 8, len(shapes)))

        # 写入各维度大小，每个维度 4 字节大端整数
        for i in shapes:
            f.write(struct.pack('>I', i))

        # 写入矩阵数据
        f.write(matrix_list.tobytes())


def readMatrixFromFile(filename):
    with open(filename, 'rb') as f:
        data_buf = f.read()

    off_set = 0

    # 读取 IDX 文件头
    _, _, dimslen = struct.unpack_from('>HBB', data_buf, off_set)
    off_set += struct.calcsize('>HBB')

    # 读取各维度大小
    shapes = struct.unpack_from('>{}I'.format(dimslen), data_buf, off_set)
    off_set += struct.calcsize('>{}I'.format(dimslen))

    # 读取矩阵数据
    count = int(np.prod(shapes))
    matrix_list = np.frombuffer(
        data_buf,
        dtype=np.uint8,
        count=count,
        offset=off_set
    )
    matrix_list = matrix_list.reshape(shapes).copy()

    return matrix_list


if __name__ == '__main__':
    matrix_list = createMatrixList(5, 2, 3)
    print(type(matrix_list), '\n', matrix_list.dtype, '\n', matrix_list)

    matrix_list = createMatrix(5, 2, 3)
    print(type(matrix_list), '\n', matrix_list.dtype, '\n', matrix_list)

    matrix_list = createMatrix(num=20, rows=2, cols=3)
    writeMatrixToFile('data/data.idx3.ubyte', matrix_list)

    restored = readMatrixFromFile('data/data.idx3.ubyte')
    print(restored, '\n', type(restored), '\n', restored.dtype)
    print('恢复是否一致:', np.array_equal(matrix_list, restored))