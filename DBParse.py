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
                
    def already_exists(self, id, valid):
        for movie in valid:
            if valid['id'] == id:
                return True
                
        return False
    
    
    def get(self, tag, valid = {}):
        if len(tag.split(" ")) < 1 or tag == "":
            return {}
        elif len(tag.split(" ")) == 1:
            with self.connection.cursor() as cursor:
                query = '''
                SELECT * FROM `movie` 
                WHERE `name` LIKE %s OR
                `tags` LIKE %s
                '''
                args = ("%%"+tag+"%%", "%%"+tag+"%%")
                d = {}
                cursor.execute(query, (args))
                for movie in cursor.fetchall():
                    movie['relevance'] = 1
                    d[movie['id']] = movie
                    
                return d
        else:
            valid = {}
            lis = []
            for word in tag.split(" "):
                movies = self.get(word, valid)
                for key in movies:
                    if key in valid:
                        valid[key]['relevance'] += 1
                    else:
                        valid[key] = movies[key]
                
            return valid
            
    def random(self):
        with self.connection.cursor() as cursor:
                query = "SELECT * FROM `movie` ORDER BY RAND() LIMIT 6"
                cursor.execute(query)
                return cursor.fetchall()
        
        
            
    def search(self, tag):
        d = self.get(tag)
        l = []
        for key in d:
            l.append(d[key])
            
        return l
            
if __name__ == "__main__":
    d = DBParse()
    print(d.random())
    