from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from .routers import tickets, products
from .config import settings
from .db.database import get_db

app = FastAPI(dependencies=[Depends(get_db)])

origins = [
    "http://localhost:3001",
    "http://localhost:3000",
    "https://zen-meninsky-88deba.netlify.app/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(tickets.router)
app.include_router(products.router)

@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
