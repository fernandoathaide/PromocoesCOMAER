# PromocoesCOMAER

Digital Twin do processo de promoções
uv sync
source .venv/bin/activate
uvicorn backend.app.main:app --reload
 1244  uv venv
 1245  python -m venv .venv
 1246  python3 --version
 1247  sudo apt update
 1248  sudo apt install python3.10-venv python3-pip
 1249  curl -LsSf https://astral.sh/uv/install.sh | sh
 1250  python3 --version
 1251  uv --version
 1252  uv venv
 1253  source .venv/bin/activate
 1254  uv sync
 1255  uvicorn backend.app.main:app --reload
 1256  uname -a
 1257  psql --version
 1258  sudo apt update
 1259  sudo apt install postgresql postgresql-contrib
 1260  sudo apt install postgresql-client libpq-dev
 1261  psql --version
 1262  sudo systemctl status postgresql
 1263  pg_lsclusters
 1264  sudo -u postgres psql
 1265  psql -h localhost -U postgres -d promocoescomaer
 1266  sudo nano /etc/postgresql/14/main/postgresql.conf
 1267  sudo systemctl restart postgresql
 1268  sudo nano /etc/postgresql/14/main/pg_hba.conf
 1269  udo ifconfig
 1270  sudo ifconfig
 1271  sudo nano /etc/postgresql/14/main/pg_hba.conf
 1272  sudo systemctl restart postgresql
 1273  sudo systemctl status postgresql
 1274  uvicorn backend.app.main:app --reload
 1275  git status
 1276  git add .
 1277  git commit -m "130726 - Configura ambiente de desenvolvimento local CASA."
 1278  git push
 1279  git config --global credential.helper store


# ghp

## _xT0dtqnujO1QsozKywqAj0V04xwwb92aZlsw ##

| Item         | Padrão              |
| ------------ | ------------------- |
| Python       | 3.10+               |
| Estilo       | PEP 8               |
| Line Length  | 100                 |
| Type Hints   | Obrigatório         |
| Docstrings   | Google Style        |
| Logging      | Rich                |
| ORM          | SQLAlchemy 2.x      |
| Configuração | Pydantic Settings   |
| Banco        | PostgreSQL + Oracle |
| API          | FastAPI             |
| Testes       | Pytest              |

core/

settings.py

↓

config.py

↓

logging.py

↓

database.py

source .venv/bin/activate
python -m pip show oracledb
python -m backend.app.infrastructure.etl.jobs.sync_pesfis
psql -U postgres -d postgres

git pull
uv sync

## uv run alembic upgrade head    # se o projeto usar migrations

uv run uvicorn backend.app.main:app --reload

# PromocoesCOMAER

> Plataforma de Apoio à Decisão para Promoções de Oficiais-Generais do COMAER

![Status](https://img.shields.io/badge/status-Sprint%204-blue)
![Python](https://img.shields.io/badge/Python-3.10+-green)
![FastAPI](https://img.shields.io/badge/FastAPI-0.116+-009688)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-14+-336791)
![License](https://img.shields.io/badge/License-GPLv3-red)

---

# Sobre o Projeto

O **PromocoesCOMAER** é uma plataforma de apoio à decisão desenvolvida para atuar como um **Digital Twin (Gêmeo Digital)** do processo de promoções dos Oficiais-Generais da Força Aérea Brasileira (COMAER).

Seu propósito é fornecer um ambiente seguro para análises, simulações e projeções estratégicas utilizando dados corporativos, sem qualquer impacto sobre os sistemas oficiais utilizados pela Instituição.

O sistema foi concebido para transformar informações operacionais em conhecimento estratégico, permitindo avaliar diferentes cenários antes da tomada de decisão.

---

# Objetivos

- Construir uma base analítica independente do Oracle corporativo.
- Disponibilizar um ambiente seguro para estudos estratégicos.
- Automatizar análises atualmente realizadas por planilhas.
- Permitir simulações de promoções, efetivos e reservas.
- Projetar cenários futuros utilizando regras de negócio.
- Disponibilizar indicadores gerenciais.
- Integrar Inteligência Artificial para interpretação dos resultados.

---

# Estado Atual do Projeto

**Versão:** 0.4.0

**Sprint Atual:** Sprint 4 (Concluída)

## Funcionalidades Implementadas

- Estrutura do projeto definida.
- Backend FastAPI.
- PostgreSQL configurado.
- Alembic para versionamento do banco.
- Ambiente de desenvolvimento utilizando uv.
- Estrutura inicial do ETL.
- Scripts de instalação e manutenção.
- Snapshot inicial da base Oracle.
- Organização das camadas RAW, CORE e ANALYTICS.
- Base para o Motor de Simulação.

---

# Arquitetura

```text
                 Oracle SIG
                      │
                      ▼
             ETL (Python)
                      │
                      ▼
             PostgreSQL
      ┌──────────┴──────────┐
      │                     │
    RAW                  CORE
      │                     │
      └──────────┬──────────┘
                 ▼
            ANALYTICS
                 │
                 ▼
        Simulation Engine
                 │
                 ▼
             FastAPI
                 │
                 ▼
        React + Apache ECharts
                 │
                 ▼
              Usuário
```

---

# Tecnologias

## Backend

- Python 3.10+
- FastAPI
- SQLAlchemy
- Alembic
- Pydantic
- Uvicorn

## Banco de Dados

- PostgreSQL 14+

## Frontend

- React
- TypeScript
- Vite
- Apache ECharts

## Inteligência Artificial

- OpenAI GPT
- Claude Sonnet

## Infraestrutura

- Docker
- Docker Compose
- Debian Linux
- Nginx

## Controle de Versão

- Git
- GitHub

---

# Estrutura do Projeto

```text
PromocoesCOMAER/

backend/
    app/
    api/
    core/
    models/
    services/

database/
    migrations/
    snapshots/
    seeds/

docs/

scripts/

tests/

docker/

ai/

frontend/

.env.example
README.md
pyproject.toml
uv.lock
```

---

# Modelo de Dados

O banco de dados foi organizado em camadas.

## RAW

Armazena cópia dos dados provenientes do Oracle.

Nenhuma regra de negócio é aplicada.

---

## CORE

Camada de integração.

Responsável pela padronização dos dados utilizados pelas regras de negócio.

---

## ANALYTICS

Base otimizada para consultas, indicadores e dashboards.

---

## SIMULATION

Responsável pelos cenários simulados.

---

## CONFIG

Parâmetros do sistema.

---

## AUDIT

Auditoria das operações.

---

# Motor de Simulação

O Motor de Simulação representa o núcleo do PromocoesCOMAER.

Será responsável por:

- Simular promoções.
- Simular reservas.
- Projetar efetivos.
- Simular alterações de vagas.
- Calcular probabilidades.
- Aplicar regras de negócio.
- Gerar indicadores.
- Explicar decisões.

Toda decisão será acompanhada da justificativa correspondente.

---

# ETL

Fluxo de processamento dos dados:

```text
Oracle SIG
      │
Extração
      │
Transformação
      │
Carga RAW
      │
Validação
      │
CORE
      │
Analytics
```

---

# API REST

A API é construída utilizando FastAPI.

Principais recursos:

- Consulta de militares.
- Consulta de promoções.
- Indicadores.
- Simulações.
- Administração.
- Configuração.

A documentação OpenAPI estará disponível em:

```
/docs
```

---

# Ambiente de Desenvolvimento

## Requisitos

- Python 3.10+
- PostgreSQL 14+
- Git
- uv

---

## Instalação

Clone o projeto.

```bash
git clone https://github.com/<usuario>/PromocoesCOMAER.git
```

Entre na pasta.

```bash
cd PromocoesCOMAER
```

Crie o ambiente virtual.

```bash
uv venv
```

Instale as dependências.

```bash
uv sync
```

Execute as migrações.

```bash
uv run alembic upgrade head
```

Inicie o backend.

```bash
uv run uvicorn backend.app.main:app --reload
```

---

# Roadmap

## Sprint 1

- Fundação do projeto

✅ Concluída

---

## Sprint 2

- Banco PostgreSQL
- Estrutura inicial

✅ Concluída

---

## Sprint 3

- ETL
- Arquitetura

✅ Concluída

---

## Sprint 4

- FastAPI
- Alembic
- Ambiente uv
- Organização do projeto

✅ Concluída

---

## Sprint 5

- Motor de Simulação
- Dashboards
- API de Simulação

🚧 Em planejamento

---

# Documentação

Toda a documentação encontra-se na pasta:

```text
docs/
```

Principais documentos:

- Vision
- Domain
- Architecture
- Database
- API
- Development
- Operations

---

# Licença

Este projeto está licenciado sob os termos da **GNU General Public License v3 (GPL-3.0)**.

---

# Autor

**Fernando Athaide Nóbrega Filho**

Analista de Sistemas

Secretaria de Promoções (SECPROM)

Força Aérea Brasileira (COMAER)

---

# Agradecimentos

Este projeto está sendo desenvolvido com o objetivo de modernizar os estudos estratégicos relacionados ao processo de promoções do COMAER, fornecendo uma plataforma analítica robusta, escalável e preparada para evolução contínua.
