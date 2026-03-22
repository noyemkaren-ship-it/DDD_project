from database.db import Base, engine

Base.metadata.create_all(engine)
print("Таблицы созданный!!!")