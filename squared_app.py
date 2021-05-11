from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 'Hello World'

@app.route('/home/<int:number>')
def squared(number):
    return str(number * number)

if __name__ == "__main__":
    app.run(debug=True)