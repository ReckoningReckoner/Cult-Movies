import pymysql.cursors

class DBParse:
    def __init__(self):
        self.connection = pymysql.connect(host='sql5.freemysqlhosting.net',
                                     user='sql5107655',
                                     password='izqAeyN6Yu',
                                     db='sql5107655',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

    def return_all(self):
        with self.connection.cursor() as cursor:
                query = "SELECT * FROM `movie`"
                cursor.execute(query)
                return cursor.fetchall()