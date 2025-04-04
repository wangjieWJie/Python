import pandas as pd
import numpy as np

file_adr = "my_project/pandas_pynumb/"

df1=pd.read_excel(file_adr + '附件1.xlsx')
df2=pd.read_excel(file_adr + '附件2.xlsx')
print(df1)
print(df2)           

#按照地块类型提取名称和面积
crop_data = ['作物名称', '地块类型', '种植季次', '亩产量/斤', '种植成本/(元/亩)', '销售单价/(元/斤)']

#提取相关数据列
crop_names = crop_data['作物名称']
plot_types = crop_data['地块类型']
planting_seasons = crop_data['种植季次']
yield_per_mu = crop_data['亩产量/斤']
planting_costs = crop_data['种植成本/(元/亩)']
sale_prices = crop_data['销售单价/(元/斤)']


# 合并数据并仅保留 2023 年种植数据中的条目
# merged_data = pd.merge(planting_data_2023, crop_data, on=['作物名称', '种植季次',
# '地块类型'], how='inner')
# # 检查合并后的数据
# print('合并后的数据（前 10 行）：')
# print(merged_data.head(10))#





