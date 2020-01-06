
# 1.导入包，xlrd
import xlrd
# 2.创建workbook对象
book = xlrd.open_workbook("./database.xlsx")
# print(book)
# 3.sheet对象
# 索引/名称获取
# sheet = book.sheet_by_index(0)
sheet = book.sheet_by_name("会计平台")
# 4.获取行数和列数
rows = sheet.nrows  # 行数
# print(rows)
cols = sheet.ncols  # 列数
# print(cols)
# 5.读取每行的内容
for r in range(rows):
   # print(r)
   r_values = sheet.row_values(r)
   print(r_values)

# 6.读取每列的内容
for c in range(cols):
    c_values = sheet.col_values(c)
    print(c_values)
# 7.读取固定列的内容
print(sheet.cell(1,1))
