from .chart_component import ChartComponentDict


class Ticks(ChartComponentDict):
    """
    Manipulate the axis ticks.

    Parameters
    ----------

    axis : c3py.axes.Axis

        The axis object to which the ticks belong.
    """

    def __init__(self, axis):

        super(Ticks, self).__init__()

        self.axis = axis

    def set_format(self, tick_format):
        """
        Set the formatting of the tick labels. See https://github.com/mbostock/d3/wiki/Formatting for formatting
        numbers, and https://github.com/mbostock/d3/wiki/Time-Formatting for formatting dates / times.

        Parameters
        ----------

        tick_format : str

            The formatting of the tick labels.

        Returns
        -------
        None
        """

        if self.axis.axis_dimension == 'x':
            if self.axis.config['type'] == self.__string_wrap__('timeseries'):
                format_str = "d3.time.format({tick_format})"
            else:
                format_str = "d3.format({tick_format})"

        else:
            format_str = "d3.format({tick_format})"

        self.config['format'] = format_str.format(
            tick_format=self.__string_wrap__(tick_format),
        )

    def set_count(self, tick_count):
        """
        Set the number of ticks on the axis.

        Parameters
        ----------

        tick_count : int

            The desired number of ticks.

        Returns
        -------
        None
        """

        self.config['count'] = tick_count

    def set_values(self, tick_values):
        """
        Set the values of the ticks.

        Parameters

        tick_values : list

            A list of tick values.

        Returns
        -------
        None
        """

        if self.axis.axis_dimension == 'x' and self.axis.config['type'] != self.__string_wrap__('indexed'):
            tick_values = [self.__string_wrap__(i) for i in tick_values]

        self.config['values'] = tick_values


class XTicks(Ticks):

    def __init__(self, axis):

        super(XTicks, self).__init__(axis)

    def cull(self, max_ticks):
        """
        Limit the number of x tick labels displayed.

        Parameters
        ----------

        max_ticks : int

            The maximum number of x tick labels to be displayed.

        Returns
        -------
        None
        """

        self.config['culling'] = {
            'max': max_ticks,
        }

    def rotate(self, degrees):
        """
        Rotate the x tick labels.

        Parameters
        ----------

        degrees : int

            The number of degrees by which to rotate the x tick labels.

        Returns
        -------
        None
        """

        self.config['rotate'] = degrees

    def set_multiline(self, multiline):
        """
        Control whether or not the x tick labels should occupy multiple lines.

        Parameters
        ----------

        multiline : bool

            Whether or not the x tick labels should occupy multiple lines

        Returns
        -------
        None
        """

        self.config['multiline'] = str(multiline).lower()

    def set_fit(self, fit):
        """
        Fit x axis ticks. If true set, the ticks will be positioned nicely. If false set, the ticks will be
        positioned according to x value of the data points.

        Parameters
        ----------

        fit : bool

            Whether or not to fit x axis ticks.

        Returns
        -------
        None
        """

        self.config['fit'] = str(fit).lower()


class YTicks(Ticks):

    def __init__(self, axis):

        super(YTicks, self).__init__(axis)