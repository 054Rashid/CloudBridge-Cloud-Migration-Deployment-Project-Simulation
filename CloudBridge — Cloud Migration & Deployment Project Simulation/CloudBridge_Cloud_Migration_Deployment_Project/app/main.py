from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="CloudBridge Demand Insights API", version="1.0.0")

class ForecastRequest(BaseModel):
    recent_demand: float = Field(..., ge=0)
    growth_rate: float = Field(default=0.03, ge=-1, le=2)

class ForecastResponse(BaseModel):
    baseline: float
    growth_rate: float
    forecast: float

@app.get("/health")
def health() -> dict:
    return {"status": "healthy", "service": "cloudbridge-api"}

@app.get("/version")
def version() -> dict:
    return {"version": "1.0.0"}

@app.post("/forecast", response_model=ForecastResponse)
def forecast(request: ForecastRequest) -> ForecastResponse:
    value = round(request.recent_demand * (1 + request.growth_rate), 2)
    return ForecastResponse(baseline=request.recent_demand, growth_rate=request.growth_rate, forecast=value)
