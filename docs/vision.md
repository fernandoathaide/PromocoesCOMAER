# PromocoesCOMAER

## Vision Document (VISION.md)

**Versão:** 1.0
**Status:** Em desenvolvimento
**Projeto:** PromocoesCOMAER
**Licença:** GNU General Public License v3.0

---

# Visão do Projeto

O **PromocoesCOMAER** é uma plataforma de apoio à decisão desenvolvida para atuar como um **Digital Twin (Gêmeo Digital)** do processo de promoções dos Oficiais-Generais da Força Aérea Brasileira (COMAER).

Seu objetivo é permitir que analistas e gestores realizem estudos, projeções, simulações e análises estratégicas sobre promoções, efetivos, vagas e passagens para a reserva, utilizando dados corporativos provenientes dos sistemas oficiais do COMAER.

O sistema não substituirá os sistemas corporativos existentes. Sua finalidade é fornecer um ambiente analítico seguro para apoiar estudos técnicos e decisões estratégicas.

---

# Missão

Desenvolver uma plataforma moderna de apoio à decisão capaz de reproduzir virtualmente o processo de promoções do COMAER, permitindo análises históricas, projeções de efetivo, simulações de cenários e geração de indicadores estratégicos baseados em dados oficiais.

---

# Visão de Futuro

Ser a principal plataforma de análise estratégica do processo de promoções do COMAER, oferecendo recursos avançados de simulação, inteligência analítica e apoio à decisão baseados em Inteligência Artificial.

---

# Objetivos Estratégicos

* Centralizar dados relevantes para análise de promoções.
* Construir uma base analítica independente do ambiente transacional Oracle.
* Possibilitar simulações de múltiplos cenários.
* Produzir indicadores gerenciais e estatísticos.
* Automatizar estudos atualmente realizados por planilhas.
* Disponibilizar painéis interativos.
* Explicar resultados utilizando Inteligência Artificial.
* Evoluir continuamente conforme novas regras de negócio forem surgindo.

---

# Escopo Inicial (MVP)

A primeira versão do sistema contemplará:

* Importação de dados do Oracle corporativo.
* Banco PostgreSQL para análise.
* ETL automatizado.
* Cadastro de parâmetros de simulação.
* Pesquisa de militares.
* Visualização individual do militar.
* Dashboard executivo.
* Simulações de promoções.
* Simulações de passagem para reserva.
* Indicadores estatísticos.
* Exportação de resultados.

---

# Escopo Funcional

O sistema deverá permitir:

## Consulta

* Pesquisar militares.
* Filtrar por posto, quadro, organização e situação.
* Visualizar histórico funcional.

## Simulação

* Alterar quantidade de vagas.
* Alterar parâmetros de promoção.
* Alterar regras de reserva.
* Simular múltiplos anos.
* Comparar cenários.

## Indicadores

* Efetivo atual.
* Efetivo projetado.
* Promoções previstas.
* Reservas previstas.
* Déficit ou excesso de vagas.
* Distribuição por posto.
* Evolução temporal.

---

# Público-Alvo

* Analistas da SECPROM.
* Gestores do COMAER.
* Administradores do sistema.
* Usuários autorizados.

---

# Postos contemplados

Inicialmente o sistema contemplará os seguintes postos:

* Coronel do Ar (Cel / CL-Ar)
* Brigadeiro do Ar (Br / Br-Ar)
* Major-Brigadeiro do Ar (Maj Brig / MB-Ar)
* Tenente-Brigadeiro do Ar (Ten Brig / TB-Ar)
* Marechal do Ar (quando aplicável)

A arquitetura permitirá expansão para outros postos futuramente.

---

# Princípios Arquiteturais

O PromocoesCOMAER será construído seguindo os seguintes princípios:

* Separação entre dados transacionais e analíticos.
* Arquitetura modular.
* Regras de negócio independentes da interface gráfica.
* APIs REST.
* Versionamento completo via Git.
* Desenvolvimento orientado por documentação.
* Código limpo e testável.
* Alta rastreabilidade.

---

# Arquitetura Geral

```text
Oracle (SIG)
        │
        ▼
 ETL Python
        │
        ▼
 PostgreSQL
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

# Motor de Simulação

O Motor de Simulação constitui o núcleo do sistema.

Será responsável por:

* Calcular probabilidades de promoção.
* Projetar efetivos.
* Simular reservas.
* Simular alterações de vagas.
* Simular alterações de legislação.
* Gerar rankings.
* Gerar indicadores.
* Produzir justificativas para cada resultado.

O Motor de Simulação será completamente independente da interface gráfica, permitindo reutilização por APIs, aplicações futuras e agentes de Inteligência Artificial.

---

# Inteligência Artificial

O sistema será preparado para integração com modelos de IA, como GPT-5.5 e Claude Sonnet.

A IA deverá ser capaz de:

* Responder perguntas em linguagem natural.
* Explicar resultados das simulações.
* Gerar relatórios executivos.
* Identificar tendências.
* Auxiliar analistas durante os estudos.

---

# O que o sistema NÃO fará

O PromocoesCOMAER não substituirá os sistemas corporativos do COMAER.

Também não realizará:

* Alterações na base Oracle.
* Processamento oficial de promoções.
* Publicação de atos administrativos.
* Atualização de dados corporativos.

Toda a análise será realizada sobre uma base analítica própria.

---

# Roadmap

## Fase 1

* Fundação do projeto
* Arquitetura
* Banco PostgreSQL
* ETL Oracle → PostgreSQL

## Fase 2

* API FastAPI
* Interface React
* Dashboards

## Fase 3

* Motor de Simulação
* Indicadores
* Relatórios

## Fase 4

* Inteligência Artificial
* Explicação de cenários
* Recomendações

## Fase 5

* Simulações avançadas
* Modelos preditivos
* Machine Learning

---

# Filosofia do Projeto

O PromocoesCOMAER não é apenas um sistema de consultas.

Seu propósito é transformar dados corporativos em conhecimento estratégico, oferecendo aos analistas ferramentas modernas para compreender o presente, projetar o futuro e avaliar o impacto de diferentes cenários antes da tomada de decisão.
