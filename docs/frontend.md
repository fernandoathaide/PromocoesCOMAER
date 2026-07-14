# Frontend.md

# Arquitetura do Frontend

**Projeto:** PromocoesCOMAER

**Versão:** 0.4.0

**Status:** Sprint 4 – Baseline

---

# Objetivo

Este documento descreve a arquitetura, organização, tecnologias e padrões de desenvolvimento do Frontend do **PromocoesCOMAER**.

O Frontend é responsável por fornecer uma interface moderna, intuitiva e responsiva para que analistas da SECPROM possam consultar dados, executar simulações, visualizar indicadores estratégicos e analisar cenários de promoção dos Oficiais-Generais do COMAER.

---

# Visão Geral

O Frontend foi concebido como uma **Single Page Application (SPA)** utilizando **React**, **TypeScript** e **Vite**, consumindo exclusivamente os serviços disponibilizados pela API REST do sistema.

Toda a lógica de negócio permanece no Backend (FastAPI), mantendo o Frontend responsável apenas pela apresentação dos dados e interação com o usuário.

---

# Objetivos

O Frontend deverá:

* Disponibilizar uma interface moderna.
* Facilitar a análise estratégica.
* Apresentar dashboards interativos.
* Executar simulações.
* Consumir exclusivamente a API REST.
* Ser modular e reutilizável.
* Suportar futuras integrações com IA.

---

# Arquitetura Geral

```text id="4wmtc8"
             Usuário

                │

          React + Vite

                │

         Componentes React

                │

        Serviços (API Client)

                │

        FastAPI REST API

                │

           PostgreSQL
```

---

# Tecnologias

## Framework

* React 19+
* TypeScript
* Vite

---

## Componentes

* React Router
* Axios
* Apache ECharts

---

## Qualidade

* ESLint
* Prettier

---

## Futuras Bibliotecas

Previstas para as próximas Sprints:

* TanStack Query
* React Hook Form
* Zod
* Zustand (ou Context API)
* Day.js

---

# Estrutura do Projeto

```text id="5pqjlwm"
frontend/

src/

assets/

components/

layouts/

pages/

services/

hooks/

contexts/

routes/

types/

utils/

styles/

App.tsx

main.tsx
```

Cada diretório possui uma responsabilidade específica.

---

# Organização das Camadas

```text id="mbwqmw"
Pages

↓

Components

↓

Hooks

↓

Services

↓

API
```

---

# Layout da Aplicação

O sistema utilizará um layout administrativo composto por:

* Menu lateral.
* Barra superior.
* Área principal.
* Breadcrumb.
* Rodapé.

```text id="7xms4v"
+--------------------------------------+

 Header

+---------+----------------------------+

 Menu     Conteúdo

 Lateral

+---------+----------------------------+

 Footer
```

---

# Páginas Previstas

## Dashboard

Resumo executivo contendo:

* Efetivo atual.
* Promoções previstas.
* Reservas.
* Indicadores.
* Alertas.

---

## Militares

Consulta completa dos militares.

Filtros:

* Posto
* Quadro
* Organização
* Situação
* Nome

---

## Promoções

Consulta das promoções.

Visualização:

* Histórico.
* Próximas promoções.
* Elegibilidade.

---

## Vagas

Consulta de vagas existentes.

Permite visualizar:

* Quantidade.
* Distribuição.
* Evolução temporal.

---

## Simulações

Principal módulo do sistema.

Permitirá:

* Criar cenários.
* Alterar parâmetros.
* Executar simulações.
* Comparar resultados.

---

## Indicadores

Apresentará:

* Gráficos.
* Estatísticas.
* Evolução anual.
* Tendências.

---

## Administração

Permissões:

* Usuários.
* Configurações.
* ETL.
* Logs.
* Auditoria.

---

# Navegação

Estrutura inicial:

```text id="hjp5fu"
/dashboard

/militares

/promocoes

/vagas

/simulacoes

/indicadores

/relatorios

/configuracoes

/admin
```

---

# Comunicação com Backend

Toda comunicação ocorrerá através da API REST.

Fluxo:

```text id="e0smyl"
React

↓

Axios

↓

FastAPI

↓

Services

↓

Repository

↓

PostgreSQL
```

---

# Dashboards

Os dashboards utilizarão **Apache ECharts**.

Gráficos previstos:

* Barras
* Linhas
* Pizza
* Área
* Heatmap
* Sankey
* Timeline

---

# Indicadores

Exemplos:

* Efetivo por posto.
* Promoções anuais.
* Reservas previstas.
* Tempo médio no posto.
* Evolução histórica.
* Distribuição por quadro.
* Ocupação de vagas.

---

# Simulações

O Frontend permitirá criar cenários como:

* Alteração do número de vagas.
* Mudança de parâmetros.
* Alteração de regras.
* Comparação entre cenários.

Toda execução ocorrerá através da API.

---

# Integração com IA

Está prevista uma interface para interação em linguagem natural.

Exemplos:

```text id="drrn3t"
"Quais oficiais possuem maior probabilidade de promoção?"

"Qual o impacto da redução de vagas?"

"Explique por que determinado militar não foi promovido."
```

As respostas serão geradas pelo Backend utilizando modelos de IA.

---

# Organização dos Componentes

Exemplo:

```text id="j84w4r"
components/

Button/

Card/

DataTable/

SearchBox/

Modal/

Chart/

Sidebar/

Header/

Footer/
```

Todos os componentes deverão ser reutilizáveis.

---

# Estado da Aplicação

Na Sprint 4 será utilizada uma abordagem simples.

Evolução prevista:

Sprint 5:

* Context API

Sprint 6:

* Zustand ou TanStack Query

Conforme a complexidade do sistema aumentar.

---

# Padrões de Desenvolvimento

* Componentes pequenos.
* Responsabilidade única.
* Tipagem obrigatória.
* Reutilização máxima.
* Separação entre UI e lógica.
* Nenhuma regra de negócio no Frontend.

---

# Responsividade

O sistema deverá funcionar em:

* Desktop
* Notebook
* Tablet

O foco principal do projeto é o uso em ambiente corporativo, portanto a experiência em desktop será priorizada.

---

# Tema Visual

Padrões sugeridos:

* Interface limpa.
* Alto contraste.
* Ícones intuitivos.
* Poucas cores.
* Layout institucional.

O tema deverá seguir identidade visual compatível com aplicações corporativas.

---

# Segurança

O Frontend deverá:

* Armazenar apenas o JWT.
* Nunca armazenar senhas.
* Validar permissões.
* Tratar erros da API.
* Encerrar sessão automaticamente quando necessário.

---

# Estrutura de Rotas

```text id="olh8kl"
/

dashboard

militares

promocoes

vagas

simulacoes

indicadores

configuracoes

admin
```

---

# Fluxo Geral

```text id="pdv1pp"
Usuário

↓

React

↓

Axios

↓

FastAPI

↓

PostgreSQL

↓

Resposta

↓

Interface
```

---

# Roadmap

## Sprint 5

* Estrutura inicial React.
* Layout principal.
* Sistema de rotas.
* Login.
* Dashboard inicial.
* Consulta de militares.

---

## Sprint 6

* Simulações.
* Indicadores.
* Relatórios.
* Dashboards completos.
* Integração inicial com IA.

---

# Boas Práticas

* Componentes reutilizáveis.
* Evitar lógica de negócio na interface.
* Tipagem completa.
* Comunicação exclusivamente via API.
* Código organizado por funcionalidades.
* Interfaces consistentes.
* Utilizar loading e tratamento de erros em todas as chamadas.

---

# Histórico

| Versão    | Sprint       | Alteração                                                                                                                       |
| --------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| 0.1.0     | Sprint 1     | Definição da estratégia de Frontend                                                                                             |
| 0.2.0     | Sprint 2     | Escolha de React e Vite                                                                                                         |
| 0.3.0     | Sprint 3     | Definição da arquitetura SPA                                                                                                    |
| **0.4.0** | **Sprint 4** | Consolidação da arquitetura do Frontend, definição da estrutura de componentes, páginas, dashboards e integração com a API REST |
