from flask import Flask, render_template
from calldb import select_dt

app = Flask(__name__)

@app.route('/')
def home():
    sid = 68130677
    sname = "Tammarit Tana-Anant"
    return render_template('info.html', ids=sid, names=sname)

@app.route('/movie')
def movie():
    dt = select_dt()
    return render_template('movie.html', table=dt)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

