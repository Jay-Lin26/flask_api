import pymysql


def Sql(sentence):
    try:
        conn = pymysql.connect(
            host='47.100.164.202',
            user='root',
            password='123456',
            database='Testcases')
        cursor = conn.cursor()
        sql = sentence
        cursor.execute(sql)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result
    except IndexError:
        return {'message': ' select IndexError '}
    except pymysql.err.OperationalError:
        return {'message': ' select OperationalError'}
