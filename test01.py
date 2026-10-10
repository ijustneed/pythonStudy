from task01_matrix import readMatrixFromFile, writeMatrixToFile
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import random

def displayImages(imgs, titles, nrows=2, ncols=2):
    # 设定n*n排列方式，这里设置的是2*2，nrows行，ncols列，figsize设定窗口大小
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(5, 6))
    for row in range(nrows):
        for col in range(ncols):
            axes[row, col].imshow(imgs[row * ncols + col], cmap=cm.gray)
            axes[row, col].set_title(titles[row * ncols + col])
plt.show()

def readMnistAndDisplay(mnist_filename):
    mnist = readMatrixFromFile(mnist_filename)
    print(mnist.shape, mnist.dtype)
    num, width, height = mnist.shape
    sample = list(range(num))
    random.shuffle(sample)
    displayImages(mnist[sample[0:4]], range(4))
    displayImages(mnist[sample[5:9]], range(4))

if __name__ == '__main__':
    dst_dir = 'data/
    readMnistAndDisplay(dst_dir+'t10k-images-idx3-ubyte')
