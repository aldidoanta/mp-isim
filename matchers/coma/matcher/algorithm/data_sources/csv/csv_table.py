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
        for column_name, column_data in self.__data.items():
            data = list(column_data.dropna().values)
            d_type = self.get_data_type(data, str(column_data.dtype))
            self.__columns[column_name] = CSVColumn(column_name, data, d_type, self.unique_identifier)
