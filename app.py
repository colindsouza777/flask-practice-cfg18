from flask import Flask, render_template,redirect
app = Flask(__name__)

@app.route('/')
def hello_world18():
    return render_template('index/index.html')

@app.route('/about')
def about():
    return render_template('about_us/about.html')
@app.route('/contact')
def contact():
    redirect('/')

if __name__ == "__main__":
    app.run(debug=True)
