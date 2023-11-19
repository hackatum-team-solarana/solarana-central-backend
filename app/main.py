from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.routes import marketplace_route
from app.utils.db import engine
from app.models import offers

offers.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(marketplace_route.router)


@app.get("/")
async def docs_redirect():
    return RedirectResponse(url='/docs')
