class MusicPlayer(object):
    instant = None

    def __new__(cls, *args, **kwargs):
        if cls.instant is None:
            cls.instant = super().__new__(cls)

        return cls.instant

    def __init__(self, name):
        self.name = name
        print("%s初始化播放器" % self.name)


player1 = MusicPlayer("mp3")

player2 = MusicPlayer("mp4")

print(player1)
print(player2)

print("*" * 50)


# 初始化动作限定为一次（我们无法限制初始化，但是初始化的动作可以限制）

class MusicPlayer2(object):
    instant = None
    init_flag = False

    def __new__(cls, *args, **kwargs):
        if cls.instant is None:
            cls.instant = super().__new__(cls)

        return cls.instant

    def __init__(self, name):

        if self.init_flag:  # 果然是True 代表已经初始化了 ，那么return
            return
        self.name = name
        print("%s初始化播放器" % self.name)
        self.init_flag = True  # 没有初始化过，就初始化一次之后标记为True ，代表已初始化


player111 = MusicPlayer2("mp3")

player222 = MusicPlayer2("mp4")

print(player111)  # 你会发现 对象的地址一样的，但是初始化的动作只有一次
print(player222)
