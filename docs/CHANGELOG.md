# CHANGELOG.md

# Changelog

Todas as alterações relevantes do projeto **PromocoesCOMAER** serão registradas neste documento.

Este projeto adota as recomendações do **Keep a Changelog** e segue o padrão de versionamento **Semantic Versioning (SemVer)**.

---

# Versionamento

Formato:

```text
MAJOR.MINOR.PATCH
```

Exemplo:

```text
1.0.0
│ │ └── Correções
│ └──── Novas funcionalidades
└────── Grandes mudanças
```

Enquanto o sistema estiver em desenvolvimento, as versões seguirão o padrão:

```text
0.x.y
```

---

# Situação Atual

| Projeto        | Valor                |
| -------------- | -------------------- |
| Nome           | PromocoesCOMAER      |
| Status         | Em Desenvolvimento   |
| Sprint Atual   | Sprint 4 (Concluída) |
| Próxima Sprint | Sprint 5             |
| Versão Atual   | **0.4.0**            |

---

# [0.4.0] - Sprint 4 - Baseline

## Data

Julho de 2026

---

## Objetivo da Sprint

Consolidar a infraestrutura do projeto, padronizar o ambiente de desenvolvimento e preparar a base tecnológica para o desenvolvimento das funcionalidades de negócio.

---

## Adicionado

### Arquitetura

* Definição da arquitetura em camadas.
* Consolidação do conceito de Digital Twin.
* Separação entre Backend, Banco de Dados, ETL e Frontend.
* Organização do repositório.

---

### Backend

* Estrutura inicial utilizando FastAPI.
* Organização dos módulos.
* Estrutura para Services.
* Estrutura para Repositories.
* Estrutura para Schemas.
* Estrutura para Models.

---

### Banco de Dados

* Configuração do PostgreSQL.
* Estrutura inicial dos schemas.

Criados:

* raw
* core
* analytics
* simulation
* config
* audit

---

### Alembic

* Configuração do Alembic.
* Primeiras migrations.
* Versionamento do banco.

---

### ETL

* Estrutura inicial do ETL.
* Organização para importação Oracle → PostgreSQL.
* Preparação para cargas incrementais.

---

### Ambiente de Desenvolvimento

* Padronização utilizando **uv**.
* Configuração do ambiente virtual.
* Organização do `pyproject.toml`.
* Geração do `uv.lock`.

---

### Scripts

Criados scripts para:

* instalação
* desenvolvimento
* produção
* backup
* restore
* reset do banco
* execução do ETL

---

### Oracle

* Primeiros snapshots da base Oracle.
* Organização da pasta de snapshots.
* Estrutura para futuras sincronizações.

---

### API

* Estrutura inicial da API.
* Organização das rotas.
* Planejamento da autenticação.
* Preparação para OpenAPI.

---

### Documentação

Criados ou revisados:

* README
* Vision
* Domain
* API
* Authentication
* Changelog
* Contributing

---

### Git

* Organização do repositório.
* Configuração inicial do GitHub.
* Padronização dos commits.

---

## Alterado

* Estrutura das pastas do projeto.
* Organização da documentação.
* Organização das migrations.
* Estrutura do backend.
* Fluxo de desenvolvimento.
* Processo de instalação.

---

## Corrigido

* Ajustes no ambiente local.
* Correções de configuração do PostgreSQL.
* Correções na criação do ambiente virtual.
* Ajustes de configuração do Alembic.
* Organização dos arquivos do projeto.

---

## Removido

* Estruturas experimentais utilizadas durante a fase inicial.
* Configurações antigas baseadas em `pip`.
* Scripts obsoletos.

---

# [0.3.0] - Sprint 3

## Principais entregas

* Estrutura inicial do ETL.
* Definição da arquitetura.
* Estudos do modelo de domínio.
* Organização da documentação.
* Definição da estratégia do Motor de Simulação.

---

# [0.2.0] - Sprint 2

## Principais entregas

* Criação do repositório.
* Estrutura inicial do PostgreSQL.
* Primeiras migrations.
* Definição das tecnologias.
* Organização inicial do projeto.

---

# [0.1.0] - Sprint 1

## Principais entregas

* Definição da visão do projeto.
* Estudos do processo de promoções.
* Levantamento das regras de negócio.
* Escolha da arquitetura.
* Definição do conceito de Digital Twin.

---

# Próximas Versões

## Sprint 5

Previsto:

* CRUD de Militares
* CRUD de Promoções
* CRUD de Vagas
* API funcional
* Rule Engine
* Primeira versão do Motor de Simulação
* Dashboard inicial
* Autenticação JWT
* Controle de perfis

---

## Sprint 6

Previsto:

* Dashboards avançados
* Indicadores estratégicos
* Integração inicial com IA
* Explicação de cenários
* Relatórios executivos
* Auditoria completa

---

## Versão 1.0

Objetivos:

* Plataforma operacional.
* Motor de Simulação completo.
* API estável.
* Dashboards gerenciais.
* Integração com IA.
* Documentação completa.
* Testes automatizados.
* Pipeline de Deploy.

---

# Convenções para Contribuição

Todas as alterações deverão ser registradas utilizando uma das categorias abaixo:

* Added
* Changed
* Deprecated
* Removed
* Fixed
* Security

Cada Sprint deverá gerar uma nova versão do Changelog, mantendo o histórico completo da evolução do projeto.

---

# Histórico de Versões

| Versão    | Sprint          | Status             |
| --------- | --------------- | ------------------ |
| 0.1.0     | Sprint 1        | Concluída          |
| 0.2.0     | Sprint 2        | Concluída          |
| 0.3.0     | Sprint 3        | Concluída          |
| **0.4.0** | **Sprint 4**    | **Baseline Atual** |
| 0.5.0     | Sprint 5        | Planejada          |
| 0.6.0     | Sprint 6        | Planejada          |
| 1.0.0     | Release Inicial | Planejada          |

---

# Observações

Este documento deverá ser atualizado ao final de cada Sprint, registrando todas as alterações relevantes da arquitetura, banco de dados, backend, frontend, infraestrutura, documentação e regras de negócio.

Nenhuma funcionalidade deverá ser considerada concluída sem que sua alteração correspondente esteja registrada neste Changelog.
