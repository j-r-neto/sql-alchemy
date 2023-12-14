import sys
import os

# Obtém o diretório do script atual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Obtém o diretório do projeto (assumindo que o projeto está um nível acima de methods)
project_dir = os.path.dirname(script_dir)

# Adiciona o diretório do projeto ao sys.path
sys.path.append(project_dir)

# Agora você pode importar o User de models
from models import User
from createSession import session
# ---------------------------------------------------------------------------------------

# Buscando no banco a primeira corresponência do usuário de nome "Kakashi"
user = session.query(User).filter_by(name="Kakashi").first()

# Apagando o usuário
session.delete(user)

# Enviando as atualizações para o banco de dados
session.commit()