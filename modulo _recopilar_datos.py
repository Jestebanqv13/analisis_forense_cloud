import requests  # La librería se llama "requests", no "request"


def recolectar_datos(token_auth):
    # Logica para recopilar datos de la plataforma en la nube
    url = "https://api.cloudplatform.com/get_data"
    # Debería ser "Authorization" en lugar de "Autorizacion"
    encabezados = {"Autorizacion": f"Bearer {token_auth}"}

    try:
        # La función es "requests.get", no "request.get"
        respuesta = requests.get(url, headers=encabezados)
        respuesta.raise_for_status()

        datos = respuesta.json()
        return datos

    # "requests.exceptions" en lugar de "resquest.exceptions"
    except requests.exceptions.RequestException as e:
        print(f"Error al recopilar datos: {e}")
        return None
