from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from crypto_utils import operation

app = Flask(__name__)

@app.route('/')
def Index():
    return render_template('index.html')

@app.route('/add_password', methods=['POST'])
def add_password():
    if request.method == 'POST':
        aplication = request.form['appli']
        normal = request.form['password']
        include = request.form.get('Spanish')
        print(include)
        Pass = operation(include, normal, aplication)
    return render_template('Show.html', Password = Pass)


if __name__ == '__main__':
    app.run(debug=True)