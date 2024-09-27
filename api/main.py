from flask import Flask, request
from flask_cors import CORS  # Agrega esta línea
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
CORS(app)  # Permitir CORS para todas las rutas

@app.route('/send-email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    msg = MIMEText(f'Nombre: {name}\nCorreo: {email}\nMensaje: {message}')
    msg['Subject'] = 'Nuevo mensaje de contacto'
    msg['From'] = email
    msg['To'] = 'a.mejiabjs@gmail.com'

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login('a.mejiabjs@gmail.com', 'Alexmb130899.?')
            server.send_message(msg)
        return 'Correo enviado exitosamente.', 200
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(port=8080, debug=True)  # Asegúrate de que la aplicación se ejecute en el puerto 8080
