
class Line:
    def __init__(self, idd, name):
        self.id = idd
        self.name = name


class Delay:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Time:
    def __init__(self, line, stop, value):
        self.line = line
        self.stop = stop
        self.value = value


class Stop:
    def __init__(self, idd, x, y):
        self.id = idd
        self.x = x
        self.y = y