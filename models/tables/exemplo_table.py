from sqlalchemy import Column, Integer, String
from config.database import Base


# Definindo a tabela Exemplo
class Exemplo(Base):

    # Nome da tabela
    __tablename__ = "exemplo"
    
    # Colunas da tabela
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    cpf = Column(String)
    rg = Column(String)
    motherName = Column(String)
    birthDate = Column(String)