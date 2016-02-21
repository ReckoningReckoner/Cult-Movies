from flask import *
from DBParse import *
import datetime

app = Flask(__name__)


@app.route('/search')
def search():
    search_query = request.args.get("query").replace("+", " ")
    sort_by = request.args.get("sort")
    results = DBParse().search(search_query)

    if sort_by == "release_date":
        rows = reversed(sorted(results, key=lambda k: datetime.datetime.strptime(k["release_date"], '%Y-%m-%d')))
    else:
        rows = sorted(results, key=lambda k: -k[sort_by])        
    return render_template('results.html', rows=rows, search_query=search_query)
    
    
@app.route('/')
def index():
    randrow = DBParse().random()
    return render_template('index.html', randrow=randrow)


if __name__ == '__main__':
    app.run()
