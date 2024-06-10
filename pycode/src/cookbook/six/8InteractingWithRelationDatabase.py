# 同关系型数据库交互
import sqlite3

db = sqlite3.connect('database.db')

c = db.cursor()
c.execute('create table dalq_table (id integer, name text)')

datas = [(1, 'ada'), (2, 'bob'), (3, 'charles')]
c.executemany('insert into dalq_table values(?, ?)', datas)
db.commit()

for row in db.execute('select * from dalq_table'):
    print(row)