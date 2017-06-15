from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/requests')
def requests():
    return render_template('requests.html')

@app.route('/shopping-list')
def requests():
    return render_template('shopping-list.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
