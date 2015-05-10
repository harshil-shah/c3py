from .chart_component import ChartComponentDict


class Ticks(ChartComponentDict):

    def __init__(self, axis):

        super(Ticks, self).__init__()

        self.axis = axis

    def set_format(self, tick_format):

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

        self.config['count'] = tick_count

    def set_values(self, tick_values):

        if self.axis.axis_dimension == 'x' and self.axis.config['type'] != self.__string_wrap__('indexed'):
            tick_values = [self.__string_wrap__(i) for i in tick_values]

        self.config['values'] = tick_values


class XTicks(Ticks):

    def __init__(self, axis):

        super(XTicks, self).__init__(axis)

    def cull(self, max_ticks):

        self.config['culling'] = {
            'max': max_ticks,
        }

    def rotate(self, degrees):

        self.config['rotate'] = degrees

    def set_multiline(self, multiline):

        self.config['multiline'] = str(multiline).lower()

    def set_fit(self, fit):

        self.config['fit'] = str(fit).lower()


class YTicks(Ticks):

    def __init__(self, axis):

        super(YTicks, self).__init__(axis)