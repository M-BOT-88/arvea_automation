import requests

def test_product_availability_in_depot():
    print("🧪 Test lancé...")  # ✅ Ajout de ce print
    base_url = "http://127.0.0.1:5000"  # Fausse URL
    endpoint = "/stock/getQuantity"
    product_config_id = "12345"
    stock_type = "depot"
    depot_id = "67890"

    response = requests.get(
        f"{base_url}{endpoint}",
        params={
            "product_config_id": product_config_id,
            "stock_type": stock_type,
            "depot_id": depot_id
        }
    )

    assert response.status_code == 200

    data = response.json()
    assert "quantity" in data
    assert isinstance(data["quantity"], int)

    if data["quantity"] > 0:
        print("✅ Produit disponible dans le dépôt")
    else:
        print("❌ Produit non disponible dans le dépôt")

test_product_availability_in_depot()
