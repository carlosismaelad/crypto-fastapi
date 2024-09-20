from fastapi import FastAPI, APIRouter
from controllers.user_controller import user_router
import uvicorn

app = FastAPI()
router = APIRouter()

@router.get('/')
def first():
    return 'Hello from FastAPI!'

app.include_router(prefix='/home', router=router)
app.include_router(user_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)