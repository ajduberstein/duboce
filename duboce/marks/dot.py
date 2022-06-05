from .plottable import Plottable


class Dot(Plottable):
    def __init__(self, data, **kwargs):
        super().__init__(data, **kwargs)
