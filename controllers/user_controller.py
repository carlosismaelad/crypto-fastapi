from fastapi import APIRouter, HTTPException
from schemas.schemas import UserCreateInput, StandardOutput, AlternativeOutput
from services import user_services

user_router = APIRouter()

@user_router.post('/user', response_model=StandardOutput, responses={418: {'model': AlternativeOutput}})
async def user_create(user_input: UserCreateInput):
    try:
        await user_services.create_user(name=user_input.name)
        return StandardOutput(message='Usuário criado com sucesso!')
    except Exception as e:
        print(f"An error ocurred while creating user: {e}")
        raise HTTPException(status_code=418, detail=str(e))

