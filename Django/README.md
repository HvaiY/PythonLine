### Django  使用
---
 - **配置环境(window10) 安装pip,配置python虚拟环境**
   - 安装Python3.6 略(需要添加环境变量)
   - cmd 输入 python 查看Python版本
   - 打开资源文件 解压`pip-18.0.tar`  使用管理员打开命令窗(cmd)输入`python setup.py install` 自动安装
   - 输入`pip`查看看安装成功否
   - 安装成功后继续安装 Python虚拟环境输入`pip install virtualenv` 等待安装完成
   - 找到python安装目录并找到Scripts 添加到环境变量
   - 输入 `virtualven Test`可以创建一个叫做Test的测试虚拟环境（当前目录）
   - 我这边创建了在：C:\Windows\system32\testhai\Scripts
   - 进入该目录 运行`activate` 即可开启进入该虚拟环境
   - 退出虚拟环境 输入`deactivate`
  ---
  [点击查看MarkDown语法](https://www.jianshu.com/p/191d1e21f7ed)

  ---
|name|age|address|
:--:|:--:|:--:
大海|28|上海
小孩|29|海南

```
    function fun(){
         echo "这是一句非常牛逼的代码";
    }
    fun();
```

```flow
st=>start: 开始流程
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
```

![图片](https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=2552174933,2157022207&fm=58&bpow=950&bpoh=1425"测试图片")

---