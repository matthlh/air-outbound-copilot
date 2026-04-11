from fastapi import FastAPI
from app.api.routes_generate import router as generate_router

app = FastAPI(title="Air Outbound Copilot")
app.include_router(generate_router)


@app.get("/")
def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "Air Outbound Copilot"}
