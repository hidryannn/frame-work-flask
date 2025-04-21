from flask import Flask, render_template

app = Flask(__name__)

app_name = "My Application Name is: Baco dan Besse"

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/aplikasi/")
def aplikasi():
    return "<p>Selamat datang di Aplikasi Flask</p>"

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/about-bostrapp/")
def about_bostrapp():
    return render_template('about_with_bostrapp.html')

@app.route("/nama/<string:nama_mahasiswa>/")
def getnama(nama_mahasiswa):
    return "nama anda adalah {}".format(nama_mahasiswa)

@app.route('/user/<int:user_id>')  # Hanya menerima angka
def user_id(user_id):
    return f"User ID: {user_id}"

@app.route('/variabel-global/')
def variabel_global():
    return f"Welcome {app_name}"

@app.route('/data/')
def data():
    user = {"name": "Ali", "age": 25, "city": "Jakarta"}
    return render_template('data.html', user=user)

if __name__ == "__main__":
    app.run(debug=True)
