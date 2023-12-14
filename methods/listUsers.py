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

# Imprimindo todos os usuários do banco, ordenando via id
print('\n-----------------')
for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

# Buscando no banco as informações "nome" e "idade" do usuário com nome "Kakashi"
print('\n-----------------')
for info in session.query(User.name, User.age).filter_by(name='Kakashi'):
    print(info)