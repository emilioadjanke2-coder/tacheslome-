from flask import Flask

app = Flask(__name__)

WHATSAPP_NUMBER = "22870005827"
WHATSAPP_LINK = f"https://api.whatsapp.com/send?phone={WHATSAPP_NUMBER}&text=Bonjour%20Emilio,%20je%20veux%20la%20gestion%20Page%20à%2015.000F"

HTML = f"""
<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TachesLome - Lomé</title>
<style>
body{{font-family:Arial;text-align:center;padding:20px;background:#f5f5f5}}
.card{{background:white;padding:25px;border-radius:15px;max-width:400px;margin:auto;box-shadow:0 4px 10px rgba(0,0,0,0.1)}}
.btn{{display:block;background:#0d6efd;color:white;padding:15px;border-radius:10px;text-decoration:none;font-weight:bold;margin-top:15px}}
.tag{{display:inline-block;background:#eee;padding:6px 12px;border-radius:20px;margin:5px;font-size:14px}}
</style>
</head>
<body>
<div class="card">
<p>🚀 LANCEMENT BIENTOT</p>
<h1>TachesLome 🇹🇬</h1>
<p>Petits boulots à Lomé - Rapide & Fiable</p>
<div>
<span class="tag">🧹 Nettoyage</span>
<span class="tag">🛒 Courses</span>
<span class="tag">🏠 Aide menagere</span>
<span class="tag">📦 Livraison</span>
<span class="tag">🔧 Petits travaux</span>
</div>
<p><b>Anciennes annonces supprimees<br>Reduction de lancement pour premiers clients !</b></p>
<a href="{WHATSAPP_LINK}" class="btn">📱 NOUVEAU: Gestion Page Facebook 15.000F/mois →</a>
<p style="font-size:11px;color:#666;margin-top:15px">Lome - 7j/7 - WhatsApp: {WHATSAPP_NUMBER} - Togo only</p>
</div>
</body>
</html>
"""

@app.route('/')
def home():
    return HTML

@app.route('/gestion-page')
def gestion():
    return HTML

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
