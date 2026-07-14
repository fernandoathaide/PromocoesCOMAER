# ETL.md

# Processo de ETL (Extract, Transform and Load)

**Projeto:** PromocoesCOMAER

**Versão:** 0.4.0

**Status:** Sprint 4 – Baseline

---

# Objetivo

Este documento descreve a arquitetura, os processos e as regras do **ETL (Extract, Transform and Load)** do PromocoesCOMAER.

O ETL é responsável por replicar, transformar e disponibilizar os dados provenientes do Oracle corporativo do COMAER em uma base PostgreSQL otimizada para análises, simulações e indicadores estratégicos.

Todo o processo foi projetado para preservar a integridade dos sistemas corporativos, garantindo que nenhuma operação realizada pelo PromocoesCOMAER altere a base oficial.

---

# Visão Geral

O ETL é um dos componentes centrais da arquitetura do sistema.

Ele realiza a sincronização periódica dos dados entre o Oracle e o PostgreSQL, alimentando as camadas analíticas utilizadas pelo Motor de Simulação e pela API.

Fluxo geral:

```text
Oracle SIG
      │
      ▼
Extração
      │
      ▼
Validação
      │
      ▼
RAW
      │
      ▼
Transformação
      │
      ▼
CORE
      │
      ▼
ANALYTICS
      │
      ▼
FastAPI
      │
      ▼
React / Dashboards
```

---

# Objetivos do ETL

* Replicar dados corporativos para ambiente analítico.
* Isolar o Oracle das consultas analíticas.
* Garantir consistência entre as bases.
* Preparar dados para o Motor de Simulação.
* Gerar indicadores de apoio à decisão.
* Permitir sincronizações periódicas.

---

# Arquitetura

```text
                Oracle SIG

                     │

             Python ETL Engine

                     │

          Leitura somente (Read Only)

                     │

                PostgreSQL

      RAW → CORE → ANALYTICS
```

O ETL é desenvolvido em **Python** e utiliza SQLAlchemy para acesso ao PostgreSQL e drivers Oracle apropriados para leitura da base corporativa.

---

# Princípios

O processo de ETL segue os seguintes princípios:

* Nunca escrever na base Oracle.
* Todas as operações Oracle são somente leitura.
* Manter rastreabilidade das cargas.
* Registrar logs completos.
* Permitir reprocessamento.
* Ser idempotente.
* Executar de forma transacional sempre que possível.

---

# Etapas do Processo

## 1. Extração (Extract)

Conecta-se ao Oracle corporativo e extrai os dados necessários.

Características:

* Conexão somente leitura.
* Consultas otimizadas.
* Paginação quando necessário.
* Controle de tempo de execução.

---

## 2. Validação

Antes da carga, os dados são validados.

Exemplos:

* Campos obrigatórios.
* Tipos de dados.
* Datas inválidas.
* Chaves duplicadas.
* Integridade referencial.

Registros inválidos serão registrados em log para análise posterior.

---

## 3. Carga RAW

Os dados são inseridos no schema **raw**, preservando ao máximo a estrutura original do Oracle.

Características:

* Sem regras de negócio.
* Sem enriquecimento.
* Estrutura semelhante à origem.
* Base para auditoria.

---

## 4. Transformação

Os dados da camada RAW são convertidos para o modelo de domínio do PromocoesCOMAER.

Nesta etapa ocorrem:

* Padronização de nomes.
* Conversão de tipos.
* Normalização.
* Tratamento de valores nulos.
* Consolidação de relacionamentos.
* Enriquecimento dos dados.

O resultado é gravado no schema **core**.

---

## 5. Consolidação Analítica

A camada **analytics** recebe dados preparados para:

* Dashboards.
* Indicadores.
* Consultas estatísticas.
* Relatórios.
* Motor de Simulação.

---

# Organização dos Schemas

## RAW

Replica da base Oracle.

Atualizada exclusivamente pelo ETL.

---

## CORE

Modelo de domínio consolidado.

Consumido pelos serviços da aplicação.

---

## ANALYTICS

Modelo otimizado para leitura.

Consumido por:

* API
* Dashboards
* Relatórios
* IA

---

# Fluxo Completo

```text
Oracle

↓

Consulta SQL

↓

Extração

↓

Validação

↓

RAW

↓

Transformação

↓

CORE

↓

Indicadores

↓

ANALYTICS

↓

FastAPI

↓

Frontend
```

---

# Tabelas Prioritárias

A carga inicial contempla principalmente informações relacionadas ao processo de promoções, tais como:

* Dados cadastrais dos militares.
* Histórico funcional.
* Promoções.
* Tempo de serviço.
* Quadros.
* Postos.
* Efetivos.
* Situação funcional.
* Dados auxiliares necessários às simulações.

Novas tabelas poderão ser incorporadas conforme evolução do projeto.

---

# Tipos de Carga

## Carga Inicial

Executada quando o ambiente é criado.

Características:

* Importação completa.
* Todas as tabelas.
* Maior tempo de execução.

---

## Carga Incremental

Executada periodicamente.

Atualiza apenas registros alterados desde a última sincronização.

Objetivos:

* Reduzir tempo.
* Minimizar carga sobre o Oracle.
* Atualizar apenas o necessário.

---

## Reprocessamento

Permite reconstruir completamente as camadas:

* RAW
* CORE
* ANALYTICS

Utilizado em:

* Correções.
* Mudanças de regras.
* Evolução do modelo.

---

# Controle das Execuções

Cada execução deverá registrar:

* Data e hora de início.
* Data e hora de término.
* Usuário responsável (quando aplicável).
* Quantidade de registros processados.
* Quantidade de erros.
* Tempo total.
* Status da execução.

Essas informações serão armazenadas no schema **audit**.

---

# Tratamento de Erros

O ETL deverá interromper imediatamente em caso de:

* Falha de conexão.
* Erro de leitura.
* Corrupção de dados.
* Falha crítica de integridade.

Erros não críticos deverão ser registrados em log para análise.

---

# Logs

Cada execução deverá produzir registros contendo:

* Início da carga.
* Consulta executada.
* Tempo por etapa.
* Quantidade de registros.
* Erros encontrados.
* Estatísticas de processamento.
* Encerramento da execução.

---

# Performance

Boas práticas adotadas:

* Processamento em lotes (batch).
* Paginação de consultas Oracle.
* Bulk Insert no PostgreSQL.
* Uso de transações.
* Índices apropriados.
* Paralelização quando viável.

---

# Segurança

O ETL utilizará:

* Usuário Oracle somente leitura.
* Credenciais protegidas por variáveis de ambiente.
* Comunicação segura.
* Controle de acesso ao PostgreSQL.

As credenciais nunca deverão ser armazenadas no código-fonte.

---

# Estrutura Prevista

```text
database/

etl/

    extract/

    transform/

    load/

    validators/

    mappings/

    jobs/

    logs/
```

---

# Variáveis de Ambiente

Exemplo:

```env
ORACLE_HOST=

ORACLE_PORT=

ORACLE_SERVICE=

ORACLE_USER=

ORACLE_PASSWORD=

POSTGRES_HOST=

POSTGRES_PORT=

POSTGRES_DATABASE=

POSTGRES_USER=

POSTGRES_PASSWORD=
```

---

# Execução

Execução manual:

```bash
./scripts/run_etl.sh
```

ou

```bash
uv run python backend/app/etl/main.py
```

---

# Futuras Evoluções

Na Sprint 5 estão previstos:

* ETL incremental.
* Processamento por lotes.
* Agendamento automático.
* Monitoramento.
* Notificações de falha.

Na Sprint 6:

* Paralelização.
* Otimizações de performance.
* Métricas de execução.
* Painel de monitoramento do ETL.

---

# Boas Práticas

* Nunca alterar dados na origem Oracle.
* Sempre validar os dados antes da transformação.
* Manter logs completos.
* Evitar consultas desnecessárias ao Oracle.
* Garantir idempotência das cargas.
* Documentar novas tabelas incorporadas.
* Testar cargas em ambiente de desenvolvimento antes da produção.

---

# Histórico

| Versão    | Sprint       | Alteração                                                                                                                                                  |
| --------- | ------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.1.0     | Sprint 1     | Definição da estratégia de ETL                                                                                                                             |
| 0.2.0     | Sprint 2     | Planejamento da sincronização Oracle → PostgreSQL                                                                                                          |
| 0.3.0     | Sprint 3     | Estrutura inicial do ETL em Python                                                                                                                         |
| **0.4.0** | **Sprint 4** | Consolidação da arquitetura do ETL, definição das camadas RAW, CORE e ANALYTICS, preparação para cargas incrementais e integração com o Motor de Simulação |
