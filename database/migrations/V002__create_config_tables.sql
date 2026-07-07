CREATE TABLE config.business_rules
(
    id                  BIGSERIAL PRIMARY KEY,

    code                VARCHAR(20) UNIQUE NOT NULL,

    name                VARCHAR(200) NOT NULL,

    description         TEXT,

    category            VARCHAR(100),

    rule_type           VARCHAR(50),

    parameter           VARCHAR(100),

    parameter_value     VARCHAR(100),

    enabled             BOOLEAN DEFAULT TRUE,

    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP
);