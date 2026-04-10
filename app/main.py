from fastapi import FastAPI

app = FastAPI(title="Air Outbound Copilot")


@app.get("/")
def healthcheck() -> dict[str, str]:
    return {"status": "ok", "service": "Air Outbound Copilot"}
