from flask import Flask, render_template
from controller.user import user
from controller.emp import emp



app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(emp)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/welcome')
def welcome():
    return render_template("welcome.html", message="你好世界")

if __name__ == '__main__':
    app.run(host='0.0.0.0')