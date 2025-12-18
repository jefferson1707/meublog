#  Meu Blog Django

[![Django CI](https://github.com/seu-usuario/meublog/actions/workflows/django-ci.yml/badge.svg)](https://github.com/seu-usuario/meublog/actions/workflows/django-ci.yml)
[![Python Version](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2-green.svg)](https://www.djangoproject.com/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Um blog completo no modelo MVT desenvolvido com Django, incluindo sistema de posts, categorias, comentários e painel administrativo. Esse projeto é somente para aprendizado.



##  Funcionalidades

-  Sistema de posts com categorias
-  Comentários em posts
-  Upload de imagens
-  Painel administrativo personalizado
-  Autenticação de usuários
-  Templates responsivos com Bootstrap 5
-  CI/CD com GitHub Actions

##  Tecnologias

- **Backend**: Django 4.2, Python 3.10+
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Banco de Dados**: PostgreSQL (produção), SQLite (desenvolvimento)
- **CI/CD**: GitHub Actions
- **Deploy**: Render/Railway/Vercel

##  Instalação Local

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/meublog.git
cd meublog

# 2. Crie ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou venv\Scripts\activate  # Windows

# 3. Instale dependências
pip install -r requirements.txt

# 4. Configure variáveis de ambiente
cp .env.example .env
# Edite .env com suas configurações

# 5. Execute migrações
python manage.py migrate

# 6. Crie superusuário
python manage.py createsuperuser

# 7. Execute servidor
python manage.py runserver