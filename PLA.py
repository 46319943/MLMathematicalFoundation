import numpy as np


def sign(num):
    if num <= 0:
        return -1
    else:
        return 1


def cycle_pla():
    train_data = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_15_train.dat')

    train_x = train_data[:, :4]
    train_y = train_data[:, [4]]

    train_x = np.concatenate(
        [np.ones((train_x.shape[0], 1)), train_x]
        , axis=1
    )

    w = np.zeros((1, 5))

    update_time = 0
    while True:
        has_update = False
        for index, x in enumerate(train_x):
            predict_y = sign(np.dot(w, x))
            if predict_y != train_y[index]:
                w = w - predict_y * x
                update_time += 1
                has_update = True
        if has_update == False:
            break
    print(update_time)


def permutate_cycle_pla():
    train_data = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_15_train.dat')

    train_x = train_data[:, :4]
    train_y = train_data[:, [4]]

    train_x = np.concatenate(
        [np.ones((train_x.shape[0], 1)), train_x]
        , axis=1
    )

    w = np.zeros((1, 5))

    permutation = np.random.permutation(train_x.shape[0])

    update_time = 0
    while True:
        has_update = False
        for index in permutation:
            x = train_x[index]
            predict_y = sign(np.dot(w, x))
            if predict_y != train_y[index]:
                w = w - predict_y * x
                update_time += 1
                has_update = True
        if has_update == False:
            break
    print(update_time)
    return update_time


def learning_rate_permutate_cycly_pla():
    train_data = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_15_train.dat')

    train_x = train_data[:, :4]
    train_y = train_data[:, [4]]

    train_x = np.concatenate(
        [np.ones((train_x.shape[0], 1)), train_x]
        , axis=1
    )

    w = np.zeros((1, 5))

    permutation = np.random.permutation(train_x.shape[0])

    update_time = 0
    while True:
        has_update = False
        for index in permutation:
            x = train_x[index]
            predict_y = sign(np.dot(w, x))
            if predict_y != train_y[index]:
                w = w - 0.5 * predict_y * x
                update_time += 1
                has_update = True
        if has_update == False:
            break
    print(update_time)
    return update_time


def mistake_count(x, y, w):
    predict_y = np.dot(x, w.T)
    predict_y[predict_y == 0] = -1
    predict_y = np.sign(predict_y)
    return np.count_nonzero(predict_y != y)


def pocket_pla(max_update_time=50, use_pocket=True):
    train_data = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_18_train.dat')

    train_x = train_data[:, :4]
    train_y = train_data[:, [4]]

    train_x = np.concatenate(
        [np.ones((train_x.shape[0], 1)), train_x]
        , axis=1
    )

    w = np.zeros((1, 5))
    w_pocket = np.zeros((1, 5))

    update_time = 0
    while True:
        index = np.random.permutation(train_x.shape[0])[0]
        x = train_x[index]
        predict_y = sign(np.dot(w, x))
        if predict_y != train_y[index]:
            w = w - predict_y * x
            update_time += 1

            if mistake_count(train_x, train_y, w_pocket) > mistake_count(train_x, train_y, w):
                w_pocket = w

        if update_time >= max_update_time:
            break

    test_data = np.loadtxt('https://www.csie.ntu.edu.tw/~htlin/mooc/datasets/mlfound_math/hw1_18_test.dat')
    test_x = test_data[:, :4]
    test_y = test_data[:, [4]]
    test_x = np.concatenate(
        [np.ones((train_x.shape[0], 1)), test_x]
        , axis=1
    )
    if use_pocket:
        return mistake_count(test_x, test_y, w_pocket) / test_y.shape[0]
    else:
        return mistake_count(test_x, test_y, w) / test_y.shape[0]


if __name__ == '__main__':
    # cycle_pla()

    stat_sum = 0
    for _ in range(2000):
        # stat_sum += permutate_cycle_pla()
        stat_sum += learning_rate_permutate_cycly_pla()
        '''
        编写pocket pla代码时，需要注意numpy的+=赋值是替换赋值，也就是改变原数组，而不是生成新数组（对象），故会改变引用数组（对象）。
        调用对象内置方法不同
        change the array in place
        '''
        # stat_sum += pocket_pla()
        # stat_sum += pocket_pla(50, False)
        # stat_sum += pocket_pla(100)
        pass
    print(stat_sum / 2000)
