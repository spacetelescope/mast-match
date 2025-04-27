import pandas as pd

def read_xl(filename="MAST Match Card List.xlsx"):
    sheet = pd.read_excel(filename)
    obs = sheet["Observation Cards"]
    return obs