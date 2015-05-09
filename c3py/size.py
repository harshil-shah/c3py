from .chart_component import ChartComponentDict


class Size(ChartComponentDict):

    def __init__(self):

        super(Size, self).__init__()

    def set_width(self, width):

        self.config['width'] = width

    def set_height(self, height):

        self.config['height'] = height

    def set(self, width, height):

        self.set_width(width)
        self.set_height(height)