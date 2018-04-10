from src.target import ArbitraryType
from src.target import is_arbitrary_type


def test_type_locally():
    a = ArbitraryType()
    assert type(a) is ArbitraryType


def test_type_other_module():
    a = ArbitraryType()
    assert is_arbitrary_type(type(a))