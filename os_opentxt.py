import os
file_path = "data/sheetGIT.txt"

with open(file_path, 'r' ,encoding = "utf-8") as file:
    file_content = file.read() #讀文件
    print(file_content) #印出文件內容