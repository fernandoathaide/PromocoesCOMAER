# Glossário do PromocoesCOMAER

## Objetivo

Este documento centraliza os termos, siglas e conceitos utilizados no projeto PromocoesCOMAER.

Todo desenvolvedor ou assistente de IA deve utilizar este documento como referência para compreender o domínio do negócio antes de implementar novas funcionalidades.

Quando um novo termo surgir durante o desenvolvimento, ele deverá ser adicionado a este glossário.

---

# COMAER

Comando da Aeronáutica.

Órgão responsável pela administração da Força Aérea Brasileira (FAB).

---

# FAB

Força Aérea Brasileira.

Instituição militar pertencente às Forças Armadas do Brasil.

---

# COMGEP

Comando-Geral do Pessoal.

Órgão responsável pela gestão do efetivo do COMAER.

---

# DGEP

Diretoria de Gestão de Pessoal.

Responsável pelos processos administrativos relacionados ao pessoal militar.

---

# SECPROM

Secretaria de Promoções.

Órgão responsável pela condução dos processos de promoção de militares.

Este sistema é desenvolvido para atender às necessidades analíticas da SECPROM.

---

# SISPROM

Sistema oficial utilizado para gerenciamento dos processos de promoção.

O PromocoesCOMAER **não substitui** o SISPROM.

Ele funciona como uma plataforma analítica complementar.

---

# SIG

Sistema Integrado de Gestão.

Banco de dados operacional utilizado como origem de informações.

---

# Oracle

Banco de dados operacional do COMAER.

No contexto deste projeto:

- Fonte oficial de dados.
- Apenas leitura.
- Nunca deve ser alterado pelo PromocoesCOMAER.

---

# PostgreSQL

Banco analítico do projeto.

Recebe os dados sincronizados do Oracle.

É utilizado pelas simulações e dashboards.

---

# ETL

Extract

Transform

Load

Processo responsável pela sincronização dos dados entre Oracle e PostgreSQL.

---

# Digital Twin

Representação digital do processo de promoções.

O objetivo é reproduzir o comportamento do sistema real permitindo testar cenários futuros.

O Digital Twin não altera dados oficiais.

---

# Simulação

Execução de um cenário hipotético utilizando os dados sincronizados.

Uma simulação nunca modifica os dados reais.

---

# Cenário

Conjunto de parâmetros utilizados em uma simulação.

Exemplos:

- aposentadorias
- novas vagas
- alterações de efetivo
- mudanças legislativas

---

# Efetivo

Quantidade de militares existente em determinado posto, quadro ou organização.

---

# Limite de Efetivo

Quantidade máxima autorizada para determinado posto ou quadro.

Os limites influenciam diretamente as promoções.

---

# Vaga

Posição disponível para promoção.

Pode ser criada por diversos eventos administrativos, como:

- promoção
- passagem para a reserva
- falecimento
- exclusão
- reorganização administrativa

---

# Cadeia de Promoções

Sequência de promoções desencadeada pela abertura de uma vaga.

Uma única vaga pode provocar diversas promoções em cascata.

---

# Efeito Cascata

Fenômeno em que uma promoção gera uma nova vaga, permitindo novas promoções sucessivas.

Este comportamento é um dos principais objetos de estudo do sistema.

---

# Promoção

Mudança de posto de um militar conforme legislação vigente e critérios estabelecidos pelo COMAER.

O sistema apenas simula esse processo.

---

# Antiguidade

Critério baseado na precedência cronológica do militar.

As regras específicas serão documentadas em business-rules.md.

---

# Merecimento

Critério baseado em avaliação funcional e demais requisitos definidos pela legislação.

As regras específicas serão documentadas em business-rules.md.

---

# Elegibilidade

Condição necessária para que um militar possa concorrer à promoção.

Os critérios dependem da legislação e das regras do COMAER.

---

# Probabilidade de Promoção

Indicador estatístico produzido pelo sistema.

Não representa decisão oficial.

Serve apenas como apoio analítico.

---

# Motor de Simulação

Conjunto de algoritmos responsáveis por executar os cenários simulados.

É o núcleo do Digital Twin.

---

# Dashboard

Interface gráfica utilizada para apresentação de indicadores, gráficos e resultados das simulações.

---

# Indicador

Métrica calculada pelo sistema.

Exemplos:

- militares elegíveis
- vagas disponíveis
- promoções previstas
- tempo médio para promoção

---

# API

Interface REST utilizada pelo frontend e por possíveis integrações futuras.

---

# Backend

Aplicação FastAPI responsável pela lógica do sistema.

---

# Frontend

Aplicação React responsável pela interface do usuário.

---

# Repositório

Camada responsável exclusivamente pelo acesso ao banco de dados.

Não implementa regras de negócio.

---

# Serviço (Service)

Camada responsável pelas regras de negócio.

Toda lógica de promoção deve permanecer nesta camada.

---

# Simulação Determinística

Simulação que produz exatamente o mesmo resultado quando executada com os mesmos parâmetros.

---

# Simulação Probabilística

Simulação que utiliza distribuições estatísticas para estimar cenários futuros.

Pode produzir resultados diferentes entre execuções.

---

# RAG

Retrieval-Augmented Generation.

Estratégia utilizada para fornecer contexto aos assistentes de IA através da documentação do projeto.

---

# IA

Assistente de Inteligência Artificial utilizado para auxiliar no desenvolvimento, documentação, revisão e implementação do sistema.

---

# Documento Vivo

Este glossário deverá ser atualizado continuamente.

Sempre que uma nova sigla, conceito ou termo de negócio surgir durante o desenvolvimento, ele deverá ser registrado aqui.

---

Fim do documento.
