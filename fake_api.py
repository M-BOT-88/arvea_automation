from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/stock/getQuantity", methods=["GET"])
def get_quantity():
    product_config_id = request.args.get("product_config_id")
    stock_type = request.args.get("stock_type")
    depot_id = request.args.get("depot_id")

    if stock_type != "depot":
        return jsonify({"error": "invalid stock type"}), 400

    # Simule la réponse avec une quantité
    return jsonify({
        "quantity": 10  # Change à 0 pour simuler "non dispo"
    })

if __name__ == "__main__":
    app.run(port=5000)
