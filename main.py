from fastapi import FastAPI, APIRouter
import uvicorn

app = FastAPI()
router = APIRouter()

@router.get('/')
def first():
    return 'Hello from FastAPI!'

app.include_router(prefix='/home', router=router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, reload=True)