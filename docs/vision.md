# VISION.md

# Visão do Projeto

**Projeto:** PromocoesCOMAER

**Versão:** 0.4.0

**Status:** Sprint 4 – Baseline

---

# 1. Introdução

O **PromocoesCOMAER** é uma plataforma de apoio à decisão desenvolvida para a **Secretaria de Promoções (SECPROM)** da Força Aérea Brasileira (COMAER).

O projeto nasceu da necessidade de modernizar os estudos relacionados ao processo de promoções dos Oficiais-Generais, substituindo análises manuais e planilhas por uma plataforma analítica moderna, segura e escalável.

Mais do que um sistema de consulta, o PromocoesCOMAER foi concebido como um **Digital Twin (Gêmeo Digital)** do processo de promoções, permitindo reproduzir virtualmente diferentes cenários antes da tomada de decisão.

---

# 2. Missão

Disponibilizar uma plataforma moderna de apoio à decisão capaz de transformar dados corporativos em conhecimento estratégico, permitindo análises, projeções e simulações confiáveis sobre promoções, efetivos e reservas dos Oficiais-Generais do COMAER.

---

# 3. Visão

Ser a principal plataforma institucional de análise estratégica do processo de promoções do COMAER, oferecendo recursos avançados de simulação, indicadores gerenciais e Inteligência Artificial para apoiar decisões baseadas em dados.

---

# 4. Valores

O desenvolvimento do PromocoesCOMAER é orientado pelos seguintes princípios:

* Confiabilidade.
* Transparência.
* Rastreabilidade.
* Segurança da informação.
* Simplicidade.
* Escalabilidade.
* Documentação contínua.
* Qualidade de software.
* Apoio à decisão baseado em evidências.

---

# 5. Problema

Atualmente, grande parte dos estudos relacionados às promoções militares depende da consolidação manual de informações provenientes de diferentes sistemas corporativos.

Esse processo apresenta limitações como:

* Alto consumo de tempo.
* Dependência de planilhas.
* Dificuldade para reproduzir cenários.
* Baixa rastreabilidade.
* Pouca automação.
* Limitações na geração de indicadores.

Além disso, os sistemas corporativos existentes possuem finalidade operacional e não foram concebidos para realizar análises prospectivas ou simulações estratégicas.

---

# 6. Solução Proposta

O PromocoesCOMAER propõe uma arquitetura analítica composta por:

* Base PostgreSQL independente.
* Processo automatizado de ETL.
* API REST.
* Interface Web moderna.
* Motor de Simulação.
* Rule Engine.
* Dashboards executivos.
* Integração futura com Inteligência Artificial.

Essa arquitetura permitirá estudar cenários complexos sem qualquer impacto sobre os sistemas oficiais.

---

# 7. Objetivos Estratégicos

## Curto Prazo

* Construir a infraestrutura do projeto.
* Implantar o banco PostgreSQL.
* Automatizar a importação dos dados Oracle.
* Disponibilizar APIs REST.

---

## Médio Prazo

* Implementar o Motor de Simulação.
* Disponibilizar dashboards gerenciais.
* Automatizar indicadores.
* Consolidar regras de negócio.

---

## Longo Prazo

* Inteligência Artificial.
* Modelos preditivos.
* Estudos probabilísticos.
* Apoio completo à tomada de decisão.

---

# 8. Público-Alvo

A plataforma destina-se principalmente a:

* Analistas da SECPROM.
* Gestores do COMAER.
* Administradores do sistema.
* Equipes de Tecnologia da Informação.
* Usuários autorizados.

---

# 9. Escopo

## Incluído

O sistema permitirá:

* Importar dados do Oracle.
* Manter uma base analítica própria.
* Consultar militares.
* Consultar promoções.
* Consultar vagas.
* Projetar efetivos.
* Simular promoções.
* Simular reservas.
* Gerar indicadores.
* Emitir relatórios.
* Apoiar decisões estratégicas.

---

## Fora do Escopo

O PromocoesCOMAER **não** realizará:

* Alterações na base Oracle.
* Processamento oficial das promoções.
* Publicação de atos administrativos.
* Alteração de dados corporativos.
* Substituição dos sistemas institucionais do COMAER.

Sua função é exclusivamente analítica e de apoio à decisão.

---

# 10. Objetivos Funcionais

A plataforma deverá permitir:

## Consultas

* Pesquisar militares.
* Consultar histórico funcional.
* Visualizar promoções.
* Consultar efetivos.
* Consultar vagas.

---

## Simulações

* Criar cenários.
* Alterar parâmetros.
* Simular alterações de vagas.
* Simular alterações legislativas.
* Projetar promoções futuras.
* Comparar cenários.

---

## Indicadores

* Efetivo atual.
* Promoções previstas.
* Reservas previstas.
* Tempo médio no posto.
* Distribuição por quadro.
* Evolução histórica.

---

# 11. Objetivos Não Funcionais

O sistema deverá apresentar:

* Alta disponibilidade.
* Arquitetura modular.
* Escalabilidade.
* Segurança.
* Desempenho.
* Facilidade de manutenção.
* Código testável.
* Documentação completa.

---

# 12. Arquitetura Conceitual

```text id="8wnv9d"
Oracle SIG

      │

      ▼

ETL Python

      │

      ▼

PostgreSQL

RAW

↓

CORE

↓

ANALYTICS

↓

Simulation Engine

↓

FastAPI

↓

React

↓

Usuário
```

---

# 13. Princípios Arquiteturais

O PromocoesCOMAER adota os seguintes princípios:

* Arquitetura em camadas.
* Separação entre dados operacionais e analíticos.
* APIs REST.
* Clean Architecture.
* Domain-Driven Design (DDD).
* Versionamento do banco via Alembic.
* Desenvolvimento orientado por documentação.
* Baixo acoplamento.
* Alta coesão.

---

# 14. Motor de Simulação

O Motor de Simulação constitui o principal diferencial do sistema.

Ele será responsável por:

* Aplicar regras de negócio.
* Simular promoções.
* Simular reservas.
* Projetar efetivos.
* Calcular probabilidades.
* Explicar resultados.

Todas as decisões serão fundamentadas em regras documentadas.

---

# 15. Inteligência Artificial

O projeto foi concebido para integração com modelos de IA.

Entre as funcionalidades previstas:

* Explicação de cenários.
* Perguntas em linguagem natural.
* Geração automática de relatórios.
* Interpretação de indicadores.
* Apoio técnico aos analistas.

A IA atuará como apoio à decisão, sem substituir a análise humana.

---

# 16. Situação Atual

Ao final da Sprint 4, o projeto possui:

## Arquitetura

* Estrutura consolidada.
* Organização em camadas.

---

## Banco de Dados

* PostgreSQL configurado.
* Schemas definidos.
* Alembic configurado.

---

## Backend

* FastAPI.
* SQLAlchemy.
* Estrutura modular.

---

## ETL

* Estrutura inicial.
* Processo Oracle → PostgreSQL.

---

## Ambiente

* Python.
* uv.
* Docker.
* GitHub.

---

## Documentação

Documentação técnica estruturada.

---

# 17. Roadmap

## Sprint 1

Fundação do projeto.

✅ Concluída

---

## Sprint 2

Infraestrutura.

✅ Concluída

---

## Sprint 3

Arquitetura.

✅ Concluída

---

## Sprint 4

Consolidação.

✅ Concluída

---

## Sprint 5

Primeiras funcionalidades.

🚧 Planejada

---

## Sprint 6

Motor de Simulação.

📅 Planejada

---

## Sprint 7

Inteligência Artificial.

📅 Planejada

---

## Sprint 8

Preparação para produção.

📅 Planejada

---

# 18. Indicadores de Sucesso

O projeto será considerado bem-sucedido quando:

* Os estudos deixarem de depender de planilhas.
* As simulações forem reproduzíveis.
* Os indicadores forem gerados automaticamente.
* O tempo de elaboração dos estudos for significativamente reduzido.
* As decisões puderem ser fundamentadas por evidências e regras documentadas.
* O sistema estiver preparado para evolução contínua.

---

# 19. Riscos

Principais riscos identificados:

* Alterações nas regras de promoção.
* Mudanças na estrutura do Oracle.
* Crescimento do volume de dados.
* Evolução das normas institucionais.
* Dependências de infraestrutura.

Todos os riscos deverão ser monitorados durante o ciclo de vida do projeto.

---

# 20. Considerações Finais

O PromocoesCOMAER representa uma evolução significativa na forma como os estudos de promoções poderão ser conduzidos no âmbito da SECPROM.

Ao combinar arquitetura moderna, banco de dados analítico, Motor de Simulação e Inteligência Artificial, a plataforma permitirá transformar grandes volumes de dados em informações estratégicas, contribuindo para decisões mais rápidas, fundamentadas e transparentes.

A arquitetura foi concebida para evoluir continuamente, acompanhando mudanças nas regras de negócio, na legislação e nas necessidades da Força Aérea Brasileira, preservando sempre os princípios de segurança, rastreabilidade e confiabilidade.
