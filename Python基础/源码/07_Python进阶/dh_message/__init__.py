from . import send_message
from . import receive_message
# 搜索当前目录的包，引入模块到这里 其它项目引入该包名就可以引入所有的模块
# __init__.py 文件很重要，不然无法搜索到对应的模块。本质就是模块初始化(模块生成导入口)
