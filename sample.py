import numpy as np
from matplotlib import pyplot as plt


def main():

    # def y_value(x):
    #     #     return np.sin(x)
    #     # x_num = [30, 60, 90]
    #     # y_num = [0.5, 0.75, 1]
    #     #
    #     # plt.figure()
    #     # plt.subplot(211)
    #     # plt.plot(x_num, y_num, 'ro')
    #     #
    #     # plt.subplot(212)
    #     # plt.plot(y_num, x_num)
    #     #
    #     # plt.legend(['zavie', 'sin'], loc='upper left')
    #     # plt.show()

    #################################3



    x = []
    y = []

    plt.figure()
    plt.subplot(211)


    plt.subplot(212)

    plt.legend(['x', 'y'], loc='upper left')

    for i in range(10):
        x.append(i)
        y.append(i*i +2)
        plt.plot(x, y, 'ro')
        plt.plot(x, y)
        plt.show()


    #
    # def f(t):
    #     return np.exp(-t) * np.cos(2 * np.pi * t)
    #
    # t1 = np.arange(0.0, 5.0, 0.1)
    # t2 = np.arange(0.0, 5.0, 0.02)
    #
    # plt.figure()
    # plt.subplot(211)
    # plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    #
    # plt.subplot(212)
    # plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
    # plt.show()
    #


if __name__ == '__main__':
    main()