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
def createMiniMNIST(mnist_filename, dst_dir):
    mnist = readMatrixFromFile(mnist_filename)

    num, width, height = mnist.shape
    top_mnist = np.zeros(mnist.shape, np.uint8)
    center_mnist = np.zeros(mnist.shape, np.uint8)
    bottom_mnist = np.zeros(mnist.shape, np.uint8)

    minw = width // 2
    minh = height // 2
    mini_mnist = mnist[:, ::2, ::2]
    top_mnist[:, :minw, :minh] = mini_mnist
    center_mnist[:, minw // 2:minw // 2 + minw, minh // 2:minh // 2 + minh] = mini_mnist
    bottom_mnist[:, minw:, minh:] = mini_mnist

    # 示例
    sample = random.randint(0, num - 1)
    displayImages([mnist[sample], top_mnist[sample],
                   center_mnist[sample], bottom_mnist[sample]],
                  ['raw', 'top', 'center', 'bottom'])
    sample = random.randint(0, num - 1)
    displayImages([mnist[sample], top_mnist[sample],
                   center_mnist[sample], bottom_mnist[sample]],
                  ['raw', 'top', 'center', 'bottom'])

    return top_mnist, center_mnist, bottom_mnist
def dataReader(image_filename, label_filename, batch_size, drop_last=False):
    labels = readMatrixFromFile(label_filename)
    images = readMatrixFromFile(image_filename)
    batchnum = int(len(images) / batch_size)
    sample = list(range(len(images)))
    random.shuffle(sample)

    def batch_reader():
        # 每次迭代提供batch_size个样本
        for i in range(batchnum):
            # yield buff[i * batch_size:(i + 1) * batch_size]
            yield (images[sample[i*batch_size:i*batch_size+batch_size]],
                   labels[sample[i * batch_size:i * batch_size + batch_size]])

        if drop_last and len(images) % batch_size != 0:
            # yield buff[batchnum * batch_size:]
            yield (images[sample[i*batch_size:]],
                   labels[sample[i * batch_size:i]])
    return batch_reader()


def displayBatch(image_file, label_file, batch_size, drop_last=False):
    loader = dataReader(image_file, label_file, batch_size, drop_last)
    for i, data in enumerate(loader):
        # images, labels = zip(*data)
        images, labels = data
        displayImages(images, labels)
        if i > 3:
            break

if __name__ == '__main__':
    dst_dir = 'D:/MyProject/firstDay/data/'
    displayBatch(dst_dir+'t10k-images-idx3-ubyte',dst_dir+'t10k-labels-idx1-ubyte',4)


# if __name__ == '__main__':
#     dst_dir = 'data/'
#     readMnistAndDisplay(dst_dir+'t10k-images-idx3-ubyte')
#     top_mnist, center_mnist, bottom_mnist =createMiniMNIST(
#     mnist_filename=dst_dir+'t10k-images-idx3-ubyte',
#     dst_dir= dst_dir)
#     writeMatrixToFile(dst_dir + 'top_t10k-images-idx3-ubyte', top_mnist)
#     writeMatrixToFile(dst_dir + 'centre_t10k-images-idx3-ubyte', center_mnist)
#     writeMatrixToFile(dst_dir + 'bottom_t10k-images-idx3-ubyte', bottom_mnist)


# if __name__ == '__main__':
#     dst_dir = 'data/'
#     readMnistAndDisplay(dst_dir+'t10k-images-idx3-ubyte')
