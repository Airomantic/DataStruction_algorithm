"""
简单工厂模式，把好几种商品的模式集中到一个工厂里，需要拆开，一个工厂生产一个产品
内容:定义一个用于创建对象的接口(工厂接口),让子类決定实例化哪一个产品类
角色:
1 抽象工厂角色( Creator)
2 具体工厂角色( Concrete Creator)
3 抽象产品角色( Product)
4 具体产品角色( Concrete Product)
优点
1 每个具体产品都对应一个具体工厂类,不需要修改工厂类代码
2 隐藏了对象创建的实现细节
缺点
1 每增加一个具体产品类,就必须增加一个相应的具体工厂类

"""
from abc import ABCMeta,abstractmethod
class Payment(metaclass=ABCMeta):
    #abstract class
    @abstractmethod
    def pay(self,money):
        pass

class Alipay(Payment):
    def __init__(self,use_huabei=False):
        self.use_huabei=use_huabei

    def pay(self,money):
        if self.use_huabei: #当传入参数是True时
            print("花呗支付%d元"% money)
        else:
            print("支付宝余额支付%d元."% money)

class WeChatpay(Payment):
    def pay(self,money):
        print("微信支付%d元"% money)

class Bankpay(Payment):
    def pay(self,money):
        print("银联（银行卡）支付%d元"% money)

class PaymentFactory:
    @abstractmethod #工厂类的接口
    def creat_payment(self):
        pass

class AlipayFactory(PaymentFactory):
    def creat_payment(self):
        return Alipay() #调用函数

class WechatPayFactory(PaymentFactory):
    def creat_payment(self):
        return WeChatpay() #调用函数

class HuabeiFactory(PaymentFactory):
    def creat_payment(self):
        return Alipay(use_huabei=True) #还是调用Alipey 只是参数不同

class BankPayFactory(PaymentFactory):
    def creat_payment(self):
        return Bankpay() #调用函数

pf=BankPayFactory() #只需改工厂就行了
p=pf.creat_payment()
p.pay(100)