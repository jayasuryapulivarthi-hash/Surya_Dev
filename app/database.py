from sqlalchemy import create_engine
try:
    from sqlalchemy.orm import sessionmaker
except Exception:
    # Fallback for environments where direct import may fail
    from sqlalchemy import orm
    sessionmaker = orm.sessionmaker

DATABASE_URL = "postgresql+psycopg://postgres:Surya%40sql@localhost:5432/Surya_Learning"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)