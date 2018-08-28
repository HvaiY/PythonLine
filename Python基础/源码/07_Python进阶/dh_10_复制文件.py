# 1.打开 小文件操作
file_read = open("ReadMe")
file_write = open("Read_复件", "w")
# 2.读写

text = file_read.read()
file_write.write(text)
# 3.关闭
file_read.close()
file_write.close()

print("*" * 50)

# 大文件操作
file_read_big = open("ReadMe")
file_write_big = open("ReadMeBig复件", "w")

while True:
    text = file_read_big.readline()
    if not text:
        break
    file_write_big.write(text)

file_read_big.close()
file_write_big.close()
