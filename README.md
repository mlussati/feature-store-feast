# Feature Store feast

## O que é uma feature store
Suponha que tenhamos uma tarefa onde precisamos prever algo para uma entidade (ex. usuário) usando suas features.

* *Duplicação*: Crie um repositório central de features onde toda a equipe contribui com recursos mantidos, que qualquer pessoa pode usar em qualquer aplicação.
* *Desvio*: Crie features usando um pipeline unificado e armazene-as em um local central de onde os pipelines de treinamento e de serviço possam puxar.
* *Valores*: Recupere as features de entrada para os respectivos resultados puxando o que está disponível quando uma previsão for feita.

Quando você está construindo uma feature store, há vários componentes centrais que precisamos ter para enfrentar esses desafios:
- Ingestão de dados
- Definições de features
- Features históricas
- Features online

## Set up
```
# Create environment using conda:
conda create -n "feast-environment" python=3.11.5

# Activate Environment
conda activate feast-environment

# Install Feast
pip install feast==0.39
```

**Registro**: Informações sobre o nosso repositório de features, como fontes de dados, visualizações de features, etc.

**Store online**: banco de dados (SQLite para local) que armazena as features (mais recentes) para entidades definidas, a serem usadas para inferência online.

> Quando executamos o Feast localmente, o store offline é efetivamente representado por junções ponto no tempo do Pandas. Já em produção, o store offline pode ser algo mais robusto como o Google BigQuery, Amazon RedShift, etc.
