import numpy as np


class ArbitraryType(object):
    def __init__(self):
        self.arbitrary_attribute = 42
        pass


def is_arbitrary_type(some_type):
    return some_type is ArbitraryType


def is_rank_one_tensor(some_object):
    return len(np.shape(some_object)) == 1