from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.route import router as router

# Instantiate the FastAPI application
app: FastAPI = FastAPI()

# Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://localhost:8081/*",
    allow_methods=['*'],
    allow_headers=['*'],
)

# Load up the router for the application
app.include_router(router)