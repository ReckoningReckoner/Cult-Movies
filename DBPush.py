import metacritic
import shlex
import mysql.connector
import sys
from datetime import date, datetime, timedelta


def is_cult(crit, user):
    return crit <= 50 and user >= 60
    
def get_cult(title):
    result = metacritic.Metacritic.search(title)
    for r in result:
        if r.metascore and r.user_score:
            metascore = int(r.metascore)
            user_score = int(float(r.user_score))*10
            release_date = datetime.strptime(r.release_date, '%B %d, %Y').strftime("%Y-%m-%d")
            if is_cult(metascore, user_score):
                yield r.id, r.title, metascore, user_score, release_date, r.link, r.tags, r.image, r.summary
                
db = mysql.connector.connect(user='sql5107655', 
                            password='izqAeyN6Yu', 
                            host='sql5.freemysqlhosting.net', 
                            database='sql5107655')
cursor = db.cursor()

i = 0
with open("movies.list.txt") as f:
    for line in f:
        if i == 100:
           break;
                  
        try:
            line = f.readline()
            line = shlex.split(line)
            print(i)
            for id, title, metascore, user_score, release_date, url, tags, image, summary in get_cult(line[0]):
                try:
                    print(id, title, metascore, user_score, url, release_date, tags, image, summary)
                    args = (id, title, metascore, user_score, url, release_date, tags, image, summary)
                    command = "INSERT INTO `movie` VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s) "
                    cursor.execute(command, args)
                except:
                    print(sys.exc_info()[0])
                    continue
            i += 1
        except:
            continue
            
db.commit()
cursor.close()
db.close()            
