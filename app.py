from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>TachesLome 🇹🇬</h1><p>Petits boulots a Lome - Ca marche !</p>"

if __name__ == '__main__':
    app.run()
