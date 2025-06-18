from flask import Flask, request, jsonify
from app.cupones import calcular_precio_final

app = Flask(__name__)

@app.route('/precio', methods=['POST'])
def calcular():
    data = request.get_json()
    precio  = data.get("precio")
    cupon   = data.get("cupon")
    impuesto= data.get("impuesto", 0.19)
    final   = calcular_precio_final(precio, cupon, impuesto)
    return jsonify({"precio_final": final})
