# DOMAIN.md

# Domínio do Sistema

Projeto: PromocoesCOMAER

Versão: 1.0

---

# Objetivo

O domínio do PromocoesCOMAER representa o processo de promoção dos Oficiais-Generais do COMAER.

O sistema não possui como foco principal armazenar militares.

O foco principal é representar todas as regras de promoção, vagas, movimentações, reserva e projeções temporais através de um Motor de Simulação.

---

# Princípios do Domínio

Todo cenário produzido pelo sistema deverá obedecer às regras vigentes.

As regras nunca ficarão espalhadas pelo código.

Toda regra deverá existir como uma Regra de Negócio documentada.

Cada regra possuirá:

- Identificador
- Nome
- Descrição
- Prioridade
- Tipo
- Implementação
- Status

Exemplo

RN001

Quantidade máxima de Oficiais Generais NUM

---

# Contextos do Domínio (Bounded Contexts)

O sistema será dividido em onze contextos.

## Militar

Representa cada Oficial.

Responsabilidades

- Dados pessoais
- Dados funcionais
- Histórico
- Antiguidade
- Promoções
- Tempo de posto
- Tempo de serviço

Não calcula promoções.

---

## Quadro

Representa o quadro do militar.

Exemplos

QOAV

QOENG

QOINT

QOMED

QOINF

---

## Posto

Representa os postos.

Cel

Br

MB

TB

Marechal

---

## Vagas

Representa as vagas oficiais.

Cada vaga possui

Posto

Quadro

Quantidade

Ano

Origem

Limite

Tolerância

---

## Promoção

Representa uma promoção possível.

Uma promoção possui

Militar

Posto Atual

Novo Posto

Data

Motivo

Origem da vaga

Probabilidade

Justificativa

Status

---

## Reserva

Representa a saída da ativa.

Tipos

Compulsória

Ex-Officio

Voluntária

Decorrente de promoção

---

## Efetivo

Representa o quantitativo atual.

Possui

Ano

Posto

Quadro

Quantidade NUM

Quantidade AGR

Quantidade Total

---

## Simulação

Representa um cenário.

Um cenário possui

Nome

Ano

Parâmetros

Resultados

Indicadores

---

## Indicadores

Representa todas as métricas.

Exemplos

Tempo médio no posto

Tempo médio para promoção

Quantidade de vagas

Efetivo

Reserva prevista

Renovação anual

---

## IA

Especialista no domínio.

Não altera dados.

Interpreta cenários.

Explica decisões.

Gera relatórios.

---

## Administração

Usuários

Permissões

ETL

Logs

Configuração

---

# Motor de Regras

Todo o domínio será controlado por um Rule Engine.

Nenhuma regra ficará implementada diretamente na interface.

---

# Regras de Negócio

RN001

Quantidade máxima de Oficiais Generais NUM

Valor

87

Valor recomendado

85

(Golden Rule)

Fonte

Documento Promoções

---

RN002

Militares AGR não ocupam vaga NUM.

---

RN003

Tempo máximo no posto TB

4 anos

Tempo máximo desde promoção a BR

12 anos

---

RN004

Tempo máximo MB dos quadros

QOINT

QOENG

QOMED

4 anos no posto

8 anos desde BR

---

RN005

Tempo máximo BR QOINF

4 anos

---

RN006

Distribuição anual das vagas.

Tolerância

20%

---

RN007

Mapa oficial de vagas

TB

MB

BR

Por quadro

---

RN008

Renovação anual

25%

---

RN009

Promoções por vaga

ou

Por decorrência

---

RN010

Promoção AGR obriga promoção NUM

---

RN011

Promoção de militar mais moderno

Obriga passagem para reserva dos mais antigos

---

RN012

Simulação baseada em Decreto

Permite redução de vagas

Respeitando tolerância

---

RN013

Simulação AGR

Promoção AGR

↓

Promoção NUM

↓

Reserva Ex-Officio

---

# Motor de Simulação

O Motor será composto por pequenos motores independentes.

Promotion Engine

Reserva Engine

Vacancy Engine

Forecast Engine

Probability Engine

Rule Engine

Ranking Engine

Metrics Engine

Scenario Engine

Todos independentes.

---

# Filosofia

O sistema nunca responderá apenas

"Pode promover."

Ele deverá responder

Pode promover.

Porque.

Qual regra permitiu.

Qual regra impediu.

Qual impacto ocorrerá.

Quem será afetado.

Qual cenário é mais eficiente.
