from .chart_component import ChartComponentDict


class Grid(ChartComponentDict):

    def __init__(self, axes):

        super(Grid, self).__init__()

        self.axes = axes

        self.config = {
            'x': {
                'show': 'false',
                'lines': [],
            },
            'y': {
                'show': 'false',
                'lines': [],
            },
        }

    def show(self, x=True, y=True):

        self.config['x']['show'] = str(x).lower()

        self.config['y']['show'] = str(y).lower()

    def custom_grid_line(self, axis, value, label='', label_position='end'):

        if axis not in ['x', 'y', 'y2']:
            raise Exception('axis must be either "x", "y" or "y2".')

        elif label_position not in ['start', 'middle', 'end']:
            raise Exception('label_position must be either "start", "middle", or "end".')

        else:
            if axis == 'x' and self.axes.x_axis.config['type'] != self.__string_wrap__('indexed'):
                value = self.__string_wrap__(value)

            grid_line = {
                'value': value,
                'text': self.__string_wrap__(label),
                'position': self.__string_wrap__(label_position),
                'axis': self.__string_wrap__(axis),
            }

            trimmed_axis = axis[0]

            self.config[trimmed_axis]['lines'].append(grid_line)