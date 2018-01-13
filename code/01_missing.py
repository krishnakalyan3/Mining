#!/usr/bin/env python3

#!/usr/bin/env python3

import sys
sys.path.append("../")
import pandas as pd
from param_config import config
from utils import write_data
import numpy as np
from sklearn.utils import shuffle
np.random.seed(config.set_seed)


def get_missing(data):
    missing_cols = data.columns[data.isnull().any()]
    return missing_cols


def create_missing(missing_cols, df):
    for i in missing_cols:
        header_str = 'missing_{}'.format(i)
        df[header_str] = df[i].isnull().astype(int)
    return df


def total_missing(train, test):
    header_str = 'total_missing'
    train[header_str] = train.isnull().sum(axis=1)
    test[header_str] = test.isnull().sum(axis=1)
    return train, test


def missing(x_train, x_test):
    train_missing = get_missing(x_train)
    test_missing = get_missing(x_test)
    assert len(train_missing) == len(test_missing)

    train = create_missing(train_missing.values, x_train)
    test = create_missing(train_missing.values, x_test)

    train, test = total_missing(train, test)
    return train, test


if __name__ == '__main__':
    train_x = pd.read_csv(config.train_file)
    test_x = pd.read_csv(config.test_file)

    # Shuffle training data
    train_x = shuffle(train_x, random_state=config.set_seed)
    train_x, test_x = missing(train_x, test_x)

    print('#### Writing Pickle 01: Missing ####')
    write_data(config.a_xtrain, train_x)
    write_data(config.a_xtest, test_x)
