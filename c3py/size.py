from .chart_component import ChartComponentDict


class Size(ChartComponentDict):
    """
    Control the size of the chart.
    """
    def __init__(self):

        super(Size, self).__init__()

    def set_width(self, width):
        """
        Set the width of the chart.

        Parameters
        ----------

        width : int

            The width of the chart.

        Returns
        -------
        None
        """
        self.config['width'] = width

    def set_height(self, height):
        """
        Set the height of the chart.

        Parameters
        ----------

        height : int

            The height of the chart.

        Returns
        -------
        None
        """
        self.config['height'] = height

    def set(self, width, height):
        """
        Set the size of the chart.

        Parameters
        ----------

        width : int

            The width of the chart.

        height : int

            The height of the chart.

        Returns
        -------
        None
        """
        self.set_width(width)
        self.set_height(height)