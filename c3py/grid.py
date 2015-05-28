from .chart_component import ChartComponentDict


class Grid(ChartComponentDict):
    """
    Manipulate the chart's grid.

    Parameters
    ----------

    axes : c3py.axes.Axes

        The chart's axes object.
    """
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
        """
        Display a grid on the chart.

        Parameters
        ----------

        x : bool, optional

            Whether or not to display the x grid.

            **Default:** True

        y : bool, optional

            Whether or not to display the y grid.

            **Default:** True

        Returns
        -------
        None
        """
        self.config['x']['show'] = str(x).lower()

        self.config['y']['show'] = str(y).lower()

    def custom_grid_line(self, axis, value, label='', label_position='end'):
        """
        Add a custom grid line to the chart.

        Parameters
        ----------

        axis : str

            The axis on which to display the custom grid line.

            **Accepts:** ['x' | 'y' | 'y2']

        value : must match x axis type

            The value at which to display the custom grid line.

        label : str, optional

            The label to display with the custom grid line.

            **Default:** ''

        label_position : str, optional

            The position on the grid line at which to display the label.

            **Default:** 'end'

            **Accepts:** ['start' | 'middle' | 'end']

        Returns
        -------
        None
        """
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