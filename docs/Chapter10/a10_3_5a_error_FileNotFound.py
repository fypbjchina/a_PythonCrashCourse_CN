# a10_3_5a_error_FileNotFound.py
# FileNotFoundError是Python找不到要打开的文件时创建的异常

filename = 'alice.txt' # book/alice.txt

with open(filename, encoding='utf-8') as f:
    contents =f.read()