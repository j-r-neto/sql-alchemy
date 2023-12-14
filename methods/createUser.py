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

# Criar instância da classe
user = User(name='John', fullname='John Doe', age=20)

# Adicionar objeto (INSERT)
session.add(user)

# Adicionando vários objetos
session.add_all([
    User(name='Obito', fullname='Uchiha Obito', age=20),
    User(name='Kakashi', fullname='Hatake Kakashi', age=20),
    User(name='Rin', fullname='Nohara Rin', age=20)
])

# Enviando atualizações para o banco de dados
session.commit()