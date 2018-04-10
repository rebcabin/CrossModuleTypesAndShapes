import numpy as np

from src.target import ArbitraryType
from src.target import is_arbitrary_type
from src.target import is_rank_one_tensor


def test_type_locally():
    a = ArbitraryType()
    assert type(a) is ArbitraryType


def test_type_other_module():
    a = ArbitraryType()
    assert is_arbitrary_type(type(a))


def test_shape_other_module():
    na = np.array([ArbitraryType(), ArbitraryType()])
    assert is_rank_one_tensor(na)