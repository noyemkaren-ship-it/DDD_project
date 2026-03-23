# init_db.py
from database.db import engine, Base
from database.models import User

print("Создаю таблицы...")
Base.metadata.create_all(bind=engine)
print("✅ Таблицы созданы!")