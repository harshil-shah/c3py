from .chart_component import ChartComponentList


class Regions(ChartComponentList):

    def __init__(self, axes):

        super(Regions, self).__init__()

        self.axes = axes
        self.styles = []

    def add(self, name, axis, start, end, color):

        if axis not in ['x', 'y', 'y2']:
            raise Exception('axis must be either "x", "y" or "y2".')

        else:
            if axis == 'x' and self.axes.x_axis.config['type'] != self.__string_wrap__('indexed'):
                start = self.__string_wrap__(start)
                end = self.__string_wrap__(end)

            self.config.append({
                'class': self.__string_wrap__(name),
                'axis': self.__string_wrap__(axis),
                'start': start,
                'end': end,
            })

            self.styles.append({
                'name': name,
                'fill': color,
            })