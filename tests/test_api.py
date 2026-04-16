from fastapi.testclient import TestClient
from src.api.main import app # Asegúrate de que esta ruta apunte a tu app de FastAPI

client = TestClient(app)

def test_health():
    """Verifica que el endpoint /health responda correctamente"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"Status": "ok"}