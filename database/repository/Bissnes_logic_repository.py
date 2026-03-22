from sqlalchemy.orm import Session
from schemas.returns.ret import Message


class BusinessLogicRepository:
    def __init__(self, session: Session):
        self.session = session

    def withdraw(self, amount: int, user):
        if user.balance >= amount:
            user.balance -= amount
            self.session.commit()
            return Message(
                name='Withdraw',
                text="Successfully",
                success=True
            )
        return Message(
            name='Withdraw',
            text='Insufficient balance',
            success=False
        )

    def deposit(self, amount: int, user):
        if amount > 0:
            user.balance += amount
            self.session.commit()
            return Message(
                name='Deposit',
                text="Successfully",
                success=True
            )
        return Message(
            name='Deposit',
            text='Amount must be positive',
            success=False
        )

    def transfer(self, from_user, to_user, amount):
        if amount <= 0:
            return Message(
                name='Transfer',
                text="Amount must be positive",
                success=False
            )

        withdraw_result = self.withdraw(amount, from_user)
        if not withdraw_result.success:
            return withdraw_result

        deposit_result = self.deposit(amount, to_user)
        return deposit_result