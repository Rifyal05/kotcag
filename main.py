from flask import Flask, render_template
from flask import request, redirect, url_for


app = Flask(__name__)


@app.route('/')
def home():
    name = 'Kotcag'
    return render_template('index.html',name=name)

# @app.route('/About')
# def about():
#     return 'ini adalah moonkey!'

@app.route('/info/<string:name>')
def info(name):
    return f'selamat datang, {name} di halaman news!'

data = []
@app.route('/news/<int:index>')
def news(index):
    produk = data[index]
    return f'ini adalah halaman produk {produk}'

@app.route('/form')
def form():
    nama = 'Rifyal'
    return render_template('form.html')



# @app.route('/form')
# def form():
#     nama = 'Rifyal'
#     return render_template('form.html')


@app.route('/form', methods = {'post'})
def submit():
    # name = request.form['name'].title()
    # age = request.form['age'].title()
    name_product = request.form[name_product].title()
    kategori_produk = request.form['kategori_produk']
    harga_product = request.form[harga_product]

    produk = {'name_product' : name_product, 'kategori' : kategori_produk, 'harga' : harga_product }
    data.append(produk)
    # return f'data berhasil dikirik : nama : {name}, umur : {age}'
    return redirect(url_for('form'))


@app.route('/About')
def about():
    nama = 'Rifyal'
    umur = 20
    list = ['ikan', 'buaya', 'paus']
    # list = []


    produk_saya = [
        {'nama' : 'ikan', 'harga' : 12000, 'stock'  : False},
        {'nama' : 'buaya', 'harga' : 12000, 'stock'  : True},
        {'nama' : 'hanzam', 'harga' : 12000, 'stock'  : True}
    ]
    return render_template('about.html', nama=nama, umur = umur, list = list, produk = produk_saya)

@app.route('/homepage')
def homepage():
    return render_template('homepage.html')

@app.route('/aboutpage')
def aboutpage():
    return render_template('aboutpage.html')
    