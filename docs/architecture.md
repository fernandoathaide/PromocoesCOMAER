# Authentication.md

# Autenticação e Autorização

**Versão:** 0.4.0
**Status:** Sprint 4 – Concluída
**Projeto:** PromocoesCOMAER

---

# Objetivo

Este documento define a arquitetura de autenticação e autorização do **PromocoesCOMAER**, estabelecendo os mecanismos que garantirão acesso seguro às funcionalidades da plataforma.

Embora a autenticação ainda não esteja implementada na Sprint 4, sua arquitetura foi completamente planejada para suportar o crescimento do sistema e a integração com os serviços corporativos do COMAER.

---

# Visão Geral

O PromocoesCOMAER é uma plataforma de apoio à decisão que manipula informações estratégicas sobre efetivos, promoções, reservas e projeções.

Por esse motivo, todo acesso ao sistema deverá ser autenticado e autorizado conforme o perfil do usuário.

A arquitetura prevê:

* Autenticação segura
* Autorização baseada em papéis (RBAC)
* Tokens JWT
* OAuth2
* Registro de auditoria
* Expiração automática de sessões
* Registro de acessos

---

# Arquitetura

```text
                Usuário

                   │

              Login Seguro

                   │

             Authentication API

                   │

            Validação Usuário

                   │

          Geração do Token JWT

                   │

          Requisições Autenticadas

                   │

              FastAPI Services
```

---

# Princípios

O modelo de autenticação seguirá os princípios abaixo:

* Segurança por padrão (Secure by Default)
* Menor privilégio (Least Privilege)
* Sessões stateless
* Tokens assinados digitalmente
* Expiração automática
* Auditoria completa
* Separação entre autenticação e autorização

---

# Fluxo de Autenticação

```text
Usuário

↓

Login

↓

Validação das credenciais

↓

Geração do JWT

↓

Cliente recebe Token

↓

Requisições autenticadas

↓

Validação do Token

↓

Acesso autorizado
```

---

# Modelo de Autenticação

Na versão inicial será utilizado:

* OAuth2 Password Flow
* JWT (JSON Web Token)
* Bearer Token

Cabeçalho HTTP:

```http
Authorization: Bearer <token>
```

---

# Estrutura do Token

O JWT conterá informações mínimas necessárias para identificar o usuário.

Exemplo:

```json
{
    "sub": "12345",
    "nome": "João da Silva",
    "perfil": "ANALISTA",
    "exp": 1780000000
}
```

---

# Tempo de Expiração

Valores inicialmente previstos:

| Token         | Tempo      |
| ------------- | ---------- |
| Access Token  | 30 minutos |
| Refresh Token | 8 horas    |

Os tempos poderão ser ajustados por configuração.

---

# Perfis de Usuário

O sistema utilizará Controle de Acesso Baseado em Papéis (RBAC).

Perfis inicialmente previstos:

## Administrador

Possui acesso completo.

Permissões:

* Administração do sistema
* Configuração
* ETL
* Usuários
* Auditoria
* Simulações
* Dashboards

---

## Analista

Responsável pelos estudos técnicos.

Permissões:

* Consultas
* Simulações
* Indicadores
* Relatórios

Não poderá alterar configurações críticas.

---

## Gestor

Visualização gerencial.

Permissões:

* Dashboards
* Indicadores
* Relatórios
* Simulações autorizadas

---

## Consulta

Perfil somente leitura.

Permissões:

* Consultas
* Visualização de dashboards
* Indicadores públicos

---

# Matriz de Permissões

| Recurso                  | Admin | Analista | Gestor | Consulta |
| ------------------------ | :---: | :------: | :----: | :------: |
| Consultar militares      |   ✅   |     ✅    |    ✅   |     ✅    |
| Executar ETL             |   ✅   |     ❌    |    ❌   |     ❌    |
| Criar simulações         |   ✅   |     ✅    |    ❌   |     ❌    |
| Gerenciar usuários       |   ✅   |     ❌    |    ❌   |     ❌    |
| Alterar parâmetros       |   ✅   |     ❌    |    ❌   |     ❌    |
| Visualizar dashboards    |   ✅   |     ✅    |    ✅   |     ✅    |
| Configurações do sistema |   ✅   |     ❌    |    ❌   |     ❌    |

---

# Autorização

Toda rota protegida utilizará dependências do FastAPI para validação do token.

Exemplo conceitual:

```python
@router.get("/militares")
def listar_militares(
    usuario=Depends(get_current_user)
):
    ...
```

---

# Controle de Permissões

As permissões serão verificadas antes da execução de qualquer operação.

Fluxo:

```text
Requisição

↓

JWT

↓

Validação

↓

Perfil

↓

Permissões

↓

Execução
```

---

# Segurança das Senhas

As senhas nunca serão armazenadas em texto puro.

Será utilizado algoritmo de hash seguro, como:

* Argon2 (preferencial)
* bcrypt (compatível)

---

# Renovação de Sessão

Quando o Access Token expirar:

1. Cliente envia Refresh Token.
2. Token é validado.
3. Novo Access Token é emitido.
4. Sessão permanece ativa.

---

# Revogação de Tokens

O sistema permitirá revogar tokens em situações como:

* Logout
* Alteração de senha
* Bloqueio de usuário
* Revogação administrativa

---

# Auditoria

Eventos registrados:

* Login
* Logout
* Tentativas inválidas
* Expiração de sessão
* Alteração de permissões
* Alteração de senha
* Execução do ETL
* Execução de simulações
* Alterações administrativas

---

# Integração Futura

A arquitetura foi preparada para integração com:

* LDAP/Active Directory
* Single Sign-On (SSO)
* OpenID Connect
* Provedores OAuth2 corporativos

Essa integração será avaliada conforme as diretrizes de infraestrutura do COMAER.

---

# Proteção da API

A API deverá implementar:

* HTTPS obrigatório
* CORS configurado
* Rate Limiting
* Validação de origem
* Proteção contra ataques de força bruta
* Expiração automática de sessões

---

# Variáveis de Ambiente

Exemplo:

```env
SECRET_KEY=<chave-secreta>

ALGORITHM=HS256

ACCESS_TOKEN_EXPIRE_MINUTES=30

REFRESH_TOKEN_EXPIRE_MINUTES=480
```

---

# Estrutura Prevista

```text
backend/

app/

security/

    jwt.py

    auth.py

    permissions.py

    password.py

    oauth.py

    dependencies.py
```

---

# Fluxo Completo

```text
Usuário

↓

Login

↓

Authentication API

↓

JWT

↓

FastAPI

↓

Permission Service

↓

Business Service

↓

Repository

↓

PostgreSQL
```

---

# Boas Práticas

* Nunca armazenar senhas em texto puro.
* Utilizar HTTPS em todos os ambientes produtivos.
* Não registrar senhas ou tokens em logs.
* Aplicar o princípio do menor privilégio.
* Revogar sessões comprometidas imediatamente.
* Renovar chaves criptográficas periodicamente.
* Proteger todas as rotas sensíveis.

---

# Situação na Sprint 4

Até o encerramento da Sprint 4:

✅ Arquitetura de autenticação definida.

✅ Estrutura preparada para OAuth2.

✅ Estrutura preparada para JWT.

✅ Organização das futuras camadas de segurança.

🚧 Implementação será iniciada na Sprint 5.

---

# Roadmap

## Sprint 5

* Implementação do JWT
* OAuth2 Password Flow
* Login
* Logout
* Refresh Token
* Controle de perfis
* Dependências de autenticação
* Proteção dos endpoints

## Sprint 6

* Auditoria completa
* Integração com LDAP/SSO (quando aplicável)
* MFA (Autenticação Multifator) opcional
* Políticas avançadas de segurança

---

# Histórico

| Versão    | Sprint       | Alteração                                                                                                    |
| --------- | ------------ | ------------------------------------------------------------------------------------------------------------ |
| 0.1.0     | Sprint 1     | Documento inicial                                                                                            |
| 0.2.0     | Sprint 2     | Definição da estratégia de autenticação                                                                      |
| 0.3.0     | Sprint 3     | Planejamento do modelo RBAC                                                                                  |
| **0.4.0** | **Sprint 4** | Consolidação da arquitetura de autenticação, autorização e segurança para implementação nas próximas sprints |
