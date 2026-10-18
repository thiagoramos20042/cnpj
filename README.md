# Consulta CNPJ | Dados cadastrais em uma interface

Consulta de dados de CNPJ com visualização e exportação de informações em CSV.

**Automações** · Aplicação Streamlit

[← Data Science, IA e Automações · Thiago Oliveira](https://github.com/thiagoramos20042/thiagoramos20042) · [Catálogo de projetos](https://github.com/thiagoramos20042/thiagoramos20042/blob/main/PROJETOS.md)

## Objetivo

Facilitar a exploração de informações cadastrais retornadas por um serviço de consulta.

## O que você encontra

- Entrada do CNPJ em interface web.
- Consulta e organização da resposta do serviço.
- Conversão dos dados para download em CSV.

## Tecnologias

Python · Streamlit · requests · pandas · Pillow

## Arquivos principais

| Arquivo | Conteúdo |
| --- | --- |
| [teste.py](teste.py) | Aplicação de consulta e exportação. |
| [logo-data-marketplace-500x85-1.png](logo-data-marketplace-500x85-1.png) | Imagem usada pela aplicação. |
| [requirements.txt](requirements.txt) | Dependências do ambiente original. |

## Como explorar

Na raiz do repositório:

```bash
python -m pip install -r requirements.txt
python -m streamlit run teste.py
```

## Contexto do projeto

A entrada da aplicação é teste.py; main.py contém apenas o exemplo inicial do ambiente de desenvolvimento. As consultas dependem da resposta do serviço externo.

---

Integra o [portfólio de Thiago Oliveira](https://github.com/thiagoramos20042).
