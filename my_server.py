# Para crear un servidor podemos utilizar FLASK o DJANGO
#   1) FLASK --> Mas sencillo y basico
#   2) DJANGO --> Mas completo pero complejo de usar (muchas reglas )

# (Ambos tienen la ventaja de permitirnos, crear servidores sin tener que
# lidiar con los problemas de seguridad y demas)

# ====================== SERVIDOR CON FLASK ==================================================================

# COMANDO PARA ACTIVAR  EL ENV --> web_server_portfolio\Scripts\Activate.ps1
# COMANDO PARA SETEAR la aPP DEL SERVIDOR --> $env:FLASK_APP = "nombre_app.py"
# COMANDO PARA PONER EN MODO DEBUG --> $env:FLASK_ENV = "development"
# COMANDO PARA INICIAR SERVIDOR --> flask run
from flask import Flask, render_template, redirect, request, url_for
import csv

app = Flask(__name__)  # instanciamos una app en base a la clase FLask
print(__name__)  # __name__ es igual al __main__


@app.route('/')  # SIEMPRE DDEBE ESTAR
def my_home():
    return render_template('index_port.html')


@app.route('/<string:page_name>')  # es una ruta dinamica
def html_page(page_name):
    return render_template(page_name)


@app.route('/gracias/<username>')  # ruta hacia el gracias
def gracias(username):
    return render_template('thank_you.html', name=username)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()  # obtenemos los datos en formato de dictionary
        print(data)
        write_to_file(data, 'database.txt')
        write_to_csv(data, 'database.csv')
        name = data['name']
        return redirect(url_for('gracias', username=name))
    else:
        return 'Something went wrong. Try again!'


def write_to_file(data, fileName):
    with open(fileName, 'a', encoding='utf-8') as file:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        file.write(f'{name}//{email}//{subject}//{message}\n')


def read_from_file(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        return file.readlines()


def write_to_csv(data, fileName):
    with open(fileName, 'a', newline='', encoding='utf-8') as database:
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']

        csv_writer = csv.writer(database, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([name, email, subject, message])

# @app.route('/bolt.ico')
# def favicon():
#     return send_from_directory(os.path.join(app.root_path, 'static'),
#                                'bolt.ico', mimetype='image/vnd.microsoft.icon')
