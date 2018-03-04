import pandas as pd
import sqlite3
from scrap.scrap import Scrap

if __name__ == '__main__':
    scrap = Scrap()
    _list = scrap.get_data(country='brasil')

    # Exportando em json
    pd.DataFrame(_list).to_json('../data/brasil.json')
