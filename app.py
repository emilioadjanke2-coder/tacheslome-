from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
    <style>
    body{font-family:Arial;background:#f5f5f5;margin:0;padding:20px}
    .card{background:white;padding:15px;border-radius:12px;margin:10px 0;box-shadow:0 2px 5px #0001}
    .btn{background:#25D366;color:white;padding:10px 15px;border-radius:8px;text-decoration:none;display:inline-block}
    h1{color:#006A4E}
    </style></head><body>
    <h1>TachesLome 🇹🇬</h1>
    <p><b>Petits boulots à Lomé - Trouve de l'aide vite !</b></p>
    
    <div class='card'>
    <h3>🧹 Besoin de ménage à Adidogomé</h3>
    <p>2h de ménage, 3000 FCFA</p>
    <a class='btn' href='https://wa.me/22890000000'>Contacter sur WhatsApp</a>
    </div>

    <div class='card'>
    <h3>📦 Livraison moto à Tokoin</h3>
    <p>Besoin coursier urgent, 2000 FCFA</p>
    <a class='btn' href='https://wa.me/22890000000'>Contacter sur WhatsApp</a>
    </div>

    <div class='card'>
    <h3>💻 Aide informatique</h3>
    <p>Installation Windows, 5000 FCFA</p>
    <a class='btn' href='https://wa.me/22890000000'>Contacter sur WhatsApp</a>
    </div>

    <p style='text-align:center;margin-top:30px'>Fait avec ❤️ à Lomé</p>
    </body></html>
    """

if __name__ == '__main__':
    app.run()
