from flask import *
from DBParse import *
from wtforms import *
app = Flask(__name__)

class Search(Form):
    tags = TextField('Search:')
    

@app.route('/all')
def all():
    rows = sorted(DBParse().return_all(), key=lambda k: -k['user_score'])
    return render_template('all.html', rows=rows)
    

if __name__ == '__main__':
    app.run()