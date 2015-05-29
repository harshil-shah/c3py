from .chart_component import ChartComponentList


class Regions(ChartComponentList):
    """
    Highlight selected regions on the chart.

    Parameters
    ----------

    axes : c3py.axes.Axes

        The chart's Axes object.
    """
    def __init__(self, axes):

        super(Regions, self).__init__()

        self.axes = axes
        self.styles = []

    def add(self, name, axis, start, end, color):
        """
        Add a region to be highlighted on the chart.

        Parameters
        ----------

        name : str

            The name of the region. This will be the name of the CSS class that defines the region, therefore no two
            regions on the same chart should have the same name.

        axis : str

            The axis on which to highlight the region.

            **Accepts:** ['x' | 'y' | 'y2]

        start : must match x axis type

            The start position of the region.

        end : must match x axis type

            The start position of the region.

        color : str

            The color of the line. This can be a CSS named color, a hexadecimal value, or an RGB tuple.

        Returns
        -------
        None
        """
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