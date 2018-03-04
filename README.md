# Inflacpy

Este é um pequeno pacote para a fácil aquisição de informações sobre inflação em diversos países. A ideia é que a informação fique disponível de forma mais rápida para análises e consultas.

Todos os dados são retirados do site: [Inflation](http://pt.inflation.eu/). Estou utilizando este site pois ele faz uma excelente junção dos mais diversos serviços. Créditos pelos dados a eles.

## Utilização

A utilização é bastante simples, há um exemplo dentro de <code>app.py</code>, porém caso você queira utilizar em seu projeto, basta importar a classe <code>Scrap</code> e utilizar o método <code>get_data</code>, com ele será possível definir o país e o tempo que deverá ser considerado na busca.

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
| Inflação África do Sul   | 2018 |
| Inflação Alemanha        | 2018 |
| Inflação Austria         | 2018 |
| Inflação Bélgica         | 2018 |
| Inflação Brasil          | 2018 |
| Inflação Canadá          | 2018 |
| Inflação Chéquia         | 2018 |
| Inflação Chile           | 2018 |
| Inflação China           | 2018 |
| Inflação Coreia do Sul   | 2018 |
| Inflação Dinamarca       | 2018 |
| Inflação Eslováquia      | 2018 |
| Inflação Eslovénia       | 2018 |
| Inflação Espanha         | 2018 |
| Inflação Estados Unidos  | 2018 |
| Inflação Estónia         | 2018 |
| Inflação Finlândia       | 2018 |
| Inflação França          | 2018 |
| Inflação Grã-Bretanha    | 2018 |
| Inflação Grécia          | 2018 |
| Inflação Holanda         | 2018 |
| Inflação Hungria         | 2018 |
| Inflação India           | 2018 |
| Inflação Indonésia       | 2018 |
| Inflação Irlanda         | 2018 |
| Inflação Islândia        | 2018 |
| Inflação Israel          | 2018 |
| Inflação Itália          | 2018 |
| Inflação Japão           | 2018 |
| Inflação Luxemburgo      | 2018 |
| Inflação México          | 2018 |
| Inflação Noruega         | 2018 |
| Inflação Polónia         | 2018 |
| Inflação Portugal        | 2018 |
| Inflação Rússia          | 2018 |
| Inflação Suécia          | 2018 |
| Inflação Suíça           | 2018 |
| Inflação Turquia         | 2018 |

Lembre-se que, ao inserir o nome dos paises no método de busca, os nomes deverão ser escritos sem utilizar caracteres especiais e sem espaços. Veja um exemplo abaixo:

<code>
Para África do Sul a entrada será:
- africa-do-sul

Para Rússia a entrada será:
- russia
</code>

Com relação as datas, caso necessário sobre datas limite e valor mínimo, consulte o site da <code>inflation</code>
