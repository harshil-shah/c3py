from .chart_component import ChartComponentDict


class TooltipFormat(ChartComponentDict):

    def __init__(self):

        super(TooltipFormat, self).__init__()

    def set_title(self, title):

        self.config['title'] = 'function(x) {{ return {title}; }}'.format(
            title=title.replace('"', "'"),
        )


class Tooltip(ChartComponentDict):

    def __init__(self):

        super(Tooltip, self).__init__()

        self.tooltip_format = TooltipFormat()

        self.config = {
            'show': 'true',
            'grouped': 'true',
            'format': self.tooltip_format.config,
        }

    def hide(self):

        self.config['show'] = 'false'

    def ungroup(self):

        self.config['grouped'] = 'false'