from flask import Flask, render_template, redirect, request, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'

valid_password = '2002'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    password = request.form['password']
    if password == valid_password and password.isdigit() and len(password) == 4:
        # Password is correct and meets the criteria
        return redirect(url_for('index'))
    else:
        return render_template('login.html', error=True)

@app.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)