from .chart_component import ChartComponentDict


class Legend(ChartComponentDict):
    """
    Manipulate the chart's legend.
    """
    def __init__(self):

        super(Legend, self).__init__()

        self.config = {
            'show': 'true',
            'hide': 'false',
            'position': self.__string_wrap__('bottom'),
        }

    def hide(self):
        """
        Hide the chart's legend.

        Returns
        -------
        None
        """
        self.config['show'] = 'false'
        self.config['hide'] = 'true'

    def hide_series(self, series_to_hide):
        """
        Hide a specific series from the legend.

        Parameters
        ----------

        series_to_hide : str

            The name of the series to hide.

        Returns
        -------
        None
        """
        if type(series_to_hide) is not list:
            raise Exception('series_to_hide must be a list of series names.')

        else:
            self.config['hide'] = [self.__string_wrap__(i) for i in series_to_hide]

    def set_position(self, legend_position, inset_anchor=None):
        """
        Set the position of the legend.

        Parameters
        ----------

        legend_position : str

            The position of the legend.

            **Accepts:** ['bottom' | 'right' | 'inset']

        inset_anchor : str

            If legend_position is set to 'inset', this parameter states where the legend should be anchored to.

            **Accepts:** ['top-left' | 'top-right' | 'bottom-left' | 'bottom-right']

        Returns
        -------
        None
        """
        if legend_position not in ['bottom', 'right', 'inset']:
            raise Exception('legend_position must be one of "bottom", "right", "inset".')

        elif legend_position != 'inset' and inset_anchor is not None:
            raise Exception('inset_anchor must be None if legend_position != "inset".')

        elif legend_position == 'inset' and inset_anchor not in ['top-left', 'top-right', 'bottom-left',
                                                                 'bottom-right']:
            raise Exception('inset_anchor must be one of "top-left", "top-right", "bottom-left", "bottom-right".')

        else:
            self.config['position'] = self.__string_wrap__(legend_position)

            if legend_position == 'inset' and inset_anchor is not None:

                self.config['inset'] = {
                    'anchor': self.__string_wrap__(inset_anchor),
                }