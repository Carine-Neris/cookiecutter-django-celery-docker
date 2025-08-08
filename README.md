
# Django + Celery + Docker Template

Este projeto é um **template Cookiecutter** para iniciar rapidamente um projeto Django com Celery, Redis, PostgreSQL e Docker.

## ✨ Recursos

- 🐍 **Django 3.2** com estrutura otimizada
- 🔄 **Celery** para processamento assíncrono
- 📊 **Redis** como broker de mensagens
- 🗄️ **PostgreSQL** (escolha a versão)
- 🐳 **Docker** com docker-compose configurado
- 🔐 **Configuração automática** de SECRET_KEY
- 📁 **Ambiente virtual** criado automaticamente
- 🚫 **.gitignore** completo e otimizado
- 📧 **Configuração de email** via SMTP
- ☁️ **Integração AWS S3** para arquivos estáticos


## 🚀 Como Usar

### Pré-requisitos

- **Python 3.7+** instalado no sistema
- **Git** para clonar o repositório
- **Docker** (para execução em containers)

### 1. Instale o Cookiecutter

```bash
pip install cookiecutter
```

### 2. Gere Seu Projeto a Partir do Template

```bash
cookiecutter https://github.com/Carine-Neris/cookiecutter-django-celery-docker.git
```

Preencha as informações solicitadas e o Cookiecutter:
1. **Criará** a estrutura do projeto
2. **Configurará automaticamente** o ambiente:
   - ✅ Copia `.env.template` para `.env`
   - ✅ Gera e insere `SECRET_KEY` automaticamente
   - ✅ Cria ambiente virtual Python

| Campo              | Descrição                                          | Exemplo      |
| ------------------ | -------------------------------------------------- | ------------ |
| `folder_name`      | Nome da pasta principal do projeto                 | MeuProjeto   |
| `project_name`     | Nome do módulo Django (sem espaços, use \_ ou -)   | core\_app    |
| `author`           | Seu nome completo                                  | John Doe     |
| `app_name`         | Nome do app principal Django (sem espaços, use \_) | todo\_app    |
| `postgresql_version` | Versão do PostgreSQL (caso escolha PostgreSQL)   | 17           |

### 3. Rodando o Projeto

#### Com Docker (Recomendado):
```bash
cd seu_projeto
docker-compose up --build
```

#### Localmente (sem Docker):
```bash
cd seu_projeto

# Ativar ambiente virtual (criado automaticamente)
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# Configuração do Banco de Dados para execução local
Edite o arquivo .env conforme sua escolha:

Para PostgreSQL:
1. Instale PostgreSQL no seu sistema
2. Crie um banco de dados local
3. Configure no .env:
 DATABASE_URL=postgres://usuario:senha@localhost:5432/nome_do_banco

Para SQLite:
1. Configure diretamente no settings.py na seção DATABASES:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Executar migrações
python manage.py migrate

# Rodar servidor
python manage.py runserver
```

O Django estará disponível em [http://localhost:8000](http://localhost:8000).

### 4. Configurações Adicionais (Opcional)

O arquivo `.env` é criado automaticamente, mas você deve editá-lo para adicionar suas configurações específicas:

```env
# Configurações de E-mail
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha_app

# AWS S3 para arquivos estáticos/media
AWS_ACCESS_KEY=sua_chave_acesso
AWS_SECRET_KEY=sua_chave_secreta
AWS_BUCKET_NAME=seu_bucket
AWS_S3_REGION_NAME=us-east-1

```

### Estrutura do Projeto

```
{{cookiecutter.folder_name}}/
├── .env                     # Configurações (criado automaticamente)
├── .gitignore              # Arquivo gitignore completo
├── docker-compose.yml      # Configuração Docker
├── Dockerfile
├── requirements.txt
├── manage.py
├── venv/                   # Ambiente virtual (criado automaticamente)
├── {{cookiecutter.project_name}}
│   ├── asgi.py
│   ├── celery.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── {{cookiecutter.app_name}}
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tasks.py
│   ├── tests.py
│   └── views.py

   
```

---
Desenvolvido com ❤️ usando Cookiecutter.