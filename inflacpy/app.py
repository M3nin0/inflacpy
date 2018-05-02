import pandas as pd

from inflacpy.scrap.scrap import Scrap

if __name__ == '__main__':
    scrap = Scrap()
    _list = scrap.get_data(country='brasil')

    # Exportando em json
    _json = pd.DataFrame(_list).dropna()
    _json.to_json('../data/brasil.json')
