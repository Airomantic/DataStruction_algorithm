"""
面向对象设计SOLID原则solid固定
开放封闭原则:一个软件实体如类、模块和函数应该对扩展开放,对修改关。即软件实体应尽量在不修改原有代码的情况下进行扩展。
里氏替换原则:所有引用父类的地方必须能透明地使用其子类的对象。 （函数及里面的参数，在高级函数调用时都必须一样）
依赖倒置原则:高层模块不应该依赖低层模块,二者都应该依赖其抽象;（因为底层模块的变动会导致高层模块也要变动）接口是抽象（接口是比抽象类还要抽象的类）
           抽象不应该依赖细节;细节应该依赖抽象。换言之,要针对接口编程,而不是针对实现编程。（先定义一个接口，按接口的格式去写）
接口隔离原则:使用多个专门的接口,而不使用单一的总接口,即客户端不应该依赖那些它不需要的接口。
单一职责原则:不要存在多于一个导致类变更的原因。通俗的说,即一个类只负责一项职责。

设计模式分类：
创建型模式_5(5种):エ厂方法模式、抽象工厂模式、创建者模式、原型模式、单例模式
结构型模式(7种):适配器模式、桥模式、组合模式、装饰模式、外观模式、享元模式、代理模式
行为型模式(11种):解释器模式、责任链模式、命令模式、迭代器模式、中介者模式、备忘录模式、观察者模式、状态模式、策略模式、访问者模式、模板方法模式

"""
#里氏替换原则
class User:
    def show_name(self):
        pass
class VIPUser(User): #VIPUser继承User
    def show_name(self):
        pass

def show_user(u):
    res=u.show_name()

from abc import ABCMeta, abstractmethod


class LandAnimal(metaclass=ABCMeta):
    @abstractmethod
    def walk(self):
        pass
class WaterAnimal(metaclass=ABCMeta):
    @abstractmethod
    def swim(self):
        pass
class SKyAnimal(metaclass=ABCMeta):
    @abstractmethod
    def fly(self):
        pass

#实现这个接口
class Tiger(LandAnimal):
    def walk(self):
        print("老虎会走路")

class Frog(LandAnimal,WaterAnimal): #多继承
    pass
