file = open("ReadMe")

while True:
    # 逐行读取 ，可以使用循环读取所有的文档内容
    text = file.readline()
    if not text:
        break
    print(text)

file.close()
