#  Meu Blog Django

[![Python Version](https://img.shields.io/badge/python-3.10%20|%203.11%20|%203.12-blue.svg)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-4.2-green.svg)](https://www.djangoproject.com/)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Um blog completo no modelo MVT desenvolvido com Django, incluindo sistema de posts, categorias, comentários e painel administrativo. Esse projeto é somente para aprendizado, por sua simplicidade não houve necessidade de implementar REST.



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

# 7. Execute servidor e servidor com acesso externo
python manage.py runserver 
python manage.py runserver 0.0.0.0:8000 

##  Progressive Web App (PWA)

O blog é um **Progressive Web App (PWA)** completo que pode ser instalado no celular como um aplicativo nativo!

###  Funcionalidades PWA

| Funcionalidade | Status | Descrição |
|----------------|--------|-----------|
| **Instalação no Celular** | Implementado | "Adicionar à tela inicial" no Chrome/Android |
| **Modo Offline** |  Implementado | Cache de posts com Service Worker |
| **Ícone Personalizado** |  Implementado | Ícones para Android e iOS |
| **Splash Screen** |  Implementado | Tela de carregamento personalizada |
| **Modo Standalone** |  Implementado | Abre como app (sem barra do navegador) |

###  Como Instalar no Celular.

#### **Android (Chrome):**
1. Acesse o blog no Chrome
2. Toque em **"⋮" (Menu)** → **"Instalar aplicativo"**
3. Confirme a instalação
4. O ícone aparecerá na tela inicial

#### **iOS (Safari):**
1. Acesse o blog no Safari
2. Toque em **"Compartilhar"** 
3. Role para baixo e toque em **"Adicionar à Tela de Início"**
4. Confirme o nome e adicione

#### **Desktop (Chrome/Edge):**
1. Acesse o blog
2. Clique no ícone **"+"** na barra de endereços
3. Ou clique em **"Instalar [Nome do Blog]"**

###  Tecnologias PWA Utilizadas

- **Web App Manifest** (`manifest.json`) - Configuração do app
- **Service Worker** (`service-worker.js`) - Cache e offline
- **Cache API** - Armazenamento local de conteúdo


###  Testes PWA

Para testar as funcionalidades PWA:

```bash
# Teste com Lighthouse
npm install -g lighthouse
lighthouse http://localhost:8000 --view --output=html --output-path=./pwa-report.html

# Verifique o Service Worker
# No Chrome DevTools: Application → Service Workers