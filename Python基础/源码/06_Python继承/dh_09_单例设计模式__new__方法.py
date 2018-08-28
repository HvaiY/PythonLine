# __new__为对象分配空间，返回对象引用
class MusicPlayer(object):
    # 创建对象时，new方法会自动调用   并必须返回方法的引用
    def __new__(cls, *args, **kwargs):
        # 创建对象时，new方法会自动调用
        print("创建对象，分配空间")
        instant = super().__new__(cls)  # 调用父类的方法
        return instant

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()

print(player)
