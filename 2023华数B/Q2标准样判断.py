import pandas as pd
df = pd.read_excel("2023华数B/标准样XYZ.xlsx")# 读取标准样数据
y2 = df.iloc[0:728, 0:3] 
x0 = 94.83;y0 = 100.00;z0 = 107.38# 定义初始值
y2_divided = y2 / [x0, y0, z0]# 计算除法结果
print(y2_divided)
y2_divided.columns = ['Xj/X0', 'Yj/Y0', 'Zj/Z0']
# 保存为xlsx文件，包括属性和数据
with pd.ExcelWriter("2023华数B/标准样比值.xlsx") as writer:
    y2_divided.to_excel(writer, index=False, sheet_name="Sheet1")