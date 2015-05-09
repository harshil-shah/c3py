from .chart_component import ChartComponentDict


class Data(ChartComponentDict):

    def __init__(self, axes):

        super(Data, self).__init__()

        self.axes = axes

        self.config = {
            'xs': {},
            'columns': [],
            'types': {},
            'axes': {},
            'groups': [],
            'labels': {'format': {}},
            'colors': {},
        }

    def __add_xy_series__(self, x, y, label, chart_type, axis, color):

        if axis not in ['y', 'y2']:
            raise Exception('axis must be "y" or "y2".')

        else:

            x_label = 'x' + label

            self.config['xs'][self.__string_wrap__(label)] = self.__string_wrap__(x_label)

            if self.axes.x_axis.config['type'] != self.__string_wrap__('indexed'):
                self.config['columns'].append([self.__string_wrap__(x_label)] + [self.__string_wrap__(i) for i in x])
            else:
                self.config['columns'].append([self.__string_wrap__(x_label)] + x)

            self.config['columns'].append([self.__string_wrap__(label)] + y)
            self.config['types'][label] = self.__string_wrap__(chart_type)
            self.config['axes'][label] = self.__string_wrap__(axis)

            if color is not None:

                self.config['colors'][label] = self.__string_wrap__(color)

    def line(self, x, y, label, axis='y', color=None, spline=False, step=False):

        if spline and step:
            raise Exception('Both spline and step cannot be true.')
        elif spline and not step:
            chart_type = 'spline'
        elif step and not spline:
            chart_type = 'step'
        else:
            chart_type = 'line'

        self.__add_xy_series__(x, y, label, chart_type, axis, color)

    def area(self, x, y, label, axis='y', color=None, spline=False, step=False):

        if spline and step:
            raise Exception('Both spline and step cannot be true.')
        elif spline and not step:
            chart_type = 'area-spline'
        elif step and not spline:
            chart_type = 'area-step'
        else:
            chart_type = 'area'

        self.__add_xy_series__(x, y, label, chart_type, axis, color)

    def bar(self, x, y, label, axis='y', color=None):

        chart_type = 'bar'

        self.__add_xy_series__(x, y, label, chart_type, axis, color)

    def scatter(self, x, y, label, axis='y', color=None):

        chart_type = 'scatter'

        self.__add_xy_series__(x, y, label, chart_type, axis, color)

    def group_series(self, labels):

        self.config['groups'].append([self.__string_wrap__(i) for i in labels])

    def add_labels(self, series_name, label_format=''):

        self.config['labels']['format'][series_name] = "d3.format('{label_format}')".format(
            label_format=label_format
        )