import pandas as pd

df = pd.read_excel(r'input\sample.xlsx')

df.to_excel(r'output\excel xlsx - xlsxwriter.xlsx', engine='xlsxwriter', index=False)
df.to_excel(r'output\excel xlsx - openpyxl.xlsx', engine='openpyxl', index=False)
df.to_excel(r'output\excel xls - xlwt.xls', engine='xlwt', index=False)
