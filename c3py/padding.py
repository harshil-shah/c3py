from .chart_component import ChartComponentDict


class Padding(ChartComponentDict):

    def __init__(self):

        super(Padding, self).__init__()

    def set_left(self, left):

        self.config['left'] = left

    def set_right(self, right):

        self.config['right'] = right

    def set_top(self, top):

        self.config['top'] = top

    def set_bottom(self, bottom):

        self.config['bottom'] = bottom

    def set(self, left, right, top, bottom):

        self.set_left(left)
        self.set_right(right)
        self.set_top(top)
        self.set_bottom(bottom)