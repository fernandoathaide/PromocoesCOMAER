-- ============================================================
-- PromocoesCOMAER
-- Migration V002
-- Tabelas de configuração
-- ============================================================

CREATE TABLE IF NOT EXISTS config.business_rules
(
    id                  BIGSERIAL PRIMARY KEY,

    code                VARCHAR(30) UNIQUE NOT NULL,

    name                VARCHAR(200) NOT NULL,

    description         TEXT,

    category            VARCHAR(100),

    rule_type           VARCHAR(50),

    parameter           VARCHAR(100),

    parameter_value     VARCHAR(255),

    enabled             BOOLEAN NOT NULL DEFAULT TRUE,

    created_at          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP
);