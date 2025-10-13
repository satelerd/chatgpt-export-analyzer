def minutos_tracking_v3(tracking_id: str, **kwargs):
    """
    Devuelve la descripción legible del estado de una orden 99minutos.
    Si falla algo, retorna un dict con información del error.
    """

    import requests
    from typing import Any, Dict

    # --- Credenciales por agente -----------------------------------------
    _CREDENTIALS: Dict[str, Dict[str, str]] = {
        # Colombia
        "99-minutos-colombia": {
            "client_id": "3e617969-f95f-4df6-8e64-bb54e35612e0",
            "client_secret": "iohAuocOCm_5J4JQMcuY_LqQTbSm3_",
        },
        # Alias "Caleb" -> mismas credenciales Colombia
        "Caleb": {
            "client_id": "d8d9660c-8c61-45db-b40a-62952b5f3f03",
            "client_secret": "F2I8_AOyPRDIUgRv8DtH48fqX53yPf",
        },
        # Chile
        "99-minutos": {
            "client_id": "d8d9660c-8c61-45db-b40a-62952b5f3f03",
            "client_secret": "F2I8_AOyPRDIUgRv8DtH48fqX53yPf",
        },
        # Perú
        "99-minutos-peru": {
            "client_id": "33880b1c-e45e-4d0d-9e38-f69e7c1da85b",
            "client_secret": "o4omVtl_M2Wzc1p_zv-3SB8vhjnK6-",
        },
    }

    # --- Mapeo currentState -> descripción --------------------------------
    _STATE_MAP = {
        "1001": "Borrador",
        "1002": "Orden confirmada",
        "2001": "Lista para recolección",
        "2002": "En camino a recolección",
        "2003": "Orden recolectada",
        "2101": "Recolección fallida",
        "3001": "En almacén",
        "3002": "En almacén",
        "3003": "En almacén",
        "3004": "En transporte",
        "4001": "En camino a entrega",
        "4002": "Entrega confirmada",
        "4003": "Entrega parcial",
        "4101": "Entrega fallida",
        "5001": "En camino a devolución",
        "5002": "Orden devuelta",
        "5101": "Devolución fallida",
        "7101": "En corrección",
        "7102": "Corregido",
        "7401": "Máximo de intentos de entrega",
        "7501": "Máximo de intentos de devolución",
        "8001": "Robado",
        "8002": "Perdido",
        "8003": "Cancelado",
        "8004": "Dañado",
        "8005": "Dirección inválida",
        "8006": "Cierre indeterminado",
        "8101": "Borrador cancelado por usuario",
        "8102": "Borrador archivado",
        "8201": "Excedido máximo de intentos",
    }

    _HOST = "https://providers99.99minutos.com"

    # --------- Elegir credenciales según agente --------------------------
    agent_name = kwargs.get("automatic_agent_name")
    print(f"DEBUG: agent_name = {agent_name}")
    print(f"DEBUG: kwargs = {kwargs}")
    
    creds = _CREDENTIALS.get(agent_name)
    if not creds:
        print(f"DEBUG: No se encontraron credenciales para agente '{agent_name}'")
        return {
            "error": f"El agente '{agent_name}' no tiene credenciales configuradas.",
            "status_code": 400,
        }

    print(f"DEBUG: Usando credenciales para agente '{agent_name}'")

    # --------- Paso 1: obtener JWT ---------------------------------------
    try:
        token_resp = requests.post(
            f"{_HOST}/api/v1/oauth/token",
            json={
                "client_id": creds["client_id"],
                "client_secret": creds["client_secret"],
            },
            timeout=10,
        )
        print(f"DEBUG: Token response status = {token_resp.status_code}")
    except requests.RequestException as exc:
        print(f"DEBUG: Error en autenticación: {exc}")
        return {"error": f"Falla en autenticación: {exc}", "status_code": 500}

    if token_resp.status_code != 200:
        print(f"DEBUG: Error obteniendo JWT: {token_resp.status_code} - {token_resp.text}")
        return {
            "error": "No se pudo obtener JWT",
            "status_code": token_resp.status_code,
            "detail": token_resp.text,
        }

    access_token = token_resp.json().get("access_token")
    print(f"DEBUG: JWT obtenido exitosamente")

    # --------- Paso 2: pedir tracking ------------------------------------
    try:
        track_resp = requests.get(
            f"{_HOST}/api/v1/tracking/{tracking_id}",
            headers={"Authorization": f"Bearer {access_token}"},
            timeout=10,
        )
        print(f"DEBUG: Tracking response status = {track_resp.status_code}")
        print(f"DEBUG: Tracking response text = {track_resp.text}")
    except requests.RequestException as exc:
        print(f"DEBUG: Error en consulta de tracking: {exc}")
        return {"error": f"Falla en consulta de tracking: {exc}", "status_code": 500}

    # --------- Paso 3: procesar respuesta --------------------------------
    if track_resp.status_code in (200, 201):
        payload = track_resp.json()
        data = payload.get("data", payload)      # 200 -> todo en raíz. 201 -> viene bajo 'data'
        current_state = str(data.get("currentState", "")).strip()
        print(f"DEBUG: current_state = {current_state}")

        return _STATE_MAP.get(
            current_state,
            f"Estado desconocido ({current_state})",
        )

    # Si el HTTP no es éxito, devolver info de error
    print(f"DEBUG: Error HTTP {track_resp.status_code}: {track_resp.text}")
    return {
        "error": "Error al consultar la orden",
        "status_code": track_resp.status_code,
        "detail": track_resp.text
    }

# Pruebas
if __name__ == "__main__":
    print("=== Prueba 1: Sin automatic_agent_name ===")
    result1 = minutos_tracking_v3("1871805191")
    print(f"Resultado: {result1}")
    
    print("\n=== Prueba 2: Con automatic_agent_name = '99-minutos' ===")
    result2 = minutos_tracking_v3("1871805191", automatic_agent_name="99-minutos")
    print(f"Resultado: {result2}")
