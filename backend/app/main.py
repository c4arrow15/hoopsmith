from fastapi import FastAPI, HTTPException


app = FastAPI(title = "HoopsmithAPI")


@app.get("/api/health")
def health():
    return {"status": "ok"}