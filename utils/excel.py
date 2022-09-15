import pandas as pd


class Excel:
    @classmethod
    def parse_to_pandas(cls, file):
        return pd.read_excel(file, engine="openpyxl")

    @classmethod
    def parse_temps_to_pandas(cls, file):
        sheets = pd.read_excel(file, engine="openpyxl", sheet_name=None)
        sheets_names = list(sheets.keys())
        sheet_1_name = sheets_names[0]
        sheet_1 = sheets[sheet_1_name]
        if len(sheets_names) > 1:
            sheet_2_name = sheets_names[1]
            sheet_2 = sheets[sheet_2_name]
        else:
            sheet_2_name = None
            sheet_2 = None
        return sheet_1_name, sheet_1, sheet_2_name, sheet_2


