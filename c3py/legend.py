from .chart_component import ChartComponentDict


class Legend(ChartComponentDict):

    def __init__(self):

        super(Legend, self).__init__()

        self.config = {
            'show': 'true',
            'hide': 'false',
            'position': self.__string_wrap__('bottom'),
        }

    def hide(self):

        self.config['show'] = 'false'
        self.config['hide'] = 'true'

    def hide_series(self, series_to_hide):

        if type(series_to_hide) is not list:
            raise Exception('series_to_hide must be a list of series names.')

        else:
            self.config['hide'] = [self.__string_wrap__(i) for i in series_to_hide]

    def set_position(self, legend_position, inset_anchor=None):

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