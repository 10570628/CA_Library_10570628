class Library:
    """A sample Library class"""

    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last
        



    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.middle)

    def __repr__(self):
        return "Library('{}', '{}', {})".format(self.first, self.middle, self.last)




