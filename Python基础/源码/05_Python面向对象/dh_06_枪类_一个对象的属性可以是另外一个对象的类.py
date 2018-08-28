class Gun:
    """枪类"""

    def __init__(self, model):
        #  枪的属性，型号和子弹数量
        self.model = model
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1.发射子弹前判断子弹数量
        if self.bullet_count <= 0:
            print("%s 没有子弹。。" % self.model)

            return
        # 2.发射子弹，减少数量
        self.bullet_count -= 1

        # 3.提示信息
        print("%s 突突突。。剩余子弹%d" % (self.model, self.bullet_count))


# ak47 = Gun("ak47")
# ak47.add_bullet(50)
# ak47.shoot()
