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

# Buscando no banco a primeira correspondência do nome "Kakashi"
query_user = session.query(User).filter_by(name='Kakashi').first()
print(query_user.fullname)

