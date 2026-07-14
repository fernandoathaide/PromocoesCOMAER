# PromocoesCOMAER

Digital Twin do processo de promoções

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
