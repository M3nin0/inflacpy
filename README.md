# Inflacpy

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f2be9f8d8d544d46a17f7ce6910218a0)](https://www.codacy.com/app/M3nin0/inflacpy?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=M3nin0/inflacpy&amp;utm_campaign=Badge_Grade)
[![License](https://img.shields.io/badge/License-BSD%202--Clause-orange.svg)](https://opensource.org/licenses/BSD-2-Clause)
[![Build Status](https://travis-ci.org/M3nin0/inflacpy.svg?branch=master)](https://travis-ci.org/M3nin0/inflacpy)

Este é um pequeno pacote para a fácil aquisição de informações sobre inflação em diversos países. A ideia é que a informação fique disponível de forma mais rápida para análises e consultas.

Todos os dados são retirados do site: [Inflation](http://pt.inflation.eu/). Estou utilizando este site pois ele faz uma excelente junção dos mais diversos serviços. Créditos pelos dados a eles.

## Utilização

A utilização é bastante simples, há um exemplo dentro de <code>app.py</code>, porém caso você queira utilizar em seu projeto, basta importar a classe <code>Scrap</code> e utilizar o método <code>get_data</code>, com ele será possível definir o país e o tempo que deverá ser considerado na busca.

A instalação das dependências deverá ser feita:

```shell
pip install requirements.txt
```

O método retorna um dicionário com as informações

```python
  scrap = Scrap()
  _list = scrap.get_data(country='brasil')
```

### Salvando os dados

Caso você queira salvar em algum formato, recomenda-se a utilização do <code>Pandas</code> ele facilita o processo. Veja o exemplo para a realização da exportação dos dados em json.

```python
  _json = pd.DataFrame(_list).dropna()
  _json.to_json('brasil.json')
```

## Países disponíveis para consulta

Abaixo uma lista dos países disponíveis e o último ano disponível para análise.

|         País             | Até  |
|--------------------------|------|
| Inflação África do Sul   | 2019 |
| Inflação Alemanha        | 2019 |
| Inflação Austria         | 2019 |
| Inflação Bélgica         | 2019 |
| Inflação Brasil          | 2019 |
| Inflação Canadá          | 2019 |
| Inflação Chéquia         | 2019 |
| Inflação Chile           | 2019 |
| Inflação China           | 2019 |
| Inflação Coreia do Sul   | 2019 |
| Inflação Dinamarca       | 2019 |
| Inflação Eslováquia      | 2019 |
| Inflação Eslovénia       | 2019 |
| Inflação Espanha         | 2019 |
| Inflação Estados Unidos  | 2019 |
| Inflação Estónia         | 2019 |
| Inflação Finlândia       | 2019 |
| Inflação França          | 2019 |
| Inflação Grã-Bretanha    | 2019 |
| Inflação Grécia          | 2019 |
| Inflação Holanda         | 2019 |
| Inflação Hungria         | 2019 |
| Inflação India           | 2019 |
| Inflação Indonésia       | 2019 |
| Inflação Irlanda         | 2019 |
| Inflação Islândia        | 2019 |
| Inflação Israel          | 2019 |
| Inflação Itália          | 2019 |
| Inflação Japão           | 2019 |
| Inflação Luxemburgo      | 2019 |
| Inflação México          | 2019 |
| Inflação Noruega         | 2019 |
| Inflação Polónia         | 2019 |
| Inflação Portugal        | 2019 |
| Inflação Rússia          | 2019 |
| Inflação Suécia          | 2019 |
| Inflação Suíça           | 2019 |
| Inflação Turquia         | 2019 |

Lembre-se que, ao inserir o nome dos paises no método de busca, os nomes deverão ser escritos sem utilizar caracteres especiais e sem espaços. Veja um exemplo abaixo:

Para África do Sul a entrada será:

- africa-do-sul

Para Rússia a entrada será:

- russia

Com relação as datas, caso necessário sobre datas limite e valor mínimo, consulte o site da <code>inflation</code>
