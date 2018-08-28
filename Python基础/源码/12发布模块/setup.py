from distutils.core import setup

setup(name="dh_messages",  # 包名
      version="1.0",
      description="大海的发送和接收信息的模块",
      long_description="大海的完整的发送和接受信息的模块",
      author="大海",
      author_email="337646685@qqcom",
      url="www.dahai.com",
      py_modules=["dh_messages.send_message",
                 "dh_messages.receive_message"])
# 新建setup.py文件 然后输入上面的内容
# 在终端切换到 12发布模块 目录
# 然后输入命令python3 setup.py build
#  然后再 生成发布压缩包 命令python setup.py sdist
# 即可.
