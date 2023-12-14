from sqlAlchemy import engine
from sqlalchemy.orm import sessionmaker

# Criar uma sessão
Session = sessionmaker(bind=engine)
session = Session()