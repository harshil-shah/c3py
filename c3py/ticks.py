from .chart_component import ChartComponentDict


class Ticks(ChartComponentDict):
    """
    Manipulate the axis ticks.

    :param axis: The axis object to which the ticks belong.

    :type axis: c3py.axes.Axis
    """

    def __init__(self, axis):

        super(Ticks, self).__init__()

        self.axis = axis

    def set_format(self, tick_format):
        """
        Set the formatting of the tick labels. See https://github.com/mbostock/d3/wiki/Formatting for formatting
        numbers, and https://github.com/mbostock/d3/wiki/Time-Formatting for formatting dates / times.

        :param tick_format: The formatting of the tick labels.

        :type tick_format: str

        :return: None
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

        :param tick_count: The desired number of ticks.

        :type tick_count: int

        :return: None
        """

        self.config['count'] = tick_count

    def set_values(self, tick_values):
        """
        Set the values of the ticks.

        :param tick_values: A list of tick values.

        :type tick_values: list

        :return: None
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

        :param max_ticks: The maximum number of x tick labels to be displayed.

        :type max_ticks: int

        :return: None
        """

        self.config['culling'] = {
            'max': max_ticks,
        }

    def rotate(self, degrees):
        """
        Rotate the x tick labels.

        :param degrees: The number of degrees by which to rotate the x tick labels.

        :type degrees: int; between 0 and 360

        :return: None
        """

        self.config['rotate'] = degrees

    def set_multiline(self, multiline):
        """
        Control whether or not the x tick labels should occupy multiple lines.

        :param multiline: Whether or not the x tick labels should occupy multiple lines

        :type multiline: bool

        :return: None
        """

        self.config['multiline'] = str(multiline).lower()

    def set_fit(self, fit):
        """
        Fit x axis ticks. If true set, the ticks will be positioned nicely. If false set, the ticks will be
        positioned according to x value of the data points.

        :param fit: Whether or not to fit x axis ticks.

        :type fit: bool

        :return: None
        """

        self.config['fit'] = str(fit).lower()


class YTicks(Ticks):

    def __init__(self, axis):

        super(YTicks, self).__init__(axis)