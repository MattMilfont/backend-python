from pydantic import BaseModel

# Essa é uma Classe para uma entidade
class Exemplo(BaseModel):

    # Aqui você declara todas as características dessa entidade
    name: str
    cpf: str
    rg: str
    motherName: str
    birthDate: str

