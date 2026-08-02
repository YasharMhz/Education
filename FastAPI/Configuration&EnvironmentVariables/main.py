from fastapi import FastAPI,Depends
from config import settings,get_settings


app = FastAPI()

@app.get("/")
def home(settings= Depends(get_settings)):
    return{
        "project's name" : settings.project_name,
        "version" : settings.version,
        "debug" : settings.debug
    }

# @app.get("/")
# def home():
#     return {
#         "project" :settings.project_name,
#         "version" :settings.version
#     }
# @app.get("/")
# def home():
#     return {
#         "app": settings.app_name,
#         "debug": settings.debug
#     }