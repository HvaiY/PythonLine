import dh_06_枪类_一个对象的属性可以是另外一个对象的类


class Soldier:
    def __init__(self, name):
        self.name = name
        self.gun = dh_06_枪类_一个对象的属性可以是另外一个对象的类.Gun("M4")
        # 也可以self.gun = None ,再写个方法由外边赋值
        # None 一般在不知道属性的类型的时候可以这样使用


xuSanDuo = Soldier("许三多")
xuSanDuo.gun.add_bullet(30)

xuSanDuo.gun.shoot()
