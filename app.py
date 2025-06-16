from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def confession():
    return render_template('confession.html')

if __name__ == '__main__':
    app.run()