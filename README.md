# Repositório de Propostas e projetos de Ensino, Pesquisa e Extensão - REPEX
Para usar o sistema, siga esses passos:

### Após baixar o projeto, ative a venv e instale as dependências:
    pip install -r requirements.txt

### Após isso faça as migrações:
    python manage.py migrate

## Para usar o login com suap, crie uma aplicação aouth2 e configure a redirect URI:
    <seu-domínio>/users/auth/callback/
#### URL em ambiente de desenvolvimento:
    http://localhost:8000/users/auth/callback/
    http://127.0.0.1:8000/users/auth/callback/

### Crie o arquivo .env e adicione:
    SUAP_CLIENT_ID = <seu-client-id>
    SUAP_CLIENT_SECRET = <seu-client-secret>

### Por fim, rode:
    python manage.py runserver
