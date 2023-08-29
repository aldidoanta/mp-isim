from typing import List

from .csv_column import CSVColumn
from ..base_column import BaseColumn
from ..base_table import BaseTable


class CSVTable(BaseTable):

    def __init__(self, data: any, name: str):
        self.__table_name = name
        self.__columns = dict()
        self.__data = data

    @property
    def unique_identifier(self) -> str:
        return self.__table_name

    @property
    def name(self) -> str:
        return self.__table_name

    def get_columns(self) -> List[BaseColumn]:
        if not self.__columns:
            self.__get_columns_from_csv()
        return list(self.__columns.values())

    def get_data(self) -> any:
        return self.__data

    @property
    def is_empty(self) -> bool:
        return self.__data.empty

    def __get_columns_from_csv(self):
        # Current assumption: the CSV file only uses commas (,) as delimiter
        # To implement this method using Pandas DataFrame as input instead of CSV, see the original implementation
        # https://github.com/delftdata/valentine/blob/29be01ba1a00b389a359f856ff9b02c2bc93740e/valentine/data_sources/dataframe/dataframe_table.py#L37C5-L41
        column_names = list(filter(None, self.__data.split(','))) # use filter() to remove empty strings
        for column_name in column_names:
            data = list()
            d_type = 'varchar'
            self.__columns[column_name] = CSVColumn(column_name, data, d_type, self.unique_identifier)
