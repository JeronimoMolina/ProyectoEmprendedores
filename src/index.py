#importacion de las librerias
from flask import Flask, render_template

#inicio de la aplicacion
app = Flask(__name__)

#pagina de inicio
@app.route('/')
def home():
    #mensaje inicial
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')


#comprobacion de la pagina web
if __name__ == '__main__':
    app.run(debug = True)