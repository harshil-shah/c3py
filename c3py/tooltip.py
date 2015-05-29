from .chart_component import ChartComponentDict


class TooltipFormat(ChartComponentDict):
    """
    Manipulate the format of the tooltip.
    """
    def __init__(self):

        super(TooltipFormat, self).__init__()

    def set_title(self, title):
        """
        Set the title of the tooltip. The variable 'x' can be used to refer to the x value at the tooltip.

        Parameters
        ----------

        title : str

            The title of the tooltip.

        Returns
        -------
        None

        Example
        -------

        .. code-block:: python

           chart.tooltip.tooltip_format.set_title('"value on x-axis = " + x')
        """
        self.config['title'] = 'function(x) {{ return {title}; }}'.format(
            title=title.replace('"', "'"),
        )


class Tooltip(ChartComponentDict):
    """
    Manipulate the chart's tooltip.

    Attributes
    ----------

    tooltip_format = c3py.tooltip.TooltipFormat
    """
    def __init__(self):

        super(Tooltip, self).__init__()

        self.tooltip_format = TooltipFormat()

        self.config = {
            'show': 'true',
            'grouped': 'true',
            'format': self.tooltip_format.config,
        }

    def hide(self):
        """
        Hide the tooltip on the chart.

        Returns
        -------
        None
        """
        self.config['show'] = 'false'

    def ungroup(self):
        """
        Ungroup the tooltips. When hovering at a point on a data series, only that series' tooltip will be shown,
        instead of all series' tooltips.

        Returns
        -------
        None
        """
        self.config['grouped'] = 'false'