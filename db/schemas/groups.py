from db.config import BaseModel
from sqlalchemy.orm import relationship, mapped_column, Mapped

class GroupsTable(BaseModel):
    __tablename__ = 'groups_group'

    chat_id: Mapped[int] = mapped_column(unique=True)
    invite_link: Mapped[str] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(unique=True)
    name: Mapped[str] = mapped_column(nullable=True)
    
    game_histories: Mapped[list["GamesHistoryTable"]] = relationship(back_populates="chat")