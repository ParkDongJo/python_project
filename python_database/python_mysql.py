import pymysql as mysql


conn = mysql.connect(host='localhost',user='root',password='@Parkdj518',db='finance_crawl',charset='utf8')
cursor = conn.cursor()


"""
inster query 
"""

query = 'insert into test (id,name) values (%s,%s)'
data = (
    (4,'max'),
)
cursor.executemany(query,data)


"""
select query 
"""
query = 'select * from test'
cursor.execute(query)

rows = cursor.fetchall()

print(rows)




conn.close()