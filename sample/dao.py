from sample.Domain import Line, Stop, Time
from sample.definitions import ROOT_DIR


class Dao:
    char_split = ","

    def get_rows(self, fname):
        with open(fname, 'r') as f:
            content = f.readlines()

        f.close()
        # remove white chars and 1st line
        content = [content[i].strip() for i in range(len(content)) if i > 0]
        return content

    def get_el(self, line, index):
        return line.split(self.char_split)[index]


class LineDao(Dao):
    fname = ROOT_DIR + "/resources/lines.csv"

    def get_line_by_id(self, idd):
        lines = self.get_rows(self.fname)

        for l in lines:
            if int(self.get_el(l, 0)) == idd:
                els = l.split(self.char_split)
                return Line(int(els[0]), els[1])

    def get_line_by_ids(self, ids):
        rows = self.get_rows(self.fname)

        lines = []
        for l in rows:
            for idd in ids:
                if int(self.get_el(l, 0)) == idd:
                    els = l.split(self.char_split)
                    lines.append(Line(int(els[0]), els[1]))
        return lines


class StopDao(Dao):
    fname = ROOT_DIR + "/resources/stops.csv"

    def get_by_ids(self, ids):
        rows = self.get_rows(self.fname)

        stops = []
        for l in rows:
            for idd in ids:
                if int(self.get_el(l, 0)) == idd:
                    els = l.split(self.char_split)
                    stops.append(Stop(int(els[0]), int(els[1]), int(els[2])))
        return stops


class TimeDao(Dao):
    fname = ROOT_DIR + "/resources/times.csv"

    def get_by_time(self, time):
        rows = self.get_rows(self.fname)

        times = []
        for l in rows:
            if self.get_el(l, 2) == time:
                els = l.split(self.char_split)
                times.append(Time(int(els[0]), int(els[1]), els[2]))

        return times


class DelayDao(Dao):
    fname = ROOT_DIR + "/resources/delays.csv"

    def is_line_delayed(self, name):
        rows = self.get_rows(self.fname)

        for l in rows:
            if self.get_el(l, 0) == name:
                return int(self.get_el(l, 1)) > 0
        return False


