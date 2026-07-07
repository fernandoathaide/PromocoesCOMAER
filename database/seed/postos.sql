CREATE TABLE config.postos
(
    id          SERIAL PRIMARY KEY,

    codigo      VARCHAR(10),

    descricao   VARCHAR(100),

    estrelas    INTEGER,

    ordem       INTEGER
);