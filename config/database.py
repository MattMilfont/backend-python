from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Endereço do banco de dados (Pode ser utilizado qualquer um)
SQLALCHEMY_DATABASE_URL = "sqlite:///exemplo.db"

# Criação da Engine (Nesse caso para o SQLite)
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Utilizar para fazer sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria a Base Declarativa
Base = declarative_base()
