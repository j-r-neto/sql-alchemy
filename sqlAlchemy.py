import sqlalchemy
from dotenv import load_dotenv
import os
from models import Base

# Modulo para ler dados de um dotenv
load_dotenv()

db_user = os.getenv("DATABASE_USER")
db_pass = os.getenv("DATABASE_PASS")
db_host = os.getenv("DATABASE_HOST")
db_name = os.getenv("DATABASE_NAME")

# Configurando a conexão com o banco de dados
engine = sqlalchemy.create_engine(f"postgresql://{db_user}:{db_pass}@{db_host}/{db_name}", echo=True)

# Criando a tabela no banco de dados
Base.metadata.create_all(engine)
