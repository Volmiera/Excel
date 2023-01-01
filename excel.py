# importing the required modules
import glob
import os
import sys
from copy import copy

import numpy as np

# outrow_idx = 0
# for f in xlsfiles:
#     # This is all untested; essentially just pseudocode for concept!
#     insheet = openpyxl.open_workbook(cwd+ "\\" +f).sheets()[0]
#     for row_idx in xrange(insheet.nrows):
#         for col_idx in xrange(insheet.ncols):
#             outsheet.write(outrow_idx, col_idx, 
#                            insheet.cell_value(row_idx, col_idx))
#         outrow_idx += 1
# wkbk.save(r'C:\combined.xls')
import pandas as pd

# import xlrd
# import xlwt
from openpyxl import Workbook, load_workbook

print(os.getcwd())
os.chdir('C:\\Users\\vovch\\Desktop\\excel_n')
print(os.getcwd())
xl_files = glob.glob('*.xlsx')
combined = pd.DataFrame()
for xl_file in xl_files:
    # Создать объект ExcelFile
    xl_file_obj = pd.ExcelFile(xl_file)
    # Цикл по листам
    for sheet_name in xl_file_obj.sheet_names:
        # Прочитать нужный лист книги
        excel_n = pd.read_excel(xl_file_obj,
                             sheet_name=sheet_name)
        # Создадать столбец с названием книги
        excel_n['workbook'] = xl_file
        # Создать столбец с названием листа
        excel_n['sheet'] = sheet_name
        # Дописать в датафрейм combined
        combined = combined.append(excel_n)

combined.to_excel('sales_combined.xlsx',
                  index=False)



cwd = os.path.abspath('C:\\Users\\vovch\\Desktop\\excel_n')
files = os.listdir(cwd)


# all_data = pd.DataFrame()
# for file in files:
#     if file.endswith('.xlsx'):
#         df = pd.read_excel(cwd+"\\"+file)
#         all_data = all_data.append(df, ignore_index=True)
# all_data.head()
# status = pd.read_excel(cwd+'\\'+'test.xlsx')
# all_data_st = pd.merge(all_data, status, how='left')
# all_data_st.head()
# all_data_st.to_excel('res.xlsx')


print(os.getcwd())
os.chdir('C:\\Users\\vovch\\Desktop\\excel_n')
print(os.getcwd())
xl_files = glob.glob('*.xlsx')
combined = pd.DataFrame()
for xl_file in xl_files:
    # Создать объект ExcelFile
    xl_file_obj = pd.ExcelFile(xl_file)
    # Цикл по листам
    for sheet_name in xl_file_obj.sheet_names:
        # Прочитать нужный лист книги
        excel_n = pd.read_excel(xl_file_obj,
                             sheet_name=sheet_name)
#         # Создадать столбец с названием книги
#         excel_n['workbook'] = xl_file
#         # Создать столбец с названием листа
#         excel_n['sheet'] = sheet_name
        # Дописать в датафрейм combined
        combined = combined.append(excel_n)

combined.to_excel('sales_combined.xlsx',
                  index=False)

folder = os.chdir('C:\\Users\\vovch\\Desktop\\excel_n')  #папка с файлами
xl_files = glob.glob('*.xlsx')
all_file_frames = [] #сюда будем добавлять прочитанную таблицу 
for f in xl_files:
    print('Reading %s'%f)
    tab = pd.read_excel(f)
    all_file_frames.append(tab)
all_frame = pd.concat(all_file_frames,axis=0) #  axis=0 если нужно добавить таблицу снизу и axis=1 если нужно слева
all_frame.to_excel('final_file.xlsx') #получим файл final_file.xlsx в os.getcwd()






# cwd = os.path.abspath('C:\\Users\\vovch\\Desktop\\excel_n')
# # files = os.listdir(cwd)
# wkbk = xlwt.Workbook()
# outsheet = wkbk.add_sheet('Sheet1')
#  #папка с файлами
# folder = os.chdir('C:\\Users\\vovch\\Desktop\\excel_n')  #папка с файлами
# xlsfiles = glob.glob('*.xlsx')

import openpyxl

folder = os.chdir('C:\\Users\\vovch\\Desktop\\excel_n')  #папка с файлами
xl_files = glob.glob('*.xlsx')


all_data = pd.DataFrame()
for f in xl_files:
   df = pd.read_excel(f)
   all_data = all_data.append(df, ignore_index=True)
   all_data.to_excel('final_file.xlsx') 
