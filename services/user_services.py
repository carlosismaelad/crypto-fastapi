from models.models import User
from database.connection import async_session

class UserServices:

    async def create_user():
        async with async_session() as session:
            session.add(User(name=name))
            await session.commit()