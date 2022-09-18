from sqlalchemy import create_engine

DATABASE_URL: str = 'postgresql://rock:rock1984@localhost:5432/bh33d'
SYNC_ENGINE = create_engine(url=DATABASE_URL)
