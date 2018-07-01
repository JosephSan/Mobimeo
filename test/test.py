from sample.dao import Dao, LineDao, StopDao, TimeDao
from sample.definitions import ROOT_DIR
from sample.service import Service

import re

directory = ROOT_DIR + "/resources/"
d = Dao()

def open_file():
    fname = directory + "delays.csv"
    f = d.get_rows(fname)
    print("file_content : ")
    [print(f[i]) for i in range(len(f))]


def test_new_line():
    lineDao = LineDao()
    line = lineDao.get_line_by_id(0)
    print(line.id, line.name)

def test_stops_get_by_ids():
    stopDao = StopDao()
    s = stopDao.get_by_ids([8,9])
    return "OK" if len(s) ==  2 else "KO"

def test_new_time():
    timeDao = TimeDao()
    times = timeDao.get_by_time("10:08:00")
    #[print(t.line, t.stop, t.value) for t in times]
    return "OK" if len(times) == 2 else "KO"

def test_get_line_by_ids():
    lineDao = LineDao()
    lines = lineDao.get_line_by_ids([0, 1])
    return "OK" if len(lines) == 2 else "KO"

def test_service_get_stop_2results():
    service = Service()
    lines = service.get_by_time_stop("10:08:00", 2, 9)
    return "OK" if len(lines) == 2 else "KO"

def test_service_get_stop_1result():
    service = Service()
    lines = service.get_by_time_stop("10:09:00", 3, 11)
    #[print(l.id, l.name) for l in lines]
    return "OK" if len(lines) == 1 else "KO"






print("test_new_time", test_new_time())
print("test_stops_get_by_ids", test_stops_get_by_ids())
print("test_test_get_line_by_ids", test_get_line_by_ids())
print("test_service_get_stop_2results", test_service_get_stop_2results())
print("test_service_get_stop_1result", test_service_get_stop_1result())



