from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
    <head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
    body{font-family:sans-serif;background:#f7f7f5;display:flex;align-items:center;justify-content:center;min-height:100vh;margin:0}
    .card{background:white;max-width:400px;width:92%;border-radius:24px;padding:32px 20px;text-align:center;box-shadow:0 10px 30px rgba(0,0,0,.08)}
    .badge{background:#fff7ed;color:#f97316;padding:6px 12px;border-radius:99px;font-size:13px;font-weight:700}
    h1{font-size:32px;margin:12px 0 5px}
    .services{margin:20px 0;display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
    .services span{background:#f3f4f6;padding:8px 12px;border-radius:20px;font-size:13px}
    .btn{display:block;background:#25D366;color:white;text-decoration:none;padding:16px;border-radius:14px;font-weight:800;margin-top:20px;font-size:18px}
    </style></head>
    <body>
    <div class="card">
    <span class="badge">🚀 LANCEMENT BIENTOT</span>
    <h1>TachesLome 🇹🇬</h1>
    <p>Petits boulots à Lomé - Rapide & Fiable</p>
    <div class="services">
    <span>🧹 Nettoyage</span><span>🛒 Courses</span><span>🏠 Aide menagere</span><span>📦 Livraison</span><span>🔧 Petits travaux</span>
    </div>
    <p><b>Anciennes annonces supprimees</b><br>Reduction de lancement pour premiers clients !</p>
    <a class="btn" href="https://wa.me/22870005827?text=Salut%20TachesLome%20!%20J'ai%20besoin%20d'aide">📱 WhatsApp: 70 00 58 27</a>
    <p style="font-size:11px;color:#999;margin-top:15px">Lome - 7j/7 - Nouveau depart propre</p>
    </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
