import pymysql

db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='pythondb')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
# 1.查看数据库版本
data = cursor.fetchone()
print("数据库版本:",data)
# 2.创建新表
cursor.execute('CREATE TABLE IF NOT EXISTS students (id VARCHAR(255) NOT NULL,name VARCHAR (255) NOT NULL ,age INT NOT NULL,PRIMARY KEY (id))')
# 3.插入数据
id = 20180606
user = 'jack'
age = 18
try:
    cursor.execute('INSERT INTO students(id,user,age) values (%s,%s,%s)',(id,user,age))
    db.commit()  # commit()方法才能实现数据插入 更新  删除操作，操作数据库的函数
except:
    db.rollback() # 这里加了一层异常处理，如果执行失败，rollback()执行数据回滚，相当于什么都没发生过，事务：原子性 一致性 隔离性 持久性
# 4.插入数据的另一种写法
data = {
    'id':'200180909',
    'name':'jerry',
    'age':20
}
table = 'students'
keys = ','.join(data.keys()) # join()方法将序列中的元素以指定的字符连接生成一个新的字符串。
values = ','.join(['%s']*len(data))
sql4 = 'INSERT INTO {table }({keys}) VALUES ({values })'.format(table=table,keys=keys,values=values)
try:
    if cursor.execute(sql4,tuple(data.values())):
        print("成功")
        db.commit()
except:
    print("失败")
    db.rollback()
# 5.更新数据
db.close()