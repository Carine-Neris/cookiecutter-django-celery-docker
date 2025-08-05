
# Django + Celery + Docker Template

Este projeto é um **template Cookiecutter** para iniciar rapidamente um projeto Django com Celery, Redis, PostgreSQL e Docker.

## 🚀 Como Usar

### 1. Instale o Cookiecutter

```bash
pip install cookiecutter
```

### 2. Gere Seu Projeto a Partir do Template

```bash
cookiecutter https://github.com/seu-usuario/cookiecutter-django-celery-docker.git
```

Preencha as informações solicitadas (como o `project_slug`) e o Cookiecutter criará uma cópia do projeto com a estrutura correta.

### 3. Configure o Arquivo `.env`

Copie o arquivo `.env.template` para `.env`:

```bash
cp .env.template .env
```

Edite o `.env` preenchendo as seguintes variáveis:

```env
SECRET_KEY= # Gere com o comando abaixo
DEBUG=True
REDIS_URL=redis://redis:6379/0

EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=seu_email@gmail.com
EMAIL_HOST_PASSWORD=sua_senha

DATABASE_URL=postgres://usuario:senha@host:5432/nome_da_base

AWS_ACCESS_KEY=
AWS_SECRET_KEY=
AWS_BUCKET_NAME=
AWS_S3_REGION_NAME=
```

### 4. Gerar SECRET_KEY com o Django

Execute no terminal para gerar uma nova SECRET_KEY:

```bash
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 5. Rodando o Projeto com Docker

```bash
docker-compose up --build
```

O Django estará disponível em [http://localhost:8000](http://localhost:8000).

### Estrutura do Projeto

```
{{cookiecutter.project_slug}}/
├── docker-compose.yml
├── Dockerfile
├── .env
├── requirements.txt
├── manage.py
└── {{cookiecutter.project_slug}}/
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    ├── wsgi.py
    ├── celery.py
```

---
Desenvolvido com ❤️ usando Cookiecutter.