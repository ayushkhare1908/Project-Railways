from sqlite3 import *
conn=connect('project_db.db')
c1=conn.cursor()

def create_table_train_detail():
    c1.execute('create table if not exists trains(train_no text ,train_name text,src text,dest text,day text,month text,dept_time text,arr_time)')

def insert_into_train_detail(train_no,train_name,src,dest,day,month,dept_time,arr_time):
    a=[]
    a.append((train_no,train_name,src,dest,day,month,dept_time,arr_time))
    c1.executemany('insert into trains values(?,?,?,?,?,?,?,?)',a)
    conn.commit()

create_table_train_detail()

def create_table_reservation():
    c1.execute('create table if not exists reservation(train_no text,train_name text,class text,src text,dest text,quota text,boaring text,reservation_upto text,name text,age text,sex text,bearth_pre text,food_pre text,senior text)')
def insert_into_reservation(a5,b,c,d,e,f,g,h,i,j,k,l,m,n):
    a=[]
    a.append((str(a5),str(b),str(c),str(d),str(e),str(f),str(g),str(h),str(i),str(j),str(k),str(l),str(m),str(n)))
    c1.executemany('insert into reservation values(?,?,?,?,?,?,?,?,?,?,?,?,?,?)',a)
    conn.commit()
def fetch_data(src,dest):
    c1.execute('select train_no,train_name from trains where src=? and dest=?',(src,dest))
    x=c1.fetchall()
    return x
create_table_reservation()
