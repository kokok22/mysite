from MySQLdb import connect
from MySQLdb.cursors import DictCursor

# Create your models here.


def fetchlist():
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql = '''
        select
                b.no,
                b.title,
                u.name,
                b.user_no,
                b.view,
                date_format(b.reg_date, '%Y-%m-%d %h:%i:%s') as reg_date,
                b.depth
        from
            board as b, user as u
        where
            u.no = b.user_no
        order by
            b.g_no desc, o_no asc
    '''

    cursor.execute(sql)
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result


def fetchno(no):
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql = '''
            select
                    no,
                    title,
                    content,
                    user_no,
                    g_no,
                    o_no,
                    depth
            from
                board
            where
                no = %s
        '''

    cursor.execute(sql,[no])
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result



def insert(title, content, user_no,g_no,o_no,depth):
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql = '''
        insert into
            board
        values(null, %s, %s, '0', now(), %s,%s,%s,%s)
    '''

    cursor.execute(sql, (title, content, g_no, o_no, depth, [user_no]))
    conn.commit()

    cursor.close()
    conn.close()


def delete(no):
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql = '''
            delete from
                board
            where
                no = %s
        '''

    cursor.execute(sql, [no])
    conn.commit()

    cursor.close()
    conn.close()


def update(no, title, content):
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql = '''
            update
                board
            set
                title = %s,
                content = %s
            where
                no = %s
        '''

    cursor.execute(sql, (title, content, [no]))
    conn.commit()

    cursor.close()
    conn.close()


def updateview(no):
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql = '''
            update
                board
            set
                view = view+1
            where
                no = %s
        '''

    cursor.execute(sql, [no])
    conn.commit()

    cursor.close()
    conn.close()


def selectg_no():
    conn = getconn()
    cursor = conn.cursor(DictCursor)

    sql ='''
            select
                g_no
            from
                board
            order by
                g_no desc
                limit 0,1
    '''

    cursor.execute(sql)
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return result


def getconn():
    return connect(
        user='mysite',
        password='mysite',
        host='192.168.1.118',
        port=3307,
        db='mysite',
        charset='utf8')