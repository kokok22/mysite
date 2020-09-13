from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models

# Create your models here.


def fetchlist():
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select no,
                name,
                message,
                date_format(reg_date, '%Y-%m-%d %h:%i:%s') as reg_date
        from
            guestbook
        order by
            no desc
    '''

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def insert(name, password, message):
    conn = getconn()
    cursor = conn.cursor()

    sql = '''
            insert into
                  guestbook
            values(null, %s, %s, %s, now())
        '''

    cursor.execute(sql, (name, password, message))
    conn.commit()

    cursor.close()
    conn.close()


def delete(no, password):
    conn = getconn()
    cursor = conn.cursor()

    sql = '''
            delete from
                guestbook
            where
                no = %s and
                passwd = %s  
    '''
    cursor.execute(sql, (no, password))
    conn.commit()

    cursor.close()
    conn.close()


def getconn():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.118',
        port=3307,
        db='mysite',
        charset='utf8')