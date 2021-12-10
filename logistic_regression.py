import numpy as np


def fixed_learning_rate_gradient_descent(eta=0.001, T=2000, stochastic=False):
    X_train = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_algo/hw3_train.dat')
    Y_train = X_train[:, [-1]]
    X_train = X_train[:, :20]
    X_test = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_algo/hw3_test.dat')
    Y_test = X_test[:, [-1]]
    X_test = X_test[:, :20]

    w0 = np.zeros((20, 1))
    wt = w0
    N = X_train.shape[0]

    for i in range(T):
        if not stochastic:
            gradient_Ein = (1 / N) * \
                           np.matmul(
                               (- Y_train * X_train).T,
                               sigmoid(- Y_train * np.matmul(X_train, wt))
                           )
        else:
            x = X_train[[i % N], :]
            y = Y_train[[i % N], :]
            gradient_Ein = sigmoid(- y * np.matmul(wt.T, x.T)) * (- y * x)

        wt = wt - eta * gradient_Ein

    Ein_cross_entropy = np.mean(
        np.log(
            1 + np.exp(
                - Y_train * np.matmul(X_train, wt)
            )
        )
    )

    Eout_cross_entropy = np.mean(
        np.log(
            1 + np.exp(
                - Y_test * np.matmul(X_test, wt)
            )
        )
    )

    Ein_01 = np.mean(np.sign(np.matmul(X_train, wt)) != Y_train)
    Eout_01 = np.mean(np.sign(np.matmul(X_test, wt)) != Y_test)

    return wt


def sigmoid(x: np.ndarray):
    return np.exp(x) / (1 + np.exp(x))


if __name__ == '__main__':
    wt = fixed_learning_rate_gradient_descent(0.001, stochastic=True)
    print()
