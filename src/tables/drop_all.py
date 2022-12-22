from src.db.db import Base, engine

Base.metadata.drop_all(bind=engine)
