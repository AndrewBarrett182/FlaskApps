from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'This is the home page'

@app.route('/about')
def about():
    return 'This is the about page'

@app.route('/about/<number>')
def about_number(number):
    return 'This is the about page ' + str(number)

if __name__ == "__main__":
    app.run(debug=True)