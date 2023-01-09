import pandas as pd


iris = pd.read_csv('data/iris.csv')

grouped = iris.groupby('variety')

with pd.ExcelWriter('output/iris2.xlsx') as writer:
    for label, group in grouped:
        group.to_excel(writer, sheet_name=label)


