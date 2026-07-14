# Simulation.md

# Motor de Simulação

**Projeto:** PromocoesCOMAER

**Versão:** 0.4.0

**Status:** Sprint 4 – Baseline

---

# Objetivo

O Motor de Simulação é o componente central do **PromocoesCOMAER**.

Sua finalidade é reproduzir virtualmente o processo de promoções dos Oficiais-Generais do COMAER, permitindo a criação de cenários hipotéticos, projeções de efetivos e análises de impacto, sem interferir nos sistemas corporativos.

O objetivo não é apenas indicar **quem poderá ser promovido**, mas explicar **por que**, **quando**, **qual regra foi aplicada** e **quais serão os impactos da decisão**.

---

# Visão Geral

O Motor de Simulação foi concebido seguindo o conceito de **Digital Twin**, representando digitalmente o processo de promoções da Força Aérea Brasileira.

A partir dos dados armazenados no PostgreSQL, o motor executará simulações considerando:

* Efetivos
* Quadros
* Postos
* Vagas
* Antiguidade
* Tempo de posto
* Tempo de serviço
* Reservas
* Legislação vigente
* Regras de negócio

---

# Objetivos Estratégicos

O Motor deverá permitir:

* Simular promoções futuras.
* Projetar efetivos.
* Simular alterações de vagas.
* Simular alterações legislativas.
* Avaliar impactos organizacionais.
* Calcular probabilidades de promoção.
* Comparar diferentes cenários.
* Produzir justificativas técnicas para cada resultado.

---

# Arquitetura Geral

```text id="6v2h0n"
            PostgreSQL

                 │

        Dados Consolidados

                 │

         Rule Engine (Regras)

                 │

        Simulation Engine

                 │

       Cenários Simulados

                 │

        Indicadores

                 │

           FastAPI

                 │

        React / Dashboards
```

---

# Filosofia

O PromocoesCOMAER nunca responderá apenas:

> "O militar será promovido."

A resposta deverá incluir:

* Probabilidade da promoção.
* Fundamentação.
* Regras aplicadas.
* Regras impeditivas.
* Impactos produzidos.
* Consequências para o efetivo.
* Comparação com outros cenários.

---

# Componentes do Motor

O Motor será composto por módulos independentes.

---

## Rule Engine

Responsável por aplicar todas as regras de negócio.

Exemplos:

* Tempo mínimo no posto.
* Limite de vagas.
* Antiguidade.
* Promoções decorrentes.
* Reserva compulsória.
* Efetivo máximo.

Nenhuma regra ficará implementada diretamente na interface ou na API.

---

## Vacancy Engine

Calcula:

* vagas disponíveis;
* vagas futuras;
* vagas decorrentes;
* vagas excedentes.

---

## Promotion Engine

Responsável por:

* identificar militares elegíveis;
* ordenar candidatos;
* calcular prioridade;
* executar promoções simuladas.

---

## Reserve Engine

Calcula:

* reservas compulsórias;
* reservas voluntárias;
* reservas decorrentes de promoção.

---

## Forecast Engine

Projeta:

* efetivos futuros;
* promoções futuras;
* reservas futuras;
* ocupação de vagas.

---

## Probability Engine

Calcula a probabilidade de promoção considerando:

* histórico;
* regras;
* disponibilidade de vagas;
* cenários;
* tendências.

---

## Metrics Engine

Produz indicadores como:

* promoções previstas;
* tempo médio no posto;
* idade média;
* renovação anual;
* vagas ocupadas;
* efetivo por quadro.

---

## Scenario Engine

Gerencia os cenários simulados.

Cada cenário possuirá:

* Nome
* Descrição
* Data
* Autor
* Parâmetros
* Resultados
* Comparações

---

# Fluxo de Execução

```text id="v4cgdc"
Usuário

↓

Cria Cenário

↓

Define Parâmetros

↓

Rule Engine

↓

Simulation Engine

↓

Resultados

↓

Indicadores

↓

Dashboard
```

---

# Fluxo Interno

```text id="jdn4tu"
CORE

↓

Validação

↓

Rule Engine

↓

Simulation Engine

↓

Metrics Engine

↓

Analytics

↓

API
```

---

# Entrada da Simulação

Os parâmetros poderão incluir:

* Ano da simulação.
* Alteração de vagas.
* Inclusão ou exclusão de regras.
* Alteração de efetivos.
* Promoções extraordinárias.
* Alteração de limites legais.
* Cenários personalizados.

---

# Saída Esperada

O resultado da simulação deverá conter:

* Lista de promovidos.
* Lista de reservas.
* Vagas abertas.
* Vagas preenchidas.
* Efetivo final.
* Indicadores.
* Probabilidades.
* Justificativas.

---

# Modelo de Cenário

Cada cenário possuirá:

```text id="p58v0z"
ID

Nome

Descrição

Autor

Data

Parâmetros

Regras utilizadas

Resultado

Indicadores

Status
```

---

# Comparação de Cenários

O sistema permitirá comparar dois ou mais cenários.

Exemplo:

```text id="cxjlwm"
Cenário A

↓

Promoções

↓

Reservas

↓

Efetivo

↓

Indicadores

↓

Comparação

↓

Cenário B
```

---

# Explicabilidade

Toda decisão deverá ser explicável.

Exemplo:

```text id="fjlwmm"
Militar X

↓

Elegível

↓

RN003

↓

Vaga disponível

↓

Maior antiguidade

↓

Promoção Simulada
```

Nenhuma decisão deverá ser considerada "caixa-preta".

---

# Regras de Negócio

Todas as regras estarão centralizadas no Rule Engine.

Cada regra possuirá:

* Identificador
* Nome
* Descrição
* Categoria
* Prioridade
* Situação
* Fonte normativa

Exemplo:

| Código | Regra                              |
| ------ | ---------------------------------- |
| RN001  | Limite máximo de Oficiais-Generais |
| RN002  | Promoção decorrente                |
| RN003  | Tempo mínimo no posto              |
| RN004  | Reserva compulsória                |
| RN005  | Distribuição anual de vagas        |

---

# Persistência

Os resultados das simulações serão armazenados no schema:

```text id="jmsqnv"
simulation
```

Serão persistidos:

* Cenários.
* Parâmetros.
* Resultados.
* Logs.
* Comparações.

---

# Integração com a API

Principais endpoints previstos:

```text id="pmqvdt"
POST   /api/v1/simulacoes

GET    /api/v1/simulacoes

GET    /api/v1/simulacoes/{id}

DELETE /api/v1/simulacoes/{id}
```

---

# Integração com IA

O Motor de Simulação será preparado para integração com modelos de IA.

Exemplos de consultas:

> "Quais militares possuem maior probabilidade de promoção em 2028?"

> "Qual o impacto da redução de duas vagas de Major-Brigadeiro?"

> "Explique por que o Coronel João não foi promovido."

A IA responderá utilizando os resultados produzidos pelo Rule Engine e pelo Simulation Engine.

---

# Performance

Estratégias previstas:

* Processamento em memória.
* Cache de regras.
* Cache de indicadores.
* Execução paralela de cenários.
* Reutilização de cálculos.

---

# Auditoria

Cada simulação registrará:

* Usuário.
* Data.
* Hora.
* Parâmetros.
* Tempo de execução.
* Resultado.
* Regras aplicadas.

---

# Estrutura Prevista

```text id="74p7w7"
backend/

app/

simulation/

    engines/

    rules/

    scenarios/

    calculators/

    validators/

    metrics/

    repositories/
```

---

# Roadmap

## Sprint 5

* Estrutura inicial do Rule Engine.
* CRUD de cenários.
* Primeiros cálculos de elegibilidade.

---

## Sprint 6

* Promotion Engine.
* Reserve Engine.
* Vacancy Engine.
* Metrics Engine.
* Comparação de cenários.

---

## Sprint 7

* Probability Engine.
* IA explicativa.
* Relatórios automáticos.
* Dashboards analíticos.

---

# Boas Práticas

* Nunca alterar dados reais.
* Toda simulação deve ser reproduzível.
* Toda decisão deve ser explicável.
* Todas as regras devem ser documentadas.
* Separar regras do código de infraestrutura.
* Permitir comparação entre versões das regras.

---

# Histórico

| Versão    | Sprint       | Alteração                                                                                                                         |
| --------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| 0.1.0     | Sprint 1     | Conceito do Digital Twin                                                                                                          |
| 0.2.0     | Sprint 2     | Definição do Motor de Simulação                                                                                                   |
| 0.3.0     | Sprint 3     | Arquitetura modular dos Engines                                                                                                   |
| **0.4.0** | **Sprint 4** | Consolidação da arquitetura do Rule Engine, Simulation Engine, Metrics Engine e integração planejada com FastAPI, PostgreSQL e IA |

---

# Considerações Finais

O Motor de Simulação representa o principal diferencial do PromocoesCOMAER.

Ele transforma uma plataforma de consulta em um verdadeiro sistema de apoio à decisão, capaz de reproduzir virtualmente o comportamento do processo de promoções do COMAER, permitindo estudos estratégicos fundamentados, auditáveis e explicáveis.

A partir da Sprint 5, o desenvolvimento do projeto será concentrado neste componente, que constituirá o núcleo funcional da aplicação.
