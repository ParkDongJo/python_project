import pymysql as mysql
import datetime
import pandas as pd
import matplotlib.pyplot as plt


"""
mysql.server start
mysql -u root -p
"""

ID = 0
NAME = 1
PRICE = 2
DATE = 6


# set db conf
conn = mysql.connect(host='localhost',user='root',password='@Parkdj518',db='finance_crawl',charset='utf8')
cursor = conn.cursor()


def get_kospi(yearAt):
    try:

        query = "select * from kospi_stock WHERE createdAt >=%s and createdAt <=%s order by updn_rate desc"

        year = yearAt
        fromAt = datetime.date(year, 6, 1)
        toAt = datetime.date(year+1, 6, 1)

        cursor.execute(query,(fromAt,toAt))
        result = cursor.fetchall()

        return result
    except Exception:
        print(Exception)


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
        sum += float(item[5])

    return sum/len(group)



years = (2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017)

# years = (2013)
year_list = {}
gSum1 = 0
gSum2 = 0
gSum3 = 0
gSum4 = 0
gSum5 = 0

tot_index = ['그룹1','그룹2','그룹3','그룹4','그룹5']
tot_columns = ['평균']
total = []
val_columns = ['그룹1 평균','그룹2 평균','그룹3 평균','그룹4 평균','그룹5 평균']
val_index = ['2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
values = []

for yearAt in years:

    list = set_group(get_kospi(yearAt))
    ev_list = []
    for group in list:
        ev_list.append(calc_engage(group))

    year_list[yearAt] = ev_list


# print(year_list)


for yearAt in years:
    gSum1 += year_list[yearAt][0]
    gSum2 += year_list[yearAt][1]
    gSum3 += year_list[yearAt][2]
    gSum4 += year_list[yearAt][3]
    gSum5 += year_list[yearAt][4]

    values.append(year_list[yearAt])


total.append(gSum1/len(years))
total.append(gSum2/len(years))
total.append(gSum3/len(years))
total.append(gSum4/len(years))
total.append(gSum5/len(years))


vf = pd.DataFrame(values, index=val_index, columns=val_columns)
tf = pd.DataFrame(total, index=tot_index, columns=tot_columns)
print(vf)
print(tf)

conn.close()


def print_bar():

    data_x = ['1 Group','2 Group','3 Group','4 Group','5 Group']
    data_y1 = [total[0],0,0,0,0]
    data_y2 = [0,total[1],0,0,0]
    data_y3 = [0,0,total[2],0,0]
    data_y4 = [0,0,0,total[3],0]
    data_y5 = [0,0,0,0,total[4]]

    plt.bar(data_x, data_y1, label='Set 1', color='b')
    plt.bar(data_x, data_y2, label='Set 2', color='g')
    plt.bar(data_x, data_y3, label='Set 3', color='r')
    plt.bar(data_x, data_y4, label='Set 4', color='y')
    plt.bar(data_x, data_y5, label='Set 5', color='b')
    plt.legend()
    plt.title('Bar Chart')

    print(plt.show())


print_bar()