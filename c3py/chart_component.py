class ChartComponent(object):

    def __init__(self):

        self.config = {}

    def __string_wrap__(self, string_to_wrap):

        return "'" + str(string_to_wrap) + "'"
        

class ChartComponentDict(ChartComponent):

    def __init__(self):

        super(ChartComponentDict, self).__init__()


class ChartComponentList(ChartComponent):

    def __init__(self):

        super(ChartComponentList, self).__init__()

        self.config = []