from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from dashboard_routes import router as dashboard_router
from filtered_dashboard_routes import router as filtered_dashboard_router

app = FastAPI(
    title="API Analítica de Compras Masivas",
    description="Backend para dashboard analítico sobre Apache Doris",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def health_check():
    return {
        "message": "API de analítica funcionando correctamente"
    }


app.include_router(dashboard_router)
app.include_router(filtered_dashboard_router)
