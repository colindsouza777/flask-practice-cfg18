from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world18():

    return render_template('index/index.html')

@app.rout('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)
