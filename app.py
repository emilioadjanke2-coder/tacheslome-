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
.btn{background:#1877F2;color:white;border:none;padding:10px 20px;border-radius:8px;font-weight:bold}
.retrait{background:#00b050;color:white;text-align:center;padding:15px;font-weight:bold;font-size:18px;position:fixed;bottom:0;width:100%;cursor:pointer}
.modal{display:none;position:fixed;top:0;left:0;width:100%;height:100%;background:#0008;justify-content:center;align-items:center}
.modal-box{background:white;padding:20px;border-radius:12px;width:90%;max-width:350px;text-align:center}
input{width:100%;padding:12px;margin:8px 0;border:1px solid #ccc;border-radius:8px}
</style></head><body>

<div class='header'>TachesLome Pro 🇹🇬</div>
<div class='sub'>Gagne en aidant les commerces locaux</div>
<div class='solde' id='solde'>Solde: 10200 FCFA</div>
<div class='connect'>Connecté: +22870005827</div>

<div id='tasks'>
<div class='task'><div>❤️ <b>Liker Boutique Kpalimé - 500F</b></div><button class='btn' onclick='gagner(500)'>Faire</button></div>
<div class='task'><div>📤 <b>Partager Wax Togolais - 700F</b></div><button class='btn' onclick='gagner(700)'>Faire</button></div>
<div class='task'><div>🌐 <b>Tester site coiffeur - 1000F</b></div><button class='btn' onclick='gagner(1000)'>Faire</button></div>
<div class='task'><div>⭐ <b>Noter Adawlato - 800F</b></div><button class='btn' onclick='gagner(800)'>Faire</button></div>
<div class='task'><div>📲 <b>S'abonner TikTok Lomé - 600F</b></div><button class='btn' onclick='gagner(600)'>Faire</button></div>
</div>

<div style='height:80px'></div>
<div class='retrait' onclick='ouvrirRetrait()'>💸 Demander Retrait Mixx / Flooz</div>

<div class='modal' id='modal'>
<div class='modal-box'>
<h3>Retrait Mixx by Yas</h3>
<p id='soldeText'></p>
<input id='mixxNum' placeholder='Ton numéro Mixx / Flooz ex: 90xxxxxx'>
<input id='nom' placeholder='Ton nom'>
<button class='btn' style='width:100%;background:#00b050;margin-top:10px' onclick='envoyerRetrait()'>Confirmer Retrait</button>
<button onclick='fermer()' style='margin-top:10px;background:none;border:none;color:red'>Annuler</button>
</div>
</div>

<script>
let s=10200;
function gagner(m){s+=m;document.getElementById('solde').innerText='Solde: '+s+' FCFA';alert('Bravo ! +'+m+'F. Tâche validée !');}
function ouvrirRetrait(){
 if(s<1000){alert('Solde minimum 1000F pour retrait');return;}
 document.getElementById('soldeText').innerText='Tu vas retirer '+s+' FCFA';
 document.getElementById('modal').style.display='flex';
}
function fermer(){document.getElementById('modal').style.display='none';}
function envoyerRetrait(){
 let num=document.getElementById('mixxNum').value;
 let nom=document.getElementById('nom').value;
 if(!num){alert('Mets ton numéro Mixx');return;}
 let msg=`DEMANDE RETRAIT TachesLome Pro%0A%0ANom: ${nom}%0ANuméro Mixx: ${num}%0AMontant: ${s} FCFA%0ANuméro connecté: +22870005827%0A%0AJe confirme avoir fait les tâches.`;
 window.open(`https://wa.me/22870005827?text=${msg}`,'_blank');
 alert('Demande envoyée sur WhatsApp à l\\'admin ! Tu seras payé par Mixx en 24h.');
 fermer();
}
</script>
</body></html>
    """
if __name__ == '__main__':
    app.run()
