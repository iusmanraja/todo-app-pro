from fastapi import FastAPI
from dotenv import load_dotenv
from Dummy_structure.app.api.task.routes import router as task_router

load_dotenv()

app = FastAPI()

app.include_router(task_router)