from fastapi import APIRouter, Depends
from models import exemplo_model as exemploModel
from sqlalchemy.orm import Session
import config.database as database
from models.tables import exemplo_table as exemploTable


# Identifica que é uma router
router = APIRouter()

#Realiza a sessão do banco local
def get_db():
    db = database.SessionLocal()
    try:
        yield db

    finally:
        db.close()

# Exemplo de um método GET
@router.get("/")

# Skip define a paginação e limit é a quantidade por página
async def get_exemplo(db: Session=Depends(get_db) ,skip: int = 0, limit: int = 10):

    #Realiza a requisição para o banco
    return db.query(exemploTable.Exemplo).offset(skip).limit(limit).all()

# Exemplo de um método POST
@router.post("/")
async def post_exemplo(exemplo: exemploModel.Exemplo, db: Session = Depends(get_db)):

    # Aqui relacionamos os dados recebidos com o modelo da tabela
    db_exemplo = exemploTable.Exemplo(name = exemplo.name, cpf = exemplo.cpf, rg = exemplo.rg, motherName = exemplo.motherName, birthDate = exemplo.birthDate)
    
    # Adiciona as alterações a serem feitas
    db.add(db_exemplo)

    # Comitta as alterações
    db.commit()

    # Atualiza os dados da sessão SQLite3
    db.refresh(db_exemplo)

    return db_exemplo
