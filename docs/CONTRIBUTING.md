# CONTRIBUTING.md

# Guia de Contribuição

**Projeto:** PromocoesCOMAER
**Versão:** 0.4.0
**Status:** Sprint 4 – Baseline

---

# Bem-vindo ao PromocoesCOMAER

Obrigado pelo interesse em contribuir com o **PromocoesCOMAER**.

Este projeto foi desenvolvido para apoiar os estudos estratégicos relacionados ao processo de promoções dos Oficiais-Generais da Força Aérea Brasileira (COMAER), utilizando conceitos de **Digital Twin**, **Análise de Dados**, **Simulação** e **Inteligência Artificial**.

Como se trata de um sistema de missão crítica, todas as contribuições devem seguir os padrões estabelecidos neste documento.

---

# Objetivo

Este guia define:

* Padrões de desenvolvimento
* Fluxo de contribuição
* Organização do código
* Convenções de commits
* Processo de revisão
* Controle de qualidade
* Documentação obrigatória

O objetivo é garantir que o projeto evolua de forma organizada, segura e padronizada.

---

# Filosofia do Projeto

O PromocoesCOMAER segue alguns princípios fundamentais:

* Arquitetura limpa (Clean Architecture)
* Código simples e legível
* Documentação antes da implementação
* Regras de negócio centralizadas
* Separação de responsabilidades
* Testes sempre que possível
* Evolução incremental por Sprint

---

# Tecnologias Utilizadas

## Backend

* Python 3.10+
* FastAPI
* SQLAlchemy
* Alembic
* Pydantic

## Banco de Dados

* PostgreSQL

## Frontend

* React
* TypeScript
* Vite
* Apache ECharts

## Infraestrutura

* Docker
* Docker Compose
* Debian Linux
* Nginx

## Desenvolvimento

* Git
* GitHub
* uv

---

# Estrutura do Projeto

```text
PromocoesCOMAER/

backend/
frontend/
database/
docs/
scripts/
tests/
docker/
ai/

README.md
pyproject.toml
uv.lock
```

Cada diretório possui uma responsabilidade específica e deve permanecer organizado.

---

# Fluxo de Desenvolvimento

Todo desenvolvimento deverá seguir o fluxo abaixo:

```text
Issue

↓

Branch

↓

Desenvolvimento

↓

Testes

↓

Atualização da documentação

↓

Commit

↓

Pull Request

↓

Code Review

↓

Merge
```

Nenhuma funcionalidade deve ser incorporada ao projeto sem passar por esse processo.

---

# Branches

Padrão adotado:

```text
main
```

Código estável.

```text
develop
```

Integração contínua.

Branches de trabalho:

```text
feature/nome-da-funcionalidade
```

```text
bugfix/nome-do-bug
```

```text
hotfix/nome-do-hotfix
```

```text
release/x.y.z
```

---

# Convenção de Commits

O projeto adota o padrão **Conventional Commits**.

Exemplos:

```text
feat(api): adiciona endpoint de militares
```

```text
fix(etl): corrige importação Oracle
```

```text
docs(readme): atualiza documentação
```

```text
refactor(core): reorganiza camada de serviços
```

```text
test(api): adiciona testes para promoções
```

```text
chore(deps): atualiza dependências
```

Tipos permitidos:

* feat
* fix
* docs
* style
* refactor
* perf
* test
* build
* ci
* chore

---

# Organização do Código

Cada módulo deverá possuir responsabilidade única.

Exemplo:

```text
API

↓

Service

↓

Repository

↓

Database
```

Não implementar regras de negócio diretamente:

* na API
* nos Repositories
* na Interface

Toda regra pertence à camada de **Services** ou ao **Rule Engine**.

---

# Padrões de Código

## Python

* Seguir PEP 8.
* Utilizar tipagem estática sempre que possível.
* Preferir funções pequenas.
* Evitar duplicação de código.
* Utilizar nomes descritivos.

---

## Banco de Dados

* Toda alteração deve ser feita por migrations.
* Nunca alterar tabelas diretamente em produção.
* Toda migration deve possuir rollback quando aplicável.
* Utilizar nomenclatura consistente para tabelas, índices e constraints.

---

## API

* Utilizar verbos HTTP corretamente.
* Documentar todos os endpoints.
* Validar entradas com Pydantic.
* Retornar códigos HTTP apropriados.
* Padronizar mensagens de erro.

---

## Frontend

* Componentes reutilizáveis.
* Separação entre apresentação e lógica.
* Tipagem com TypeScript.
* Organização por funcionalidades.

---

# Documentação Obrigatória

Toda funcionalidade nova deverá atualizar, quando aplicável:

* README.md
* CHANGELOG.md
* Documentação da API
* Documentação de Banco
* Diagramas de Arquitetura
* Documentação de Regras de Negócio

Uma funcionalidade não será considerada concluída sem documentação correspondente.

---

# Testes

Sempre que possível, incluir:

## Testes Unitários

* Services
* Rule Engine
* Utilitários

## Testes de Integração

* API
* Banco de Dados
* ETL

## Testes Funcionais

* Fluxos críticos
* Simulações
* Indicadores

---

# Pull Requests

Todo Pull Request deverá conter:

* Objetivo da alteração.
* Motivação.
* Descrição das mudanças.
* Impactos esperados.
* Evidências de testes.
* Atualização da documentação.
* Atualização do CHANGELOG.

---

# Code Review

Durante a revisão serão avaliados:

* Arquitetura
* Legibilidade
* Organização
* Performance
* Segurança
* Testabilidade
* Documentação
* Conformidade com os padrões do projeto

---

# Segurança

Nunca enviar ao repositório:

* Senhas
* Tokens
* Chaves privadas
* Credenciais Oracle
* Arquivos `.env`
* Dumps confidenciais
* Dados sensíveis

Utilize sempre o arquivo `.env.example` como referência.

---

# Dependências

Novas dependências devem:

* Possuir licença compatível.
* Estar ativamente mantidas.
* Ser justificadas.
* Ser adicionadas ao `pyproject.toml`.
* Ser sincronizadas com `uv`.

Evite adicionar bibliotecas sem necessidade.

---

# Boas Práticas

* Escreva código legível antes de código "inteligente".
* Prefira simplicidade.
* Evite duplicação.
* Mantenha funções pequenas.
* Documente decisões importantes.
* Utilize logs úteis.
* Preserve a rastreabilidade das alterações.

---

# O que evitar

* Código duplicado.
* Regras de negócio espalhadas.
* SQL embutido na API.
* Alterações diretas no banco.
* Commits genéricos como "ajustes" ou "correções".
* Misturar refatoração e novas funcionalidades no mesmo Pull Request.

---

# Roadmap de Contribuição

## Sprint 5

* CRUDs principais.
* Rule Engine inicial.
* Autenticação JWT.
* API funcional.
* Dashboards iniciais.

## Sprint 6

* Motor de Simulação.
* Indicadores avançados.
* Integração com IA.
* Auditoria.
* Testes automatizados.

---

# Licenciamento

Ao contribuir com este projeto, o autor concorda que suas contribuições serão disponibilizadas sob os termos da **GNU General Public License v3 (GPL-3.0)**.

---

# Contato

**Projeto:** PromocoesCOMAER

**Equipe:** Secretaria de Promoções (SECPROM)

**Organização:** Força Aérea Brasileira (COMAER)

---

# Histórico

| Versão    | Sprint       | Alteração                                                                            |
| --------- | ------------ | ------------------------------------------------------------------------------------ |
| 0.1.0     | Sprint 1     | Documento inicial                                                                    |
| 0.2.0     | Sprint 2     | Definição das convenções                                                             |
| 0.3.0     | Sprint 3     | Padronização do fluxo de desenvolvimento                                             |
| **0.4.0** | **Sprint 4** | Consolidação do processo de contribuição, Git Flow, padrões de código e documentação |

---

# Considerações Finais

O sucesso do PromocoesCOMAER depende da consistência de sua arquitetura, da qualidade do código e da clareza de sua documentação.

Toda contribuição deve preservar esses princípios, garantindo que o sistema continue evoluindo de forma segura, escalável e alinhada aos objetivos estratégicos da SECPROM.
