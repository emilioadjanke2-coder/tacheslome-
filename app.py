from flask import Flask, request, redirect
app = Flask(__name__)

# Tes tâches - tu peux les changer ici facilement
taches = [
    {"nom": "Liker Boutique Kpalimé", "gain": 50, "lien": "https://facebook.com"},
    {"nom": "Partager Wax Togolais", "gain": 50, "lien": "https://facebook.com"},
]

@app.route('/')
def home():
    html_taches = ""
    for t in taches:
        html_taches += f"<div class='task'><div>❤️ <b>{t['nom']} - {t['gain']}F</b></div><button class='btn' onclick=\"window.open('{t['lien']}','_blank'); gagner({t['gain']})\">Faire</button></div>"

    return f"""
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
<style>
body{{font-family:Arial;margin:0;background:#f2f2f2}}
.header{{background:#1877F2;color:white;padding:15px;text-align:center;font-weight:bold}}
.solde{{background:white;text-align:center;padding:15px;color:#00b050;font-size:22px;font-weight:bold}}
.task{{background:white;display:flex;justify-content:space-between;padding:12px;margin:8px;border-radius:8px}}
.btn{{background:#1877F2;color:white;border:none;padding:8px 15px;border-radius:6px;font-weight:bold}}
.retrait{{background:#555;color:white;text-align:center;padding:15px;position:fixed;bottom:0;width:100%}}
</style></head><body>
<div class='header'>TachesLome Pro 🇹🇬</div>
<div class='solde' id='solde'>Solde: 10200 FCFA</div>
{html_taches}
<div style='height:80px'></div>
<div class='retrait'>🔒 Retraits Vendredi 18h (en pause)</div>
<script>
let s=10200;
function gagner(m){{s+=m;document.getElementById('solde').innerText='Solde: '+s+' FCFA';alert('Bravo +'+m+'F !');}}
</script>
</body></html>
"""

@app.route('/admin', methods=['GET','POST'])
def admin():
    global taches
    if request.method == 'POST':
        nom = request.form.get('nom')
        lien = request.form.get('lien')
        gain = int(request.form.get('gain', 50))
        if nom and lien:
            taches.insert(0, {"nom": nom, "gain": gain, "lien": lien})
    liste = "".join([f"<li>{x['nom']} - {x['gain']}F - <a href='{x['lien']}' target='_blank'>Voir page</a></li>" for x in taches])
    return f"""
    <h2>Page Patron - TachesLome Pro</h2>
    <p><b>Pour ajouter une boutique qui t'a payé :</b></p>
    <form method='POST'>
    Nom de la tâche: <br><input name='nom' placeholder='Ex: Liker Wax Fatou' style='width:100%;padding:8px' required><br><br>
    Lien Facebook de la boutique: <br><input name='lien' placeholder='https://facebook.com/...' style='width:100%;padding:8px' required><br><br>
    Combien tu paies le jeune: <br><input name='gain' type='number' value='50' style='width:100%;padding:8px'><br><br>
    <button style='background:green;color:white;padding:12px;width:100%'>AJOUTER LA TÂCHE</button>
    </form>
    <hr><h3>Tâches actuelles:</h3><ul>{liste}</ul>
    <p><a href='/'>Voir le site des jeunes</a></p>
    """

if __name__ == '__main__':
    app.run()
