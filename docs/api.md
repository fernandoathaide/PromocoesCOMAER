# API.md

# API do PromocoesCOMAER

**Versão:** 0.4.0
**Status:** Sprint 4 – Concluída
**Projeto:** PromocoesCOMAER

---

# Objetivo

Este documento descreve a arquitetura, os princípios, os padrões e os endpoints da API REST do **PromocoesCOMAER**.

A API é responsável por disponibilizar, de forma segura e padronizada, os serviços utilizados pela interface Web, pelo Motor de Simulação e pelas futuras integrações com Inteligência Artificial.

Todo o acesso aos dados do sistema deverá ocorrer exclusivamente através da API.

---

# Visão Geral

A API foi desenvolvida utilizando **FastAPI**, adotando arquitetura RESTful e documentação automática através do padrão **OpenAPI**.

Ela atua como camada de comunicação entre:

* Interface Web (React)
* Banco PostgreSQL
* Motor de Simulação
* Serviços de IA
* Sistemas externos (futuramente)

---

# Arquitetura

```text
                 React

                   │

            HTTP / HTTPS

                   │

              FastAPI API

        ┌──────────┼──────────┐
        │          │          │
        ▼          ▼          ▼

   PostgreSQL   Rule Engine   AI Services
```

---

# Princípios

A API segue os seguintes princípios:

* RESTful
* Stateless
* JSON como formato padrão
* Versionamento por URL
* Documentação OpenAPI
* Tipagem forte utilizando Pydantic
* Separação entre domínio e infraestrutura
* Código orientado por serviços
* Independência da interface gráfica

---

# Base URL

Durante o desenvolvimento:

```
http://localhost:8000
```

Produção:

```
https://promocoes.comaer.intraer
```

---

# Versionamento

Todas as APIs serão versionadas.

Exemplo:

```
/api/v1
```

Versões futuras:

```
/api/v2
/api/v3
```

---

# Documentação Automática

FastAPI disponibiliza automaticamente:

Swagger UI

```
/docs
```

ReDoc

```
/redoc
```

OpenAPI

```
/openapi.json
```

---

# Formato das Respostas

Todas as respostas utilizam JSON.

Exemplo

```json
{
  "success": true,
  "message": "Operação realizada com sucesso.",
  "data": {}
}
```

---

# Tratamento de Erros

Exemplo

```json
{
    "success": false,
    "error": "MILITAR_NAO_ENCONTRADO",
    "message": "O militar informado não foi localizado."
}
```

---

# Organização da API

```text
/api

    /v1

        /militares

        /promocoes

        /vagas

        /quadros

        /reservas

        /simulacoes

        /indicadores

        /usuarios

        /configuracoes

        /administracao
```

---

# Recursos da API

## Militares

Responsável pela consulta dos militares.

Exemplos

```
GET /api/v1/militares

GET /api/v1/militares/{id}

GET /api/v1/militares?posto=BR

GET /api/v1/militares?quadro=QOENG
```

---

## Promoções

Consulta das promoções.

```
GET /api/v1/promocoes

GET /api/v1/promocoes/{id}
```

---

## Quadros

```
GET /api/v1/quadros
```

---

## Vagas

```
GET /api/v1/vagas

GET /api/v1/vagas/{ano}
```

---

## Reserva

```
GET /api/v1/reservas
```

---

## Simulações

Principal módulo do sistema.

```
POST /api/v1/simulacoes

GET /api/v1/simulacoes

GET /api/v1/simulacoes/{id}
```

---

## Indicadores

```
GET /api/v1/indicadores
```

---

## Administração

```
GET /api/v1/admin

POST /api/v1/admin/importar

POST /api/v1/admin/etl
```

---

# Fluxo de Requisição

```text
Cliente

↓

FastAPI

↓

Service Layer

↓

Rule Engine

↓

Repository

↓

PostgreSQL

↓

Resposta JSON
```

---

# Organização do Backend

```text
backend/

app/

api/

core/

models/

schemas/

repositories/

services/

middlewares/

utils/

config/

main.py
```

Cada camada possui responsabilidade única.

---

# Padrão das Camadas

## API

Recebe requisições HTTP.

---

## Service

Implementa regras de negócio.

---

## Repository

Acessa o banco de dados.

---

## Database

Persistência dos dados.

---

# Segurança

A API será preparada para:

* HTTPS
* JWT
* OAuth2
* Controle de permissões
* CORS
* Rate Limiting
* Auditoria
* Logs de acesso

Na Sprint 4, a autenticação ainda não está implementada, mas a arquitetura já foi planejada para suportá-la.

---

# Integração com o Motor de Simulação

O Motor de Simulação consumirá serviços internos da API para:

* Criar cenários
* Executar simulações
* Comparar cenários
* Gerar indicadores
* Explicar resultados

---

# Integração com Inteligência Artificial

A arquitetura prevê integração futura com modelos de IA.

A IA poderá:

* Explicar cenários
* Gerar relatórios executivos
* Responder perguntas em linguagem natural
* Interpretar indicadores
* Justificar decisões tomadas pelo Motor de Simulação

---

# Convenções

## Verbos HTTP

| Método | Finalidade           |
| ------ | -------------------- |
| GET    | Consulta             |
| POST   | Criação              |
| PUT    | Atualização completa |
| PATCH  | Atualização parcial  |
| DELETE | Remoção              |

---

## Códigos HTTP

| Código | Significado         |
| ------ | ------------------- |
| 200    | OK                  |
| 201    | Criado              |
| 204    | Sem conteúdo        |
| 400    | Requisição inválida |
| 401    | Não autenticado     |
| 403    | Acesso negado       |
| 404    | Não encontrado      |
| 409    | Conflito            |
| 422    | Erro de validação   |
| 500    | Erro interno        |

---

# Boas Práticas

* Nunca acessar o banco diretamente pela interface.
* Toda regra de negócio deve estar na camada de serviços.
* Não retornar exceções internas ao cliente.
* Utilizar modelos Pydantic para validação.
* Versionar todas as APIs.
* Documentar automaticamente todas as rotas.
* Registrar logs de operações críticas.

---

# Próximos Passos (Sprint 5)

* Implementação dos primeiros endpoints funcionais.
* CRUD de militares.
* CRUD de promoções.
* CRUD de vagas.
* CRUD de parâmetros.
* API de simulação.
* Integração inicial com o Rule Engine.
* Implementação de autenticação JWT.
* Controle de perfis e permissões.
* Testes automatizados da API.
* Publicação da documentação OpenAPI completa.

---

# Histórico

| Versão    | Data         | Alteração                                                                                      |
| --------- | ------------ | ---------------------------------------------------------------------------------------------- |
| 0.1.0     | Sprint 1     | Documento inicial                                                                              |
| 0.2.0     | Sprint 2     | Definição da arquitetura                                                                       |
| 0.3.0     | Sprint 3     | Estrutura FastAPI                                                                              |
| **0.4.0** | **Sprint 4** | Consolidação da API, organização das rotas e preparação para autenticação e Motor de Simulação |
