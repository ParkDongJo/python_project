import datetime
from python_project.get_kospi import get_kospi


ID = 0
NAME = 1
PRICE = 2
DATE = 6

def set_group(data):
    group = []
    list = []
    for i in range(len(data)):
        group.append(data[i])

        if i%40 == 39:
            group.append(data[i])
            list.append(group)
            group = []

    return list


def calc_engage(group):
    sum = 0
    for item in group:
        sum += item[2]

    return sum/len(group)


all = get_kospi()


for row in all:
    standAt = datetime.datetime(2001, 6, 1, 0, 0)
    if row[DATE] == 0:
        print(row)

    list = set_group(get_kospi())
    ev_list = []
    for group in list:
        ev_list.append(calc_engage(group))

    year_list[yearAt] = ev_list


