# Database.md

# Arquitetura do Banco de Dados

**Projeto:** PromocoesCOMAER

**Versão:** 0.4.0

**Status:** Sprint 4 – Baseline

---

# Objetivo

Este documento descreve a arquitetura do banco de dados do **PromocoesCOMAER**, incluindo sua organização lógica, estrutura física, padrões de modelagem, estratégia de versionamento e fluxo de processamento dos dados.

O banco de dados é o núcleo da plataforma analítica, responsável por armazenar dados provenientes dos sistemas corporativos do COMAER e disponibilizá-los para consultas, indicadores, simulações e análises estratégicas.

---

# Visão Geral

O PromocoesCOMAER utiliza o **PostgreSQL** como banco de dados principal.

O PostgreSQL foi escolhido por oferecer:

* Alto desempenho
* Robustez
* Confiabilidade
* Extensibilidade
* Excelente suporte a SQL
* Recursos analíticos avançados
* Compatibilidade com SQLAlchemy e Alembic

O banco analítico é totalmente independente do Oracle corporativo.

Nenhuma operação realizada pelo sistema modifica dados da base oficial.

---

# Arquitetura Geral

```text
                Oracle SIG

                     │

             Extração (ETL)

                     │

                     ▼

              PostgreSQL

      ┌──────────┬──────────┬──────────┐
      │          │          │
     RAW        CORE    ANALYTICS
      │          │          │
      └──────────┴──────────┘
                │
          Simulation Engine
                │
           Dashboards/API
```

---

# Objetivos da Arquitetura

* Separar dados operacionais dos analíticos.
* Preservar a integridade dos dados importados.
* Facilitar auditorias.
* Suportar simulações sem alterar dados reais.
* Permitir evolução independente do modelo analítico.

---

# Tecnologias

Banco de Dados:

* PostgreSQL 14+

ORM:

* SQLAlchemy 2.x

Versionamento:

* Alembic

Driver:

* psycopg

---

# Schemas do Banco

O banco está organizado em múltiplos schemas especializados.

---

## raw

Responsável por armazenar uma réplica dos dados extraídos do Oracle.

Características:

* Sem regras de negócio.
* Estrutura semelhante à origem.
* Atualização pelo ETL.
* Base para integração.

---

## core

Camada responsável pela padronização dos dados.

Nesta camada:

* dados são tratados;
* inconsistências são corrigidas;
* relacionamentos são consolidados;
* entidades de domínio são organizadas.

Toda a lógica de integração ocorre neste schema.

---

## analytics

Camada destinada à geração de consultas analíticas.

Contém:

* indicadores;
* visões materializadas;
* tabelas agregadas;
* estatísticas.

Esta camada é consumida pela API e pelos dashboards.

---

## simulation

Responsável pelos cenários simulados.

Armazena:

* parâmetros;
* cenários;
* resultados;
* projeções;
* probabilidades.

Nenhum dado deste schema interfere nos dados reais.

---

## config

Armazena parâmetros configuráveis do sistema.

Exemplos:

* limites;
* pesos;
* parâmetros do motor;
* configurações gerais.

---

## audit

Responsável pelo registro das operações críticas.

Exemplos:

* ETL
* Login
* Simulações
* Alterações administrativas
* Execução de processos

---

# Fluxo dos Dados

```text
Oracle

↓

Extração

↓

RAW

↓

Tratamentos

↓

CORE

↓

Indicadores

↓

ANALYTICS

↓

API

↓

Frontend
```

---

# Modelo de Camadas

## Camada RAW

Objetivo:

Armazenar uma cópia fiel da base Oracle.

Não são aplicadas regras de negócio.

Características:

* somente leitura;
* atualização via ETL;
* preservação da estrutura original.

---

## Camada CORE

Representa o domínio do sistema.

Nesta camada são aplicadas:

* normalização;
* enriquecimento;
* integração;
* padronização.

Todas as entidades de negócio serão consumidas a partir desta camada.

---

## Camada ANALYTICS

Otimizada para consultas.

Responsável por:

* dashboards;
* indicadores;
* gráficos;
* relatórios.

---

# Modelo Conceitual

Principais entidades:

```text
Militar

↓

Promoção

↓

Vaga

↓

Quadro

↓

Reserva

↓

Efetivo

↓

Indicadores

↓

Simulações
```

---

# Organização Física

```text
database/

migrations/

seed/

snapshots/

sql/

functions/

views/
```

---

# Migrations

Todas as alterações estruturais deverão ser realizadas utilizando Alembic.

Nunca modificar tabelas diretamente em produção.

Fluxo:

```text
Modelo

↓

Migration

↓

Revisão

↓

Execução

↓

Versionamento
```

Comando:

```bash
uv run alembic revision --autogenerate -m "descricao"
```

Aplicação:

```bash
uv run alembic upgrade head
```

Rollback:

```bash
uv run alembic downgrade -1
```

---

# ETL

O processo de ETL é responsável por:

* conectar ao Oracle;
* extrair dados;
* transformar registros;
* validar informações;
* carregar a camada RAW.

Posteriormente os dados são propagados para CORE e ANALYTICS.

---

# Integridade

Serão utilizados:

* Primary Keys
* Foreign Keys
* Unique Constraints
* Check Constraints
* Índices

Sempre que possível as regras de integridade deverão ser implementadas no banco.

---

# Índices

Prioridades:

* consultas por matrícula;
* posto;
* quadro;
* antiguidade;
* data de promoção;
* situação;
* ano.

Os índices deverão ser revisados periodicamente conforme o crescimento da base.

---

# Performance

Estratégias adotadas:

* índices apropriados;
* consultas otimizadas;
* views materializadas;
* particionamento (quando necessário);
* análise de planos de execução.

---

# Segurança

O PostgreSQL deverá utilizar perfis distintos.

Exemplo:

```text
Administrador

↓

Aplicação

↓

ETL

↓

Consulta
```

Cada perfil possuirá permissões específicas.

---

# Backup

O banco deverá possuir rotina automática de backup.

Tipos:

* Full
* Incremental (quando aplicável)
* Snapshot antes de grandes cargas

Ferramentas:

* pg_dump
* pg_restore

---

# Recuperação

Estratégia prevista:

* Backup diário.
* Snapshot antes de ETLs completos.
* Testes periódicos de restauração.

---

# Convenções

## Tabelas

* letras minúsculas;
* snake_case;
* nomes descritivos.

Exemplo:

```text
core.militar
```

---

## Colunas

Exemplo:

```text
id

nr_ordem

dt_promocao

sg_posto
```

---

## Chaves

Primary Key:

```text
pk_nome_tabela
```

Foreign Key:

```text
fk_tabela_origem_destino
```

Índice:

```text
idx_nome_coluna
```

---

# Evolução do Modelo

Sprint 1

* Estudos do domínio.

Sprint 2

* Definição do PostgreSQL.

Sprint 3

* Organização das migrations.
* Estrutura inicial do ETL.

Sprint 4

* Consolidação da arquitetura.
* Organização em schemas.
* Integração com FastAPI.
* Preparação para o Motor de Simulação.

Sprint 5

Previsto:

* Implementação das entidades principais.
* Views analíticas.
* Procedures de apoio.
* Otimização das consultas.

---

# Boas Práticas

* Nunca alterar dados da camada RAW manualmente.
* Toda alteração estrutural deve passar por migration.
* Utilizar transactions.
* Evitar SQL duplicado.
* Documentar novas tabelas.
* Nomear constraints de forma consistente.
* Revisar índices periodicamente.
* Separar dados operacionais dos analíticos.

---

# Próximos Passos

* Implementação completa do modelo físico.
* Construção das entidades CORE.
* Views analíticas.
* Materialized Views.
* Procedures do ETL.
* Procedures do Motor de Simulação.
* Otimização para grandes volumes.

---

# Histórico

| Versão    | Sprint       | Alteração                                                                                                                                                |
| --------- | ------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1.0     | Sprint 1     | Definição da estratégia de banco                                                                                                                         |
| 0.2.0     | Sprint 2     | Escolha do PostgreSQL e Alembic                                                                                                                          |
| 0.3.0     | Sprint 3     | Estrutura inicial do ETL e migrations                                                                                                                    |
| **0.4.0** | **Sprint 4** | Consolidação da arquitetura em camadas (RAW, CORE, ANALYTICS, SIMULATION, CONFIG e AUDIT), integração com FastAPI e preparação para o Motor de Simulação |
