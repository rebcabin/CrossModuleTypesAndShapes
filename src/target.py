
class ArbitraryType(object):
    def __init__(self):
        self.arbitrary_attribute = 42
        pass

def is_arbitrary_type(some_type):
    return some_type is ArbitraryType