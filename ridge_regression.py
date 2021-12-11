import numpy as np


def ridge_regression(Lambda=10):
    X_train = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_algo/hw4_train.dat')
    Y_train = X_train[:, [-1]]
    X_train = X_train[:, :2]
    X_test = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_algo/hw4_test.dat')
    Y_test = X_test[:, [-1]]
    X_test = X_test[:, :2]

    # 添加 x0 = 1
    X_train = np.concatenate(
        [np.ones((X_train.shape[0], 1)), X_train],
        axis=1
    )
    X_test = np.concatenate(
        [np.ones((X_test.shape[0], 1)), X_test],
        axis=1
    )

    w = np.matmul(
        np.linalg.inv(
            np.matmul(X_train.T, X_train) + Lambda * np.identity(3)
        ),
        np.matmul(X_train.T, Y_train)
    )

    Ein_01 = np.mean(np.sign(np.matmul(X_train, w)) != Y_train)
    Eout_01 = np.mean(np.sign(np.matmul(X_test, w)) != Y_test)

    return w, Ein_01, Eout_01


def ridge_regression_with_validation(Lambda=10):
    X_train_raw = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_algo/hw4_train.dat')

    X_valid = X_train_raw[120:, :2]
    Y_valid = X_train_raw[120:, [-1]]

    X_train = X_train_raw[:120, :2]
    Y_train = X_train_raw[:120, [-1]]

    X_test = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_algo/hw4_test.dat')
    Y_test = X_test[:, [-1]]
    X_test = X_test[:, :2]

    # 添加 x0 = 1
    X_train = np.concatenate(
        [np.ones((X_train.shape[0], 1)), X_train],
        axis=1
    )
    X_valid = np.concatenate(
        [np.ones((X_valid.shape[0], 1)), X_valid],
        axis=1
    )
    X_test = np.concatenate(
        [np.ones((X_test.shape[0], 1)), X_test],
        axis=1
    )

    w = np.matmul(
        np.linalg.inv(
            np.matmul(X_train.T, X_train) + Lambda * np.identity(3)
        ),
        np.matmul(X_train.T, Y_train)
    )

    Ein_01 = np.mean(np.sign(np.matmul(X_train, w)) != Y_train)
    Eval_01 = np.mean(np.sign(np.matmul(X_valid, w)) != Y_valid)
    Eout_01 = np.mean(np.sign(np.matmul(X_test, w)) != Y_test)

    return w, Ein_01, Eval_01, Eout_01


def ridge_regression_with_cross_validation(Lambda=10):
    X_train_raw = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_algo/hw4_train.dat')
    N = X_train_raw.shape[0]

    X_test = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_algo/hw4_test.dat')
    Y_test = X_test[:, [-1]]
    X_test = X_test[:, :2]

    X_test = np.concatenate(
        [np.ones((X_test.shape[0], 1)), X_test],
        axis=1
    )

    Ecv_list = []

    for i in range(int(N / 40)):

        X_valid = X_train_raw[i * 40: (i+1) * 40, :2]
        Y_valid = X_train_raw[i * 40: (i+1) * 40:, [-1]]

        if i == 0:
            X_train = X_train_raw[ (i+1) * 40 :, :2]
            Y_train = X_train_raw[ (i+1) * 40 :, [-1]]
        elif i == (N / 40) - 1:
            X_train = X_train_raw[ : i * 40, :2]
            Y_train = X_train_raw[ : i * 40, [-1]]
        else:
            X_train = np.concatenate(
                [
                    X_train_raw[: i * 40, :2],
                    X_train_raw[ (i+1) * 40 :, :2],
                ], axis=0
            )
            Y_train = np.concatenate(
                [
                    X_train_raw[: i * 40, [-1]],
                    X_train_raw[ (i+1) * 40 :, [-1]],
                ], axis=0
            )


        # 添加 x0 = 1
        X_train = np.concatenate(
            [np.ones((X_train.shape[0], 1)), X_train],
            axis=1
        )
        X_valid = np.concatenate(
            [np.ones((X_valid.shape[0], 1)), X_valid],
            axis=1
        )


        w = np.matmul(
            np.linalg.inv(
                np.matmul(X_train.T, X_train) + Lambda * np.identity(3)
            ),
            np.matmul(X_train.T, Y_train)
        )

        Ein_01 = np.mean(np.sign(np.matmul(X_train, w)) != Y_train)
        Eval_01 = np.mean(np.sign(np.matmul(X_valid, w)) != Y_valid)
        Eout_01 = np.mean(np.sign(np.matmul(X_test, w)) != Y_test)

        Ecv_list.append(Eval_01)

    return w, np.mean(Ecv_list)


if __name__ == '__main__':
    # w, Ein, Eout = ridge_regression(10)

    # Ein_list = []
    # Eout_list = []
    # for i in range(2, -11, -1):
    #     w, Ein, Eout = ridge_regression(10 ** i)
    #     Ein_list.append(Ein)
    #     Eout_list.append(Eout)

    # Ein_list = []
    # Eval_list = []
    # Eout_list = []
    # for i in range(2, -11, -1):
    #     w, Ein, Eval, Eout = ridge_regression_with_validation(10 ** i)
    #     Ein_list.append(Ein)
    #     Eval_list.append(Eval)
    #     Eout_list.append(Eout)

    # logx = 0, x = 1 不是0
    w, Ein, Eout = ridge_regression(1)

    # Ecv_list = []
    # for i in range(2, -11, -1):
    #     w, Ecv = ridge_regression_with_cross_validation(10 ** i)
    #     Ecv_list.append(Ecv)

    # w, Ein, Eout = ridge_regression(10 ** (-8))


    print()
