from Flask import flask, render_template

app = Flask(__name__)

app.config['SECRET_KEY'] = 'the random string'
@app.route('/')
def index():
  return render_template("index.html")

@app.route('/panel', methods=['POST', 'GET'])
def do_admin_login():
  if request.form['Password'] == 'thisisthecorrectpassword':
    session['logged_in'] = True
    return render_template("panel.html", econ=econ)
  else:
    flash('wrong password!')
    return "<h2>Incorrect password</h2>"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000)
