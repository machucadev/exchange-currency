import requests

API_KEY = "7fbe88347a145d0d33fc23dd94e937fd"

def convertir_moneda(from_currency, to_currency, amount):
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    url = f"http://api.exchangeratesapi.io/v1/latest?access_key={API_KEY}&symbols={from_currency},{to_currency}"

    try:
        r = requests.get(url)
        data = r.json()
        print("📦 API Response:", data)

        if data.get("success", False):
            rates = data["rates"]
            if from_currency not in rates or to_currency not in rates:
                return None

            tasa_desde = rates[from_currency]
            tasa_hasta = rates[to_currency]
            tasa_cruzada = tasa_hasta / tasa_desde
            return amount * tasa_cruzada
        return None
    except Exception as e:
        print("❌ Error:", e)
        return None
