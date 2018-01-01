"""

1차 요청 URL>
http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx?

>>입력값 20140613 일 시
bld:MKD/03/0304/03040101/mkd03040101T3_01
name:form
_:1511625134644

>>입력값 20150613
bld:MKD/03/0304/03040101/mkd03040101T3_01
name:form
_:1511625134645

>>입력값 20170613
bld:MKD/03/0304/03040101/mkd03040101T3_01
name:form
_:1511625134646
MKD/03/0304/03040101/mkd03040101T3_01

1차 응답값>
DTdx/go1PxVkQ0orKEklB2I0ug+UlqZgG2rMyAPDpiI31cxd2ZlPgHos9zomaRM2+INL2h+ChNzbvf/bdIScPbzCJWTWNJ0RDubP0FzpRCBum6HDnJTnN0a8D5pDJ8d6oO5lIJOxz5ZHNEMJPz73+g==

2차 요청 URL>
http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx

2차 요청 시 Header 파라미터>
ind_tp_cd:1
idx_ind_cd:028
lang:ko
compst_isu_tp:1
schdate:20140613
fromdate:20171117
todate:20171124
pagePath:/contents/MKD/03/0304/03040101/MKD03040101T3.jsp
code:DTdx/go1PxVkQ0orKEklB2I0ug+UlqZgG2rMyAPDpiI31cxd2ZlPgHos9zomaRM2+INL2h+ChNzbvf/bdIScPbzCJWTWNJ0RDubP0FzpRCBum6HDnJTnN0a8D5pDJ8d6oO5lIJOxz5ZHNEMJPz73+g==


2차 응답값>
{"output":[{"isu_cd":"138930", ...}]}

2차 응답값이 내가 뽑고자 하는 목표값,
2차 응답값을을 파싱해서 리스트를 만들고 해당 리스트를 DB에 넣는다.


1. 응답값을 적절한 자료구조(튜플,리스트,딕셔너리)에 담는다.
2. 담은 자료구조의 데이터를 반복 요청을 통해 DB에 넣는다.
3. 1년 간거의 데이터 값을 가져와 그룹을 만든다.
4. 그리고 다음해 순위랑 매칭하여, true(상위권 유지) / false(하위권으로 하락) 결과값으로 변환한다

"""

import requests
import time
import json
from bs4 import BeautifulSoup
import pymysql as mysql
import datetime


# set tarket Date
date = [2017,6,1]
# req header
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
# set db conf
conn = mysql.connect(host='localhost',user='root',password='@Parkdj518',db='finance_crawl',charset='utf8')
cursor = conn.cursor()

def get_day_idx(y,m,d):
    return datetime.date(y, m, d).weekday()

def get_sec_thu(y,m,d):
    cnt = 0
    for i in range(d, 16):
        if get_day_idx(y, m, i) == 3:
            cnt += 1
            if cnt == 2:
                result = i
                break

    return result


def insert_kospi(atYears,m,d):
    target = str(get_sec_thu(atYears,m,d))
    target = target.zfill(2)
    d = get_sec_thu(atYears,m,d)

    print(target)

    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    param = {
        "ind_tp_cd":"1",
        "idx_ind_cd":"028",
        "lang":"ko",
        "compst_isu_tp":"1",
        "schdate":str(atYears)+"06"+target,
        "fromdate":str(atYears)+"0614",
        "todate":str(atYears+1)+"0613",
        "pagePath":"/contents/MKD/03/0304/03040101/MKD03040101T3.jsp",
        "code":"MbmVKCh79BD5E9+/KZcWnjBCv9cWdaWoq24KBa2hdZ6gbOcdXGAecP3ZUHFIDnvOHVdTQ/p4DBOmAThQEZQgI/6zBHDgM8EUdIp3MrCaEr1V44cmDiRNkpm6we4qc1b8DEW+V0i3tYU8Gp2aEHRDlA=="
    }

    # time.sleep(5)
    req = requests.post("http://marketdata.krx.co.kr/contents/MKD/99/MKD99000001.jspx",param,headers = headers)
    print(req.text)
    output = json.loads(req.text)

    if req.status_code == 200:

        try:
            for item in output["output"]:
                isu = (
                    str(item['isu_cd']),
                    str(item['isu_nm']),
                    int(item['tdd_clsprc'] != '-' and item['tdd_clsprc'].replace(',', '').strip() or 0),
                    str(item['acc_trdval']),
                    str(item['mktcap']),
                    str(item['updn_rate']),
                    datetime.date(atYears, m, d).strftime('%Y-%m-%d %H:%M:%S'),
                    timestamp
                )

                print(isu)

                query = "insert into kospi_stock (isu_cd,isu_nm,tdd_clsprc,acc_trdval,mktcap,updn_rate,createdAt,crawledAt) values (%s,%s,%s,%s,%s,%s,%s,%s)"

                cursor.execute(query, isu)
                conn.commit()
        except Exception:
            print(Exception)
            print(item)

        finally:
            conn.close()
    else:
        # 실패 시 재시도
        insert_kospi(atYears)


insert_kospi(date[0],date[1],date[2])


