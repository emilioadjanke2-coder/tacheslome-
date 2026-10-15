from flask import Flask, render_template

app = Flask(__name__)

WHATSAPP_NUMBER = "22870005827"
WHATSAPP_LINK = f"https://wa.me/{WHATSAPP_NUMBER}?text=Bonjour%20Emil,%20je%20veux%20la%20gestion%20Page%20Facebook%20à%2015.000F/mois%20pour%20ma%20boutique%20à%20Lomé"

@app.route('/')
def home():
    return render_template('index.html', whatsapp_link=WHATSAPP_LINK, whatsapp_number=WHATSAPP_NUMBER)

@app.route('/gestion-page')
def gestion_page():
    return render_template('gestion.html', whatsapp_link=WHATSAPP_LINK, whatsapp_number=WHATSAPP_NUMBER)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
