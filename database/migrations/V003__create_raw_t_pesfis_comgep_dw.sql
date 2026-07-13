-- ============================================================
-- PromocoesCOMAER
-- Migration V003
-- Camada RAW
-- Espelho da SIG.T_PESFIS_COMGEP_DW
-- ============================================================

CREATE TABLE IF NOT EXISTS raw.t_pesfis_comgep_dw
(
    nr_ordem            VARCHAR(7) PRIMARY KEY,

    nr_antig            VARCHAR(8),

    nm_pessoa           VARCHAR(70),

    nm_guerra           VARCHAR(20),

    sg_posto            VARCHAR(2),

    sg_qdr              VARCHAR(10),

    sg_org              VARCHAR(20),

    dt_nasc             DATE,

    dt_praca            DATE,

    dt_promocao_atual   DATE,

    dt_conc_frm         DATE,

    dt_mov_atual        DATE,

    dt_apres_atual      DATE,

    dt_ult_apres        DATE,

    sg_sit_qdr          VARCHAR(20),

    nr_sit_qdr          VARCHAR(10),

    st_mov              VARCHAR(50),

    st_veterano         VARCHAR(1),

    st_especial         VARCHAR(1),

    vl_med_cfr          NUMERIC(7,4),

    tx_tempo_servico    VARCHAR(100),

    cd_posto            VARCHAR(2),

    cd_qdr              VARCHAR(3),

    created_at          TIMESTAMP NOT NULL
                        DEFAULT CURRENT_TIMESTAMP,

    updated_at          TIMESTAMP NOT NULL
                        DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_raw_nr_antig
    ON raw.t_pesfis_comgep_dw (nr_antig);

CREATE INDEX IF NOT EXISTS idx_raw_sg_posto
    ON raw.t_pesfis_comgep_dw (sg_posto);

CREATE INDEX IF NOT EXISTS idx_raw_sg_qdr
    ON raw.t_pesfis_comgep_dw (sg_qdr);

CREATE INDEX IF NOT EXISTS idx_raw_sg_org
    ON raw.t_pesfis_comgep_dw (sg_org);

CREATE INDEX IF NOT EXISTS idx_raw_cd_posto
    ON raw.t_pesfis_comgep_dw (cd_posto);

CREATE INDEX IF NOT EXISTS idx_raw_cd_qdr
    ON raw.t_pesfis_comgep_dw (cd_qdr);

CREATE INDEX IF NOT EXISTS idx_raw_dt_promocao
    ON raw.t_pesfis_comgep_dw (dt_promocao_atual);