# AI_RULES.md

> Master instructions for AI Assistants working on the PromocoesCOMAER project.

---

# Purpose

This document defines the mandatory rules that every AI assistant must follow when interacting with this repository.

These instructions apply to:

- GitHub Copilot
- Continue
- Cline
- ChatGPT
- Claude
- Gemini
- Any future AI coding assistant

If another document conflicts with this file, **AI_RULES.md always takes precedence.**

---

# Project Overview

PromocoesCOMAER is a Decision Support System (DSS) developed for the Brazilian Air Force (COMAER).

The application creates a **Digital Twin** of the military promotion process, allowing users to simulate future promotion scenarios based on historical and current personnel data.

The system is **not** responsible for deciding promotions.

Its purpose is to provide simulations, forecasts, statistics and analytical dashboards to support decision making.

---

# Main Technologies

Backend

- Python 3.13+
- FastAPI
- SQLAlchemy 2.x
- Alembic
- Pydantic v2

Database

- PostgreSQL

Data Integration

- Oracle Database
- ETL Processes

Frontend

- React
- TypeScript
- Vite

Visualization

- Apache ECharts

Testing

- Pytest
- HTTPX

Infrastructure

- Linux
- Git
- Docker (optional)

---

# Architecture Principles

Always follow the architecture documented in:

ai/architecture.md

Never invent a different architecture.

---

# Coding Principles

Always:

- Write clean code.
- Prefer readability over cleverness.
- Use explicit typing.
- Use descriptive variable names.
- Keep functions small.
- Prefer composition over inheritance.
- Avoid duplicated code.
- Keep business logic independent from framework code.

---

# Layer Responsibilities

Routes

- Receive HTTP requests
- Validate input
- Call Services
- Return responses

Services

- Business rules
- Simulations
- Calculations
- Validations

Repositories

- Database access only

Models

- SQLAlchemy ORM

Schemas

- Request/Response validation

Never mix responsibilities.

---

# Forbidden Practices

Never:

- Put business logic inside API routes.
- Execute raw SQL inside routes.
- Duplicate business rules.
- Hardcode configuration values.
- Hardcode credentials.
- Disable type checking.
- Ignore lint errors.
- Ignore test failures.
- Modify production database manually.

---

# Database Rules

PostgreSQL is the system of record.

Oracle is used only as the source system.

Never modify Oracle data.

ETL processes are responsible for synchronization.

---

# Business Rules

All promotion rules must remain centralized.

Business logic belongs inside:

backend/app/services/

Never duplicate promotion calculations.

Never create parallel implementations of the same rule.

---

# Error Handling

Always:

- Raise meaningful exceptions.
- Return proper HTTP status codes.
- Log unexpected failures.
- Avoid silent failures.

---

# Logging

Use structured logging.

Never use print() for production code.

---

# Configuration

Configuration must come from:

.env

or

Environment Variables

Never hardcode configuration.

---

# Security

Never expose:

- passwords
- tokens
- API keys
- connection strings

Always validate user input.

Always sanitize external data.

---

# Documentation

Every public module must contain documentation.

Complex functions require docstrings.

Business rules must be documented.

---

# Testing

Every new feature should include tests.

Every bug fix should include a regression test.

Never remove tests without justification.

---

# Performance

Prefer efficient queries.

Avoid N+1 queries.

Avoid loading unnecessary data.

Paginate large datasets.

---

# Code Style

Follow:

PEP8

Use Ruff.

Use Black-compatible formatting.

Use type hints everywhere.

---

# Git Rules

Small commits.

Clear commit messages.

One logical change per commit.

Never commit:

- secrets
- passwords
- .env
- generated files

---

# AI Assistant Behavior

Before writing code, read:

1. AI_RULES.md
2. ai/project.md
3. ai/architecture.md
4. Relevant technical documentation.

If unsure:

Stop.

Explain the uncertainty.

Ask for clarification.

Do not invent requirements.

---

# Decision Priority

When making decisions, follow this order:

1. AI_RULES.md
2. User instructions
3. Business rules
4. Architecture
5. Existing codebase
6. General best practices

---

# Project Philosophy

This project values:

- Correctness
- Maintainability
- Readability
- Security
- Reproducibility
- Performance
- Documentation
- Long-term evolution

Fast code is good.

Correct code is better.

Maintainable code is mandatory.

---

End of document.
