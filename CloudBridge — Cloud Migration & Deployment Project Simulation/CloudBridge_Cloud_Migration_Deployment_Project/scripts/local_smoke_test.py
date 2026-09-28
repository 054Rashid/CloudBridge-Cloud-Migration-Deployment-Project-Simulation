import sys
from pathlib import Path
from fastapi.testclient import TestClient
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'app'))
from main import app

client = TestClient(app)
health = client.get('/health')
forecast = client.post('/forecast', json={'recent_demand': 100, 'growth_rate': 0.05})
assert health.status_code == 200 and health.json()['status'] == 'healthy'
assert forecast.status_code == 200 and forecast.json()['forecast'] == 105.0
print('Smoke test passed: health + forecast endpoints are working.')
