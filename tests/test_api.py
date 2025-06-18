'''import pytest
from app.api import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_precio_oferta10_por_defecto(client):
    # Cupón válido, impuesto por defecto (0.19)
    resp = client.post('/precio', json={
        "precio": 100,
        "cupon": "OFERTA10"
    })
    assert resp.status_code == 200
    data = resp.get_json()
    # 100 * 0.90 = 90.00, luego *1.19 = 107.1
    assert data["precio_final"] == pytest.approx(107.1)

def test_precio_super20_con_impuesto_personalizado(client):
    # Cupón válido, impuesto al 10%
    resp = client.post('/precio', json={
        "precio": 200,
        "cupon": "SUPER20",
        "impuesto": 0.10
    })
    assert resp.status_code == 200
    data = resp.get_json()
    # 200 * 0.80 = 160.00, luego *1.10 = 176.0
    assert data["precio_final"] == pytest.approx(176.0)

def test_precio_cupon_no_existente(client):
    # Cupón inválido, no descuenta
    resp = client.post('/precio', json={
        "precio": 50,
        "cupon": "INVALIDO"
    })
    assert resp.status_code == 200
    data = resp.get_json()
    # Sin descuento: 50 * 1.19 = 59.5
    assert data["precio_final"] == pytest.approx(59.5)

def test_precio_sin_cuerpo_json(client):
    # Petición sin JSON
    resp = client.post('/precio')
    # Debería recibir 400 o bien un error manejado
    assert resp.status_code == 400 or resp.status_code == 415

def test_precio_campos_incompletos(client):
    # Falta el campo 'precio'
    resp = client.post('/precio', json={"cupon": "OFERTA10"})
    assert resp.status_code == 400
    # Falta el campo 'cupon'
    resp = client.post('/precio', json={"precio": 100})
    assert resp.status_code == 400
'''