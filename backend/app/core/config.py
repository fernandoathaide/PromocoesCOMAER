"""
Constantes globais da aplicação.

Este módulo NÃO lê o arquivo .env.
"""

from pathlib import Path

# ==========================================================
# Diretórios
# ==========================================================

BASE_DIR = Path(__file__).resolve().parents[3]

LOG_DIR = BASE_DIR / "logs"

MIGRATIONS_DIR = BASE_DIR / "database" / "migrations"

SEED_DIR = BASE_DIR / "database" / "seed"

# ==========================================================
# API
# ==========================================================

API_PREFIX = "/api/v1"

DEFAULT_LANGUAGE = "pt-BR"

DEFAULT_PAGE_SIZE = 50

# ==========================================================
# Schemas PostgreSQL
# ==========================================================

CONFIG_SCHEMA = "config"

RAW_SCHEMA = "raw"

ANALYTICS_SCHEMA = "analytics"

SIMULATION_SCHEMA = "simulation"

AUDIT_SCHEMA = "audit"
