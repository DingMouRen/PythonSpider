import pymysql

db = pymysql.connect(host='localhost',user='root',password='root',port=3306,db='pythondb')
cursor = db.cursor()
cursor.execute('SELECT VERSION()')
# 1.查看数据库版本
data1 = cursor.fetchone()
print("数据库版本:",data1)
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
data4 = {
    'id':'200180909',
    'name':'jerry',
    'age':20
}
table4 = 'students'
keys4 = ','.join(data4.keys()) # join()方法将序列中的元素以指定的字符连接生成一个新的字符串。
values4 = ','.join(['%s']*len(data4))
sql4 = 'INSERT INTO {table }({keys}) VALUES ({values })'.format(table=table4,keys=keys4,values=values4)
try:
    if cursor.execute(sql4,tuple(data4.values())):
        print("成功")
        db.commit()
except:
    print("失败")
    db.rollback()
# 5.更新数据
data5 = {
    'id':'200180909',
    'name':'jerry',
    'age':20
}
table5 = 'students'
keys5 = ','.join(data5.keys()) # join()方法将序列中的元素以指定的字符连接生成一个新的字符串。
values5 = ','.join(['%s']*len(data5))
sql5 = 'INSERT INTO {table }({keys}) values ({values}) ON DUPLICATE KEY UPDATE'.format(table = table5,keys=keys5,values=values5)
update = ','.join([" {key} = %s".format(key=key) for key in data5])
sql5 += update
try:
    if cursor.execute(sql5,tuple(data5.values()*2)):
        print('成功')
        db.commit()
except:
    print('失败')
    db.rollback()
# 6.删除数据
table6 = 'students'
condition6 = 'age > 19'
sql6 = 'DELETE FROM {table} WHERE {condition}'.format(table=table6,condition=condition6)
try:
    cursor.execute(sql6)
    db.commit()
except:
    db.rollback()
# 7.查询数据
sql7 = 'SELECT * FROM students WHERE age >= 20'
try:
    cursor.execute(sql7)
    print("Count:",cursor.rowcount) # cursor.rowcount()返回查询结果的条数
    row = cursor.fetchone() #fetchont()返回一重元组，指针是偏移指针，这里每循环一次，指针就偏移一条数据，随用随取，简单高效
    while row:
        print('Row:',row)
        row = cursor.fetchone()
except:
    print('Error')
db.close()