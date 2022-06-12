"""
软件危机：就是没有提前设计，乱七八糟 ，解决-软件过程（面向对象），用类来分功能，面向过程做不了太大，人理解不了
<<可复用面向对象软件的基础>>
面向对象的三大特性（递进关系）：封装 -> 继承 -> 多态
python本身是门多态语言，不需要考虑
接口：若干抽象方法的集合 加新功能 （敲门，开门，走入，关门）
作用:限制实现接口的类必须按照接口给定的调用方式实现，这些方法;对高层模块隐藏了类的内部实现。
    Alipay，WeChatpay就是低层
python 跨平台性 ，无论是在macOS和windows或Linux间如何切换编译，无需修改任何代码，都能在当前平台运行成功
"""
from abc import ABCMeta,abstractmethod
#抽象类 如果没有被实现就是抽象方法，实现类就没有抽象方法类（有内容把它覆盖了）


#第二种实现方法
"""接口，定义方法（要求长得一样），不管实现"""
class Payment(metaclass=ABCMeta):
    #abstract class
    @abstractmethod
    def pay(self,money):
        pass

class Alipay(Payment):
    def pay(self,money):
        print("支付宝支付%d元"% money)

class WeChatpay(Payment):
    def pay(self,money):
        print("微信支付%d元"% money)

p=Alipay()
p.pay(100)