from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get("message", "").lower()
    
    if "hola" in user_message:
        reply = "¡Hola! Soy Lian-PRO. Mi servidor ya está en la nube."
    elif "record" in user_message:
        reply = "¡Estamos configurando el servidor para el Récord Guinness!"
    else:
        reply = "Lian recibió tu mensaje y está procesando..."
        
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
