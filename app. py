from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return """
<html><head><meta name='viewport' content='width=device-width,initial-scale=1'>
<style>
body{font-family:Arial;margin:0;background:#f2f2f2}
.header{background:#1877F2;color:white;padding:15px;text-align:center;font-weight:bold;font-size:22px}
.sub{background:#0d5dc0;color:white;text-align:center;padding:5px;font-size:14px}
.solde{background:white;text-align:center;padding:15px;color:#00b050;font-size:26px;font-weight:bold;border-bottom:3px solid #eee}
.connect{background:#e9e9e9;text-align:center;padding:12px;font-size:18px}
.task{background:white;display:flex;justify-content:space-between;align-items:center;padding:12px;margin:8px;border-radius:8px;box-shadow:0 1px 3px #0001}
.task b{font-size:16px}
.btn{background:#1877F2;color:white;border:none;padding:10px 20px;border-radius:8px;font-weight:bold}
.retrait{background:#00b050;color:white;text-align:center;padding:15px;font-weight:bold;font-size:18px;position:fixed;bottom:0;width:100%}
</style></head><body>

<div class='header'>TachesLome Pro 🇹🇬</div>
<div class='sub'>Gagne en aidant les commerces locaux</div>
<div class='solde' id='solde'>Solde: 3000 FCFA</div>
<div class='connect'>Connecté: +22870005827</div>

<div class='task'>
 <div>❤️ <b>Liker Boutique Kpalimé - 500F</b></div>
 <button class='btn' onclick='gagner(500)'>Faire</button>
</div>

<div class='task'>
 <div>📤 <b>Partager Wax Togolais - 700F</b></div>
 <button class='btn' onclick='gagner(700)'>Faire</button>
</div>

<div class='task'>
 <div>🌐 <b>Tester site d'un coiffeur - 1000F</b></div>
 <button class='btn' onclick='gagner(1000)'>Faire</button>
</div>

<div class='task'>
 <div>⭐ <b>Noter restaurant Adawlato - 800F</b></div>
 <button class='btn' onclick='gagner(800)'>Faire</button>
</div>

<div class='task'>
 <div>📲 <b>S'abonner TikTok boutique Lomé - 600F</b></div>
 <button class='btn' onclick='gagner(600)'>Faire</button>
</div>

<div style='height:80px'></div>
<div class='retrait' onclick="alert('Retrait Mixx : Envoie ton solde à +22870005827 sur WhatsApp pour recevoir via Mixx by Yas !')">
💸 Demander Retrait Mixx / Flooz
</div>

<script>
let s=3000;
function gagner(m){
 s+=m;
 document.getElementById('solde').innerText='Solde: '+s+' FCFA';
 alert('Bravo ! +'+m+'F ajouté. Va liker/partager la page puis reviens.');
}
</script>

</body></html>
    """
if __name__ == '__main__':
    app.run()
