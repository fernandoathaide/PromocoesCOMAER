# Roadmap.md

# Roadmap do Projeto

**Projeto:** PromocoesCOMAER

**Versão:** 0.4.0

**Status:** Sprint 4 – Baseline

---

# Objetivo

Este documento apresenta o planejamento estratégico e técnico do desenvolvimento do **PromocoesCOMAER**, definindo as etapas de evolução da plataforma desde sua concepção até a primeira versão operacional.

O Roadmap serve como referência para acompanhamento da evolução do projeto, priorização das entregas e alinhamento entre arquitetura, regras de negócio e implementação.

---

# Visão Estratégica

O PromocoesCOMAER está sendo desenvolvido para tornar-se a principal plataforma de apoio à decisão da Secretaria de Promoções (SECPROM), funcionando como um **Digital Twin** do processo de promoções dos Oficiais-Generais do COMAER.

Ao final do projeto, a plataforma deverá ser capaz de:

* Simular promoções futuras.
* Projetar efetivos.
* Estimar passagens para a reserva.
* Avaliar impactos de alterações legais.
* Gerar indicadores estratégicos.
* Explicar cenários utilizando Inteligência Artificial.

---

# Objetivos Estratégicos

## Curto Prazo

* Estruturar a arquitetura.
* Consolidar o ambiente de desenvolvimento.
* Construir a base analítica.
* Automatizar o ETL.

---

## Médio Prazo

* Implementar o Motor de Simulação.
* Disponibilizar dashboards gerenciais.
* Criar APIs funcionais.
* Automatizar indicadores.

---

## Longo Prazo

* Integração com Inteligência Artificial.
* Modelos preditivos.
* Apoio completo à tomada de decisão.
* Plataforma institucional.

---

# Cronograma Geral

```text id="a8hktx"
Sprint 1
    │
Sprint 2
    │
Sprint 3
    │
Sprint 4
    │
Sprint 5
    │
Sprint 6
    │
Release 1.0
```

---

# Sprint 1 — Fundação do Projeto

## Objetivos

* Definição da visão do projeto.
* Levantamento das regras de negócio.
* Estudos sobre promoções.
* Definição do conceito de Digital Twin.
* Escolha das tecnologias.

## Entregas

* Visão do projeto.
* Documento de domínio.
* Arquitetura inicial.
* Organização do repositório.

**Status:** ✅ Concluída

---

# Sprint 2 — Infraestrutura

## Objetivos

* Configuração do PostgreSQL.
* Organização das migrations.
* Estrutura inicial do banco.
* Preparação do ambiente.

## Entregas

* PostgreSQL configurado.
* Alembic.
* Primeiras migrations.
* Estrutura dos schemas.

**Status:** ✅ Concluída

---

# Sprint 3 — Arquitetura

## Objetivos

* Estruturação do Backend.
* Organização do ETL.
* Arquitetura da API.
* Modelo de domínio.

## Entregas

* Estrutura FastAPI.
* Organização do projeto.
* Estrutura inicial do ETL.
* Documentação arquitetural.

**Status:** ✅ Concluída

---

# Sprint 4 — Consolidação da Base

## Objetivos

Consolidar toda a infraestrutura necessária para o desenvolvimento das funcionalidades de negócio.

## Entregas

### Arquitetura

* Arquitetura em camadas.
* Organização definitiva do projeto.

### Banco de Dados

* Schemas RAW.
* CORE.
* ANALYTICS.
* SIMULATION.
* CONFIG.
* AUDIT.

### Backend

* Estrutura FastAPI.
* SQLAlchemy.
* Alembic.
* Organização dos módulos.

### ETL

* Estrutura de extração.
* Pipeline Oracle → PostgreSQL.
* Snapshots da base Oracle.

### Ambiente

* uv
* pyproject.toml
* uv.lock

### Scripts

* install
* backup
* restore
* reset_database
* run_etl

### Documentação

* README
* Vision
* Domain
* API
* Authentication
* Database
* ETL
* Frontend
* Changelog
* Contributing

**Status:** ✅ Concluída

---

# Sprint 5 — Desenvolvimento Funcional

## Objetivos

Implementar as primeiras funcionalidades de negócio.

## Entregas Previstas

### Backend

* CRUD de Militares.
* CRUD de Promoções.
* CRUD de Quadros.
* CRUD de Vagas.

---

### Banco

* Modelo físico completo.
* Views.
* Procedures.
* Índices.

---

### API

* Endpoints funcionais.
* OpenAPI completa.
* Paginação.
* Filtros.

---

### Segurança

* JWT.
* OAuth2.
* Controle de permissões.

---

### Frontend

* Layout institucional.
* Dashboard inicial.
* Consulta de militares.
* Consulta de promoções.

---

### ETL

* Carga incremental.
* Agendamento.
* Logs.

**Status:** 🚧 Planejada

---

# Sprint 6 — Motor de Simulação

## Objetivos

Construir o núcleo analítico do sistema.

## Entregas Previstas

* Rule Engine.
* Simulation Engine.
* Forecast Engine.
* Vacancy Engine.
* Ranking Engine.
* Metrics Engine.

---

Também serão implementados:

* Simulações completas.
* Comparação de cenários.
* Indicadores.
* Dashboards analíticos.

**Status:** 📅 Planejada

---

# Sprint 7 — Inteligência Artificial

## Objetivos

Adicionar recursos inteligentes de apoio à decisão.

## Entregas

* Assistente IA.
* Explicação de cenários.
* Geração automática de relatórios.
* Perguntas em linguagem natural.
* Recomendações.

Modelos previstos:

* OpenAI GPT.
* Claude Sonnet.

**Status:** 📅 Planejada

---

# Sprint 8 — Consolidação

## Objetivos

Preparação para produção.

## Entregas

* Testes automatizados.
* Auditoria.
* Performance.
* Hardening.
* Monitoramento.
* Deploy.

**Status:** 📅 Planejada

---

# Release 1.0

Objetivos finais da primeira versão operacional.

## Plataforma

* Sistema operacional.
* API estável.
* Interface React.
* Motor de Simulação.
* Dashboards.

---

## Banco

* Modelo completo.
* ETL automatizado.
* Atualizações incrementais.

---

## Segurança

* JWT.
* Perfis.
* Auditoria.

---

## Inteligência Artificial

* Explicação de cenários.
* Relatórios.
* Indicadores.

---

## Documentação

* Arquitetura.
* API.
* Banco.
* Desenvolvimento.
* Operação.

---

# Evolução da Arquitetura

```text id="m0ofr5"
Sprint 1

Visão

↓

Sprint 2

Banco

↓

Sprint 3

API

↓

Sprint 4

Infraestrutura

↓

Sprint 5

CRUD

↓

Sprint 6

Simulação

↓

Sprint 7

IA

↓

Sprint 8

Produção
```

---

# Indicadores de Sucesso

Ao final da versão 1.0 espera-se:

* ETL totalmente automatizado.
* API documentada.
* Interface moderna.
* Simulações confiáveis.
* Indicadores estratégicos.
* Código testado.
* Arquitetura escalável.
* Documentação completa.

---

# Riscos do Projeto

## Técnicos

* Alterações na estrutura da base Oracle.
* Crescimento do volume de dados.
* Mudanças nas regras de promoção.
* Dependências externas.

---

## Organizacionais

* Mudanças de prioridade.
* Evolução normativa.
* Disponibilidade de equipe.

---

# Próximas Grandes Evoluções

Após a versão 1.0 estão previstas funcionalidades como:

* Machine Learning para previsões.
* Análise de tendências.
* Comparação entre exercícios.
* Simulações probabilísticas.
* Integração com outros sistemas do COMAER.
* Exportação para Power BI e Qlik Sense.
* Geração automática de pareceres técnicos.
* Painéis executivos para o Alto-Comando.

---

# Histórico

| Versão    | Situação                    |
| --------- | --------------------------- |
| 0.1.0     | Fundação do projeto         |
| 0.2.0     | Infraestrutura              |
| 0.3.0     | Arquitetura                 |
| **0.4.0** | Baseline Sprint 4           |
| 0.5.0     | Desenvolvimento Funcional   |
| 0.6.0     | Motor de Simulação          |
| 0.7.0     | Inteligência Artificial     |
| 0.8.0     | Consolidação                |
| **1.0.0** | Primeira versão operacional |

---

# Considerações Finais

O PromocoesCOMAER é um projeto de longo prazo que busca modernizar o processo de estudos de promoções da SECPROM por meio de uma arquitetura analítica moderna, modular e escalável.

Cada Sprint foi planejada para entregar valor incremental, reduzindo riscos e permitindo que a plataforma evolua de forma consistente até sua consolidação como ferramenta institucional de apoio à decisão.
