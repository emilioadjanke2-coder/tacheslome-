from flask import Flask
app = Flask(__name__)

@app.route('/')
def maison():
    return """
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:sans-serif;background:#f5f5f5;margin:0;padding:15px}
.card{background:white;max-width:500px;margin:30px auto;padding:20px;border-radius:16px;text-align:center;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.badge{background:#fff7ed;color:#f97316;padding:5px 12px;border-radius:20px;font-size:13px}
h1{font-size:32px;margin:12px 0 5px}
.services{margin:20px 0;display:flex;flex-wrap:wrap;gap:8px;justify-content:center}
.services span{background:#f3f4f6;padding:6px 12px;border-radius:20px;font-size:14px}
.btn{display:block;background:#25D366;color:white;padding:14px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:10px}
.btn2{display:block;background:#0d6efd;color:white;padding:12px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:15px}
</style></head>
<body>
<div class="card">
<div class="badge">🚀 LANCEMENT BIENTOT</div>
<h1>TachesLome 🇹🇬</h1>
<p>Petits boulots à Lomé - Rapide & Fiable</p>
<div class="services">
<span>🧹 Nettoyage</span><span>🛒 Courses</span>
<span>🏠 Aide menagere</span><span>📦 Livraison</span>
<span>🔧 Petits travaux</span>
</div>
<p><b>Anciennes annonces supprimees<br>Reduction de lancement pour premiers clients !</b></p>
<a class="btn" href="https://wa.me/22870005827">📱 WhatsApp: 70 00 58 27</a>
<a class="btn2" href="/gestion-page">📱 NOUVEAU: Gestion Page Facebook 15.000F/mois →</a>
<p style="color:gray;font-size:12px;margin-top:15px">Lome - 7j/7 - Nouveau depart propre</p>
</div>
</body>
</html>
"""

@app.route('/gestion-page')
def gestion_page():
    return """
<html>
<head><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial;background:#f5f5f5;margin:0;padding:15px}
.card{background:white;border-radius:12px;padding:20px;max-width:500px;margin:20px auto;box-shadow:0 2px 10px rgba(0,0,0,0.1)}
.price{font-size:28px;color:#198754;font-weight:bold;margin:10px 0}
.btn{display:block;background:#25D366;color:white;text-align:center;padding:15px;border-radius:8px;text-decoration:none;font-weight:bold;margin-top:15px;font-size:18px}
</style></head>
<body>
<div class="card">
<h1>📱 Je gère votre page Facebook</h1>
<p>Vous êtes à Lomé ou Tsévié et vous n'avez pas le temps ?</p>
<div class="price">15.000 FCFA / mois</div>
<ul>
<li>✅ 3 posts / semaine</li>
<li>✅ Je réponds aux commentaires</li>
<li>✅ Tout à distance depuis Tsévié</li>
<li>✅ 2 jours d'essai GRATUIT</li>
</ul>
<p>1. Vous envoyez 10 photos WhatsApp<br>2. Je crée et je poste<br>3. Vous avez plus de clientes</p>
<a class="btn" href="https://wa.me/22870005827?text=Bonjour%20Emil%2C%20je%20veux%20gestion%20page%20Facebook%20vu%20sur%20TachesLome">Commander sur WhatsApp 70 00 58 27</a>
<br><a href="/">← Retour accueil</a>
</div>
</body>
</html>
"""

if __name__ == '__main__':
    app.run()
