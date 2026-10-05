from fastapi import FastAPI

app = FastAPI(title="Maintenance Service")


@app.get("/maintenance")
def health():
    return {
        "service": "maintenance-service",
        "status": "running"
    }
