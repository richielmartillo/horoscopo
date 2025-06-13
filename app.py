from flask import Flask, render_template
from datetime import datetime
import random

app = Flask(__name__)

horoscopos = {
    "Áries": [
        "Hoje é um bom dia para iniciar projetos.",
        "Aja com cautela nas finanças.",
        "Encare desafios com otimismo."
    ],
    "Touro": [
        "Foque em seu bem-estar.",
        "Seja flexível no trabalho.",
        "Um reencontro pode surpreender."
    ],
    "Gêmeos": [
        "A comunicação será seu ponto forte.",
        "Evite discussões desnecessárias.",
        "Novas ideias podem surgir."
    ]
}

@app.route("/")
def index():
    data_hoje = datetime.now().strftime("%d/%m/%Y")
    horoscopo_dia = {s: random.choice(mensagens) for s, mensagens in horoscopos.items()}
    return render_template("index.html", data=data_hoje, horoscopo=horoscopo_dia)

if __name__ == "__main__":
    app.run(debug=True) 
