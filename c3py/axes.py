from .chart_component import ChartComponentDict
from .ticks import Ticks, XTicks, YTicks


class AxisPadding(ChartComponentDict):
    """
    Manipulate the padding of the axis.

    N.B. padding refers to the distance between the last tick of the axis and the end of the axis itself.

    :param axis: The axis object which this padding applies to.

    :type axis: c3py.axes.Axis
    """

    def __init__(self, axis):

        super(AxisPadding, self).__init__()

        self.axis = axis

    def set(self, location, padding_amount):
        """
        Set the axis padding.

        :param location: Which end of the axis to pad.

        :type location: str; x: ['left' | 'right']; y: ['bottom' | 'top']

        :param padding_amount: The amount by which to pad the axis. For the y axis, this is in pixels. For the x
            axis, this is in the units of the axis.

        :type padding_amount: int | float
        """

        if self.axis.axis_dimension == 'x' and location not in ['left', 'right']:
            raise Exception('for x axis, padding location must be "left" or "right".')

        elif self.axis.axis_dimension == 'y' and location not in ['bottom', 'top']:
            raise Exception('for y axis, padding location must be "bottom" or "top".')

        else:

            self.config[location] = padding_amount


class AxisLabel(ChartComponentDict):
    """
    Manipulate the label of the axis.

    :param axis: The axis object which this label applies to.

    :type axis: c3py.axes.Axis
    """

    def __init__(self, axis):

        super(AxisLabel, self).__init__()

        self.axis = axis

    def set(self, label_text, label_position=None):
        """
        Set the axis label.

        :param label_text: The text for the axis label.

        :type label_text: str

        :param label_position: The position of the axis label.

        :type label_position: str; default = None; x: ['inner-right' | 'inner-center' | 'inner-left' | 'outer-right' |
            'outer-center' | 'outer-left']; y: ['inner-top' | 'inner-middle' | 'inner-bottom' | 'outer-top' |
            'outer-middle' | 'outer-bottom']

        :return: None
        """

        if label_position is None:

            if self.axis.axis_dimension == 'x':
                label_position = 'outer-center'
            else:
                label_position = 'outer-middle'

        self.config['text'] = self.__string_wrap__(label_text)
        self.config['position'] = self.__string_wrap__(label_position)


class Axis(ChartComponentDict):
    """
    Manipulate an individual axis.

    :param axis_dimension: The dimension of the axis.

    :type axis_dimension: str; ['x' | 'y']
    """

    __axis__ = None

    padding = AxisPadding(__axis__)
    label = AxisLabel(__axis__)
    ticks = Ticks(__axis__)

    def __init__(self, axis_dimension):

        super(Axis, self).__init__()

        self.axis_dimension = axis_dimension

        if self.axis_dimension not in ['x', 'y']:
            raise Exception('axis_dimension must be either "x" or "y".')

        else:

            self.padding = AxisPadding(self)
            self.label = AxisLabel(self)

            if self.axis_dimension == 'x':
                self.ticks = XTicks(self)

            else:
                self.ticks = YTicks(self)

            self.config = {
                'show': 'true',
                'tick': self.ticks.config,
                'padding': self.padding.config,
                'label': self.label.config,
            }

    def set_visibility(self, visible):
        """
        Show or hide the axis.

        :param visible: Whether or not the axis should be visible.

        :type visible: bool

        :return: None
        """

        self.config['show'] = str(visible).lower()

    def __set_range_limit__(self, limit_type, value):

        if self.axis_dimension == 'x' and self.config['type'] != self.__string_wrap__('indexed'):

            self.config[limit_type] = self.__string_wrap__(value)

        else:

            self.config[limit_type] = value

    def set_range_min(self, minimum):
        """
        Set the minimum value for the axis.

        :param minimum: The minimum value for the axis.

        :type minimum: int | float

        :return: None
        """

        self.__set_range_limit__('min', minimum)

    def set_range_max(self, maximum):
        """
        Set the maximum value for the axis.

        :param maximum: The maximum value for the axis.

        :type maximum: int | float

        :return: None
        """

        self.__set_range_limit__('max', maximum)

    def set_range(self, minimum, maximum):
        """
        Set the range of values for the axis.

        :param minimum: The minimum value for the axis.

        :type minimum: int | float

        :param maximum: The maximum value for the axis.

        :type maximum: int | float

        :return: None
        """

        self.set_range_min(minimum)
        self.set_range_max(maximum)


class XAxis(Axis):
    """
    Manipulate the chart's x axis.
    """

    def __init__(self):

        super(XAxis, self).__init__('x')

        self.config['type'] = self.__string_wrap__('indexed')

    def set_type(self, axis_type):
        """
        Set the type of the x axis.

        :param axis_type: The type of the x axis.

        :type axis_type: str; ['indexed' | 'category'| 'timeseries']

        :return: None
        """

        if axis_type not in ['indexed', 'category', 'timeseries']:
            raise Exception('axis_type must be "indexed", "category", or "timeseries".')

        else:
            self.config['type'] = self.__string_wrap__(axis_type)

        if axis_type == 'timeseries':
            self.ticks.set_format('%Y-%m-%d')

    def set_height(self, height):
        """
        Set the height of the x axis, in pixels.

        :param height: The desired height of the x axis, in pixels.

        :type height: int

        :return: None
        """
        self.config['height'] = height


class YAxis(Axis):
    """
    Manipulate the chart's y axis.
    """

    def __init__(self):

        super(YAxis, self).__init__('y')

        self.padding.set('bottom', 0)
        self.padding.set('top', 0)


class Axes(ChartComponentDict):
    """
    Manipulate the chart's axes.
    """

    x_axis = XAxis()
    y_axis = YAxis()
    y2_axis = YAxis()

    def __init__(self):

        super(Axes, self).__init__()

        self.x_axis = XAxis()

        self.y_axis = YAxis()

        self.y2_axis = YAxis()
        self.y2_axis.set_visibility(False)

        self.config = {
            'x': self.x_axis.config,
            'y': self.y_axis.config,
            'y2': self.y2_axis.config,
        }

    def add_secondary_y(self):
        """
        Add a secondary y axis to the chart.

        :return: None
        """

        self.y2_axis.set_visibility(True)