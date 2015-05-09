from .chart_component import ChartComponentDict


class Point(ChartComponentDict):

    def __init__(self):

        super(Point, self).__init__()

    def set_visibility(self, visible):

        self.config['show'] = str(visible).lower()