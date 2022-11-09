import re
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns

# table = pd.read_excel('./护腰枕品牌数据2016-2017.xlsx', sheet_name='data')
# table['年月'] = pd.to_datetime(table['年月'])
# new_table = table.set_index('年月')
# data2016 = new_table.loc['2016']
# data2017 = new_table.loc['2017']
# data2016.to_excel('data2016.xlsx')
# data2017.to_excel('data2017.xlsx')
# for root, dirs, files in os.walk('./'):
#     for file in files:
#         if file.startswith('data'):
#             data = file.split('.')[0]
#             year = re.search(r'(\d+)', file).group()
#             print(data, year, file)

# table = pd.read_excel('./护腰枕品牌数据2016-2017.xlsx', sheet_name='data')
# table['年月'] = pd.to_datetime(table['年月'])
# new_table = table.set_index('年月')
# data = new_table.resample('Y')['成交量'].sum()
# plt.figure(figsize=(10, 20))
# print(plt.bar(x=data.index, height=data.values))
# print(sns.barplot(x='成交量', y='名称', estimator=sum, data=new_table))
# print(new_table.sort_values('成交量', ascending=False).head()[['名称', '成交量']])

print(np.random.randint(10, 100))
