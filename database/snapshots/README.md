# Melhor forma de fazer

Eu evitaria exportar pelo DBeaver.
Prefira as ferramentas nativas do PostgreSQL:

## Backup em formato custom

##  No computador do trabalho:

pg_dump \
  -h localhost \
  -U postgres \
  -d promocoescomaer \
  -Fc \
  -t raw.t_pesfis_comgep_dw \
  -f t_pesfis_comgep_dw.dump

# Depois, no computador de casa:

pg_restore \
  -U postgres \
  -d promocoescomaer \
  t_pesfis_comgep_dw.dump

## Esse formato é mais rápido, compacto e preserva corretamente os tipos de dados.

# Se quiser trazer todo o ambiente

## Se além da t_pesfis_comgep_dw você tiver outras tabelas que representam a camada RAW, pode exportar o schema inteiro:

pg_dump \
  -h localhost \
  -U postgres \
  -d promocoescomaer \
  -Fc \
  -n raw \
  -f raw.dump

## No destino:

pg_restore \
  -U postgres \
  -d promocoescomaer \
  raw.dump