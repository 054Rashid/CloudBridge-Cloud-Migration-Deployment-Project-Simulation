import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_health():
    r = client.get('/health')
    assert r.status_code == 200
    assert r.json()['status'] == 'healthy'

def test_forecast():
    r = client.post('/forecast', json={'recent_demand': 100, 'growth_rate': 0.10})
    assert r.status_code == 200
    assert r.json()['forecast'] == 110.0
