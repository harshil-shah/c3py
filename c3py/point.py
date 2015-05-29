from .chart_component import ChartComponentDict


class Point(ChartComponentDict):
    """
    Control the points on line/area charts.
    """
    def __init__(self):

        super(Point, self).__init__()

    def set_visibility(self, visible):
        """
        Set the visibility of points.

        Parameters
        ----------

        visible : bool

            Whether or not the points should be visible.

        Returns
        -------
        None
        """
        self.config['show'] = str(visible).lower()