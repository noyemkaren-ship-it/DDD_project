from sqlalchemy.orm import Session
from database.models import User
from schemas.returns.ret import Message

class UserRepository:
    def __init__(self):
        self.session = Session()


    def get_user_by_username(self, username: str):
        db_user = self.session.query(User).filter(User.username == username).first()
        return db_user

    def login(self, email, password):
        if self.session.query(User).filter(User.email == email, User.password == password).first():
            return True


    def create_user(self, name: str, email: str, password: str):
        db_user = User(
            username=name,
            email=email,
            password=password
        )
        user_name = self.get_user_by_username(db_user.username)
        if user_name:
            return Message(
                name="User created",
                text="User name in use",
                success=False
            )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user


    def delete_user_by_username(self, username: str):
        user = self.get_user_by_username(username)
        if user:
            self.session.delete(user)
            self.session.commit()
            return Message(
                name="User delete",
                text="User deleted successfully",
                success=True
            )
        return Message(
            name="User delete",
            text="User not found",
            success=False
        )

    def get_user_all(self):
        return self.session.query(User).all()

    def get_user_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()