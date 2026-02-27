import pandas as pd
# import openpyxl

def get_data():
    data_os = pd.read_excel("../data/titanic3.xls", engine="xlrd")
    return data_os


# if __name__ == "__main__":
#     get_data()