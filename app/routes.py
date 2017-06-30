from flask import render_template
from app import app

@app.route('/')
def home():
    return render_template('home.html', welcome='Welcome to KnuthSnacks!')

@app.route('/moresnacks')
def moresnacks():
    return render_template('moresnacks.html')

@app.route('/shoppinglist')
def shoppinglist():
    return render_template('shoppinglist.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
