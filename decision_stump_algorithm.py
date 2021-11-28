import math
import statistics
import random
import numpy as np


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def x():
    return random.random() * 2 - 1


def y(x):
    if x > 0:
        y = 1
    elif x < 0:
        y = -1
    prob = random.random()
    if prob <= 0.2:
        y = -y

    return y


def minimize_Ein(X, Y):
    # 升序排列
    X, Y = list(zip(*sorted(
        zip(X, Y),
        key=lambda x_y_pair: x_y_pair[0]
    )))

    Ein = None
    best_s_list = None
    best_theta_list = None
    N = len(X)
    for i in range(N):
        if i < N - 1:
            r = random.random()
            interval = X[i + 1] - X[i]
            theta = X[i] + r * interval
        else:
            r = random.random()
            interval = 1 - X[i]
            theta = X[i] + r * interval

        s = 1
        Ein_current = calculate_Ein(X, Y, s, theta)
        if Ein is None or Ein_current < Ein:
            Ein = Ein_current
            best_s_list = [s]
            best_theta_list = [theta]
        elif Ein_current == Ein:
            best_s_list.append(s)
            best_theta_list.append(theta)

        s = -1
        Ein_current = calculate_Ein(X, Y, s, theta)
        if Ein is None or Ein_current < Ein:
            Ein = Ein_current
            best_s_list = [s]
            best_theta_list = [theta]
        elif Ein_current == Ein:
            best_s_list.append(s)
            best_theta_list.append(theta)

    best_index = random.randrange(0, len(best_s_list), 1)
    best_s = best_s_list[best_index]
    best_theta = best_theta_list[best_index]

    return Ein, best_s, best_theta


def calculate_Ein(X, Y, s, theta):
    Ein = 0
    for index, x in enumerate(X):
        y = Y[index]
        if y == s * sign(x - theta):
            pass
        else:
            Ein = Ein + 1
    # Average
    return Ein / len(X)


def single_dimension():
    N = 20
    iter = 5000
    Ein_list = []
    Eout_list = []
    for _ in range(iter):
        X = [
            x()
            for i in range(N)
        ]
        Y = [
            y(x)
            for x in X
        ]
        Ein, s, theta = minimize_Ein(X, Y)
        Eout = 0.5 + 0.3 * s * (abs(theta) - 1)
        Ein_list.append(Ein)
        Eout_list.append(Eout)
    print(
        statistics.mean(Ein_list),
        statistics.mean(Eout_list)
    )


def multi_dimension():
    X_train = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw2_train.dat')
    Y_train = X_train[:, -1]
    X_train = X_train[:, :9]
    X_test = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw2_test.dat')
    Y_test = X_test[:, -1]
    X_test = X_test[:, :9]

    Ein_multidimension = []
    s_multidimension = []
    theta_multidimension = []
    for dimension_index in range(X_train.shape[1]):
        X = X_train[:, dimension_index]
        Y = Y_train
        Ein, s, theta = minimize_Ein(X, Y)
        Ein_multidimension.append(Ein)
        s_multidimension.append(s)
        theta_multidimension.append(theta)
    best_dimension = np.argmin(Ein_multidimension)
    Ein = Ein_multidimension[best_dimension]
    s = s_multidimension[best_dimension]
    theta = theta_multidimension[best_dimension]

    Eout = calculate_Ein(X_test[:, best_dimension], Y_test, s, theta)

    print(Ein, Eout)


if __name__ == '__main__':
    single_dimension()

    multi_dimension()
