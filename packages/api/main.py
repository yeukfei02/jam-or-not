from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from bacinet import BacinetMiddleware
from routes.traffic_images_routes import traffic_images_router
from routes.detections_routes import detections_router

load_dotenv()

app = FastAPI()

# middleware

# cors
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# helmet
app.add_middleware(BacinetMiddleware)

# routes
app.include_router(traffic_images_router)
app.include_router(detections_router)
