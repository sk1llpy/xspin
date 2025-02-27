from sqlalchemy.orm import Session

from db.repository import BaseRepository
from db.schemas import UsersTable

class UsersTableRepository(BaseRepository):
    table = UsersTable

    async def get_user(self, user_id: int, session: Session):
        with session:
            user: UsersTable = self.get(attribute="user_id", value=user_id, session=session)

            return user

    async def create_user(self, user_id: int, username: str | None, name: str, session: Session):
        with session:
            user = await self.get_user(user_id=user_id, session=session)
            if not user:
                return self.create(params={
                    "user_id": user_id,
                    "username": username,
                    "name": name
                }, session=session)

    async def get_balance(self, user_id: int, session: Session):
        with session:
            user = await self.get_user(user_id=user_id, session=session)
            if user:
                return user.balance
            else:
                return None
