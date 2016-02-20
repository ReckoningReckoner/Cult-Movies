import metacritic

def is_cult(crit, user):
    return crit <= 50 and user >= 60


result = metacritic.Metacritic.search("Inside Out")
for r in result:
    if r.metascore and r.user_score:
        
        metascore = int(r.metascore)
        user_score = int(float(r.user_score))*10
        
        if is_cult(metascore, user_score):
            print(r.title)
            print(metascore)
            print(user_score)
            print(r.release_date)
            print(r.link)
