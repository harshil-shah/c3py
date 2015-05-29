from .chart_component import ChartComponentDict


class Padding(ChartComponentDict):
    """
    Control the padding around the chart.
    """
    def __init__(self):

        super(Padding, self).__init__()

    def set_left(self, left):
        """
        Set the chart's left padding.

        Parameters
        ----------

        left : int

            The chart's left padding.

        Returns
        -------
        None
        """
        self.config['left'] = left

    def set_right(self, right):
        """
        Set the chart's right padding.

        Parameters
        ----------

        right : int

            The chart's right padding.

        Returns
        -------
        None
        """
        self.config['right'] = right

    def set_top(self, top):
        """
        Set the chart's top padding.

        Parameters
        ----------

        top : int

            The chart's top padding.

        Returns
        -------
        None
        """
        self.config['top'] = top

    def set_bottom(self, bottom):
        """
        Set the chart's bottom padding.

        Parameters
        ----------

        bottom : int

            The chart's bottom padding.

        Returns
        -------
        None
        """
        self.config['bottom'] = bottom

    def set(self, left, right, top, bottom):
        """
        Set the chart's padding.

        Parameters
        ----------

        left : int

            The chart's left padding.

        right : int

            The chart's right padding.

        top : int

            The chart's top padding.

        bottom : int

            The chart's bottom padding.

        Returns
        -------
        None
        """
        self.set_left(left)
        self.set_right(right)
        self.set_top(top)
        self.set_bottom(bottom)