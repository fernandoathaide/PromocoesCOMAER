# Coding Standards

## Purpose

This document defines the coding standards for the PromocoesCOMAER project.

All contributors and AI assistants must follow these conventions to ensure consistency, readability and maintainability.

---

# General Principles

Always write code that is:

- Readable
- Predictable
- Testable
- Maintainable
- Explicit
- Well documented

Avoid clever code.

Readable code is preferred over shorter code.

---

# Python Version

Python 3.13+

Always use modern Python features whenever appropriate.

---

# Formatting

Use Ruff for:

- formatting
- linting
- import ordering

Never manually format code differently.

The formatter is the source of truth.

---

# Naming Conventions

## Variables

Use descriptive names.

Good

```python
promotion_date

vacancy_count

eligible_officers
```

Bad

```python
x

tmp

data1
```

---

## Functions

Function names must use verbs.

Examples

```python
calculate_probability()

load_personnel()

synchronize_oracle()

create_simulation()
```

---

## Classes

Use PascalCase.

Example

```python
PromotionService

SimulationEngine

OracleRepository
```

---

## Constants

UPPER_CASE

```python
MAX_SIMULATION_YEARS

DEFAULT_BATCH_SIZE
```

---

## Files

snake_case.py

Good

```text
promotion_service.py

oracle_repository.py

simulation_engine.py
```

---

# Imports

Use absolute imports.

Group imports in this order:

Standard Library

Third Party

Local Modules

Example

```python
from datetime import datetime

from fastapi import APIRouter

from app.services.simulation import SimulationService
```

---

# Type Hints

Always use type hints.

Example

```python
def calculate_probability(
    officer_id: int,
    year: int,
) -> float:
```

Never omit return types.

---

# Docstrings

Public functions require docstrings.

Example

```python
def synchronize() -> None:
    """
    Synchronize Oracle data with PostgreSQL.
    """
```

Complex algorithms require detailed documentation.

---

# Comments

Comments should explain

WHY

not

WHAT

Avoid obvious comments.

Bad

```python
i += 1
# increment i
```

Good

```python
# Promotion cycles begin after the eligibility window.
```

---

# Function Size

Prefer functions smaller than 40 lines.

If larger,

consider refactoring.

---

# Class Size

Large classes indicate multiple responsibilities.

Prefer composition.

---

# Business Logic

Business rules belong only in

services/

Never place business logic inside:

routes

repositories

models

---

# API Layer

Routes should only:

- validate input
- call services
- return responses

Nothing more.

---

# Repository Layer

Repositories perform:

- queries
- inserts
- updates
- deletes

Nothing else.

---

# SQL

Prefer SQLAlchemy ORM.

Use raw SQL only when justified.

Always parameterize queries.

Never concatenate SQL strings.

---

# Exceptions

Raise meaningful exceptions.

Never swallow exceptions.

Never use

```python
except:
```

Always catch explicit exception types.

---

# Logging

Use structured logging.

Never use

print()

in production code.

---

# Configuration

Read configuration from

Settings

or

Environment Variables.

Never hardcode credentials.

---

# Testing

Every feature must include tests.

Prefer

pytest

Organize tests by feature.

---

# API Design

RESTful endpoints.

Plural resource names.

Examples

```
/officers

/promotions

/simulations
```

---

# Dependency Injection

Use FastAPI dependency injection.

Avoid global objects.

---

# Async Programming

Use async only when beneficial.

Do not create asynchronous code unnecessarily.

---

# Performance

Avoid

N+1 queries

Duplicate queries

Repeated calculations

---

# Security

Validate all external input.

Escape user data when necessary.

Never expose stack traces.

---

# Documentation

Every module should explain

Purpose

Responsibilities

Dependencies

Limitations

---

# TODOs

Avoid generic TODOs.

Good

```
TODO(#42):
Support incremental synchronization.
```

Bad

```
TODO
```

---

# Git

Small commits.

Meaningful commit messages.

One feature per commit.

---

# AI Assistant Rules

Before generating code:

Read

AI_RULES.md

architecture.md

Relevant domain documentation.

Do not invent architecture.

Do not duplicate business rules.

Ask when requirements are ambiguous.

---

# Code Review Checklist

Before finishing:

☐ Ruff passes

☐ Tests pass

☐ Type hints complete

☐ Documentation updated

☐ No duplicated code

☐ No business logic in routes

☐ No SQL in services

☐ Naming conventions respected

☐ Exceptions handled correctly

☐ Logging implemented

---

End of document.
