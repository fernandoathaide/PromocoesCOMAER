CREATE TABLE config.vagas
(
    id              BIGSERIAL PRIMARY KEY,

    ano             INTEGER,

    posto_id        INTEGER,

    quadro_id       INTEGER,

    quantidade      INTEGER,

    tolerancia      NUMERIC(5,2),

    observacao      TEXT
);