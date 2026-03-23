from sqlalchemy.orm import sessionmaker
from database.db import engine
from database.models import User
from schemas.returns.ret import Message


class UserRepository:
    def __init__(self):
        SessionLocal = sessionmaker(bind=engine)
        self.session = SessionLocal()

    def get_user_by_name(self, name: str):
        return self.session.query(User).filter(User.name == name).first()

    def get_user_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    def login(self, email, password):
        return bool(self.session.query(User).filter(User.email == email, User.password == password).first())

    def create_user(self, name: str, email: str, password: str):
        existing = self.get_user_by_name(name)
        if existing:
            return Message(
                name="User created",
                text="User name in use",
                success=False
            )
        db_user = User(
            name=name,
            email=email,
            password=password
        )
        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)
        return db_user

    def delete_user_by_name(self, name: str):
        user = self.get_user_by_name(name)
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

    #Bissnes logic for user
    def deposit(self, amount: int, username: str):
        user = self.get_user_by_name(username)
        if not user:
            return Message(name="Deposit", text="User not found", success=False)

        if amount > 0:
            user.balance += amount
            self.session.commit()
            return Message(name="Deposit", text="Successfully", success=True)

        return Message(name="Deposit", text="Amount must be positive", success=False)

    def withdraw(self, amount: int, username: str):
        user = self.get_user_by_name(username)
        if not user:
            return Message(name="Withdraw", text="User not found", success=False)

        if user.balance >= amount:
            user.balance -= amount
            self.session.commit()
            return Message(name="Withdraw", text="Successfully", success=True)

        return Message(name="Withdraw", text="Insufficient balance", success=False)

    def transfer(self, from_username: str, to_username: str, amount: int):
        from_user = self.get_user_by_name(from_username)
        to_user = self.get_user_by_name(to_username)

        if not from_user or not to_user:
            return Message(name="Transfer", text="User not found", success=False)

        if amount <= 0:
            return Message(name="Transfer", text="Amount must be positive", success=False)

        if from_user.balance < amount:
            return Message(name="Transfer", text="Insufficient balance", success=False)

        from_user.balance -= amount
        to_user.balance += amount
        self.session.commit()

        return Message(name="Transfer", text="Successfully", success=True)