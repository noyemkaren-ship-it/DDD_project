from sqlalchemy.orm import Session
from database.models import User
from schemas.returns.ret import Message

class UserRepository:
    def __init__(self):
        self.session = Session()

    def create_user(self, name: str, email: str, password: str):
        db_user = User(
            username=name,
            email=email,
            password=password
        )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def get_user_by_username(self, username: str):
        db_user = self.session.query(User).filter(User.username == username).first()
        return db_user

    def delete_user_by_username(self, username: str):
        if username in self.session.query(User).all():
            self.session.query(User).filter(User.username == username).delete()
            return Message(
                name="User delete",
                text="User deleted is succesfully",
                success=True
            )
        else:
            return Message(
                name="User delete",
                text="User not found",
                success=False
            )

    def get_user_all(self):
        return self.session.query(User).all()