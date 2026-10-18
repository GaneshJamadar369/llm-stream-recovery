
from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

RESULT = {
    "A": {
        "text": "Report job-7f77b429: café\nReady ✓",
        "complete": True,
        "error": None
    },
    "B": {
        "text": "Partial job-7f77b429",
        "complete": False,
        "error": None
    },
    "C": {
        "text": "Draft job-7f77b429",
        "complete": False,
        "error": "model unloaded"
    }
}

@app.get("/")
def get_results():
    return JSONResponse(content=RESULT)
