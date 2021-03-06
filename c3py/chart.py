from html import HTML
import json
from .data import Data
from .grid import Grid
from .axes import Axes
from .legend import Legend
from .tooltip import Tooltip
from .regions import Regions
from .point import Point
from .size import Size
from .padding import Padding


class Chart(object):
    """
    Create and modify a chart.

    Parameters
    ----------

    name : str

        The name of the chart. This will be the id of the div that holds the chart. Therefore no two charts in the
        same document should have the same name.

    local_jquery : str

        Path to a local version of jquery. If not provided, one hosted on a CDN is used.

        **Default:** None

    local_requirejs : str

        Path to a local version of requirejs. If not provided, one hosted on a CDN is used.

        **Default:** None

    local_d3_js : str

        Path to a local version of d3js. If not provided, one hosted on a CDN is used.

        **Default:** None

    local_c3_js : str

        Path to a local version of c3js. If not provided, one hosted on a CDN is used.

        **Default:** None

    local_c3_css : str

        Path to a local version of c3's css. If not provided, one hosted on a CDN is used.

        **Default:** None

    Attributes
    ----------

    axes : c3py.axes.Axes

    data : c3py.data.Data

    grid : c3py.grid.Grid

    legend : c3py.legend.Legend

    tooltip : c3py.tooltip.Tooltip

    regions : c3py.regions.Regions

    point : c3py.point.Point

    size : c3py.size.Size

    padding : c3py.padding.Padding
    """

    def __init__(self, name, local_jquery=None, local_requirejs=None, local_d3_js=None, local_c3_js=None,
                 local_c3_css=None):

        super(Chart, self).__init__()

        self.chart_html = HTML()

        self.name = name
        self.c3_css_path = local_c3_css or 'https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.10/c3.min.css'
        self.jquery_path = local_jquery or 'http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js'
        self.requirejs_path = local_requirejs or \
            'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.17/require.min.js'
        self.d3_js_path = local_d3_js or 'http://d3js.org/d3.v3.min'
        self.c3_js_path = local_c3_js or 'https://cdnjs.cloudflare.com/ajax/libs/c3/0.4.10/c3.min'

        self.chart_html.div('', id=self.name)
        self.chart_html.link('', href=self.c3_css_path, rel='stylesheet', type='text/css')
        self.chart_html.script('', src=self.jquery_path)
        self.chart_html.script('', src=self.requirejs_path)

        self.requirejs_config = {
            'paths': {
                'c3': self.c3_js_path,
                'd3': self.d3_js_path,
            }
        }

        self.axes = Axes()
        self.data = Data(self.axes)
        self.grid = Grid(self.axes)
        self.legend = Legend()
        self.tooltip = Tooltip()
        self.regions = Regions(self.axes)
        self.point = Point()
        self.size = Size()
        self.padding = Padding()

        self.chart_dict = {
            'bindto': "'#" + self.name + "'",
            'data': self.data.config,
            'axis': self.axes.config,
            'grid': self.grid.config,
            'legend': self.legend.config,
            'tooltip': self.tooltip.config,
            'regions': self.regions.config,
            'point': self.point.config,
            'size': self.size.config,
            'padding': self.padding.config,
        }

    def __get_main_styles_string__(self):

        style_string = ''

        for style in self.regions.styles:
            style_string += '''
                .c3-region.{name} {{
                    fill: {fill};
                }}
            '''.format(
                name=style['name'],
                fill=style['fill'],
            )

        return style_string

    def __get_main_script_string__(self):

        chart_dict_string = json.dumps(self.chart_dict).replace('"', '')

        script = '''
            require.config({requirejs_config});

            require(["d3", "c3"], function(d3, c3) {{
                var chart = c3.generate({chart_dict});
            }});
        '''.format(
            requirejs_config=json.dumps(self.requirejs_config),
            chart_dict=chart_dict_string,
        )

        return script

    def get_html_string(self):
        """
        Return the HTML string which will draw the chart.

        In a Jupyter notebook, this would usually be used as the argument for IPython.display.HTML(),
        for the interactive chart to be displayed in the notebook.

        That is, IPython.display.HTML(chart.get_html_string()).

        Returns
        -------
        str
        """

        styles = self.__get_main_styles_string__()
        script = self.__get_main_script_string__()

        self.chart_html.style(styles)
        self.chart_html.script(script, type='text/javascript')

        return unicode(self.chart_html)