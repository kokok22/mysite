from MySQLdb import connect
from MySQLdb.cursors import DictCursor
from django.db import models

# Create your models here.

def fetchone(email, password):
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select no, name
        from
            user
        where
            email = %s and
            passwd = password(%s)
    '''

    cursor.execute(sql, (email, password))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result

def fetchonebyteno(no):
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select name, email, gender
        from
            user
        where
            no = %s
    '''

    cursor.execute(sql, str(no))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result


def insert(name, email, password, gender):
    conn = getconn()
    cursor = conn.cursor()

    sql = '''
            insert into
                  user
            values(null, %s, %s, password(%s), %s, now())
        '''

    cursor.execute(sql, (name, email, password, gender))
    conn.commit()

    cursor.close()
    conn.close()


def update(no, name, password, gender):
    conn = getconn()
    cursor = conn.cursor()

    if password != '':
        sql = '''
                    update
                        user
                    set
                        name = %s ,
                        passwd = password(%s) ,
                        gender = %s
                    where
                        no = %s
                '''

        cursor.execute(sql, (name, password, gender, str(no)))
    else:
        sql = '''
                            update
                                user
                            set
                                name = %s ,
                                gender = %s
                            where
                                no = %s
                        '''

        cursor.execute(sql, (name, gender, str(no)))

    conn.commit()
    cursor.close()
    conn.close()


def getconn():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.108',
        port=3307,
        db='mysite',
        charset='utf8')