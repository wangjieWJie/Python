# 1、 类一般首字母大写
class Zombie:
    # 类似于C++中的构造函数：
    # 方法__init__()是一个特殊的方法，每当你根据Zombie类创建新实例时，Python都会自动运行它
    def __init__(self, name, speed, health, ATK):
        self.speed = speed
        self.health = health
        # 给属性指定默认值（默认构造函数）,也可以在上面的括号中的形参后面写上等于几，来进行初始化（提供默认值）
        self.ATK = 10

    # 上述方法中的形参 self 必不可少，而且必须位于其他形参的前面
    # 因为Python调用这个__init__()方法来创建Dog实例时，将自动传入实参self。
    # 每个与类相关联的方法调用都自动传递实参self，它是一个指向实例本身的引用，让实例能够访问类中的属性和方法。
    # 以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量
    # 这种可通过实例访问的变量称为属性。

    def hurted(self, ATKed):
        self.health -= ATKed

    # 这是自己创建的方法，在这个方法中我们不需要额外的参数信息，所以我们只需要写一个形参 self 即可
    # 使用了形参 self 的方法可以直接访问之前定义的“属性”（以self为前缀的变量)
    # 如果没有形参 self ，则在此方法中，无法访问到之前创建的所有变量

    def excited(self):
        self.speed += 5
        self.ATK = 20
        print("攻击力为：" + str(self.ATK))

    def show(self):
        print("当前血量：" + str(self.health))
        print("当前攻击力：" + str(self.ATK))
        print("当前速度：" + str(self.speed))


# 根据类创建实例(和C++创建实例相同)
newspaper_zombie = Zombie("newspaper_zombie", 20, 100, 10)

# 若想访问实例的属性，则应使用句点表示法(但是只能访问属性（以self为前缀的的变量）)
print("血量：" + str(newspaper_zombie.health))
# 调用方法也是用句点表示法
newspaper_zombie.excited()


# 修改属性的值
# 1.1、可以通过句点直接修改想要修改的值
newspaper_zombie.health = 80
# 1.2、通过方法修改
newspaper_zombie.excited()
newspaper_zombie.hurted(20)

newspaper_zombie.show()


# 2、继承
class Palnt_Zombie(Zombie):
    # 可以认为 Plant_zombie 是Zombie 的一个特殊版本，因为这个植物僵尸即吃植物也攻击僵尸，
    # 但是他的本质还是一个僵尸，所以我认为他应该是zombie的一个特殊版本，有问题吗？
    # 在这个例子中， Zombie 被称为父类 ，让这个 新类 Palnt_Zombie 被称为子类
    # 子类会继承父类的所有的属性和方法
    def __init__(self, name, speed, health, ATK, frendly):
        # 方法__init__()接受创建Car实例所需的信息
        super().__init__(name, speed, health, ATK)
        # super()是一个特殊函数，帮助Python将父类和子类关联起来。
        # 这行代码让Python调用 Palnt_Zombie 的父类的方法__init__()，让ElectricCar实例包含父类的所有属性。
        # 父类也称为超类（superclass），名称super因此而得名。

        # 给子类定义新的属性和方法
        self.frendly = frendly
        self.frendly_deegre = 0
        # 像这样，你可以直接在上面最开始的初始化的括号的后面写上你要添加的属性。
        # 或者你也可以在 super() 函数下面写上具有初始值的新属性
        # 对于方法，就和任何的类的方法的定义相同了，随便定义
        # 所以，和 zombie 共有的属性或者方法就写到 zombie 里面去，特有的就写在这个子类里面

    # 重写父类的方法
    # 如果子类不应该具有和父类一样的方法，那么就可以重写他
    # 只需要写一个和父类某方法名称一致的方法即可覆盖父类的方法
    # 因为这种僵尸不会兴奋，所以我们让 excited 这个方法修改它的友好程度
    def excited(self, mood):
        self.frendly_deegre += mood
        if self.frendly_deegre >= 0:
            self.frendly = True
        elif self.frendly_deegre < 0:
            self.frendly = False


# 导入类和导入函数是一样的，可以通过直接导入模块来导入类，也可以单独导入一个或者几个类
# 和函数一样，当你通过 from 导入，你的模板可以直接使用，而不需要句点表示法
# 但是当你导入了一整个模块,你就需要使用句点表示法,
# 但是这种方法也有好处,那就是模块中的函数和类永远都不会和你现在的文件中的函数和类发生冲突

# 另: 你可以将一个模块导入进另一个模块,充分模块化


# python 标准库:
#
# 有很多实用的类能大大提高代码效率
# 比如 collections 中的 OrderedDict 类, 他的使用完全类似于字典, 但是不同的是,他可以记录键值对的顺序

from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages["jen"] = "python"
favorite_languages["sarah"] = "c"
favorite_languages["edward"] = "ruby"
favorite_languages["phil"] = "python"

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")


# Python Module of the Week：要了解Python标准库，一个很不错的资源是网站Python Module of the Week。
# 请访问http://pymotw.com/并查看其中的目录，在其中找一个你感兴趣的模块进行探索。


# 最后请注意 关于 类的写法的 约定：
# 类名应采用驼峰命名法，即将类名中的每个单词的首字母都大写，而不使用下划线。
# 实例名和模块名都采用小写格式，并在单词之间加上下划线。
# 对于每个类，都应紧跟在类定义后面包含一个文档字符串。这种文档字符串简要地描述类的功能，并遵循编写函数的文档字符串时采用的格式约定。
# 每个模块也都应包含一个文档字符串，对其中的类可用于做什么进行描述。
# 可使用空行来组织代码，但不要滥用。
# 在类中，可使用一个空行来分隔方法；而在模块中，可使用两个空行来分隔类。
# 需要同时导入标准库中的模块和你编写的模块时，先编写导入标准库模块的import语句，再添加一个空行，然后编写导入你自己编写的模块的import语句。
# 在包含多条import语句的程序中，这种做法让人更容易明白程序使用的各个模块都来自何方
