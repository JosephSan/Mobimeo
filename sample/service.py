from sample.dao import TimeDao, StopDao, LineDao, DelayDao


class Service:

    def __init__(self):
        self.timeDao = TimeDao()
        self.stopDao = StopDao()
        self.lineDao = LineDao()
        self.delayDao = DelayDao()

    def get_by_time_stop(self, time, x, y):
        times = self.timeDao.get_by_time(time);

        if not times:
            raise FileNotFoundError("No Train stops at", time)

        line_ids = []
        stops = self.stopDao.get_by_ids(set([time.stop for time in times]))
        for t in times:
            for s in stops:
                if s.id == t.stop and s.x == x and s.y == y:
                    line_ids.append(t.line)

        return self.lineDao.get_line_by_ids(line_ids)

    def is_line_delayed(self, name):
        return self.delayDao.is_line_delayed(name)




