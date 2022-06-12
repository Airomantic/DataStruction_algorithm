"""
内容:不直接向客户端暴露对象创建的实现细节,而是通过一个工厂类来负责创建产品类的实例
角色:
工厂角色( Creator)
抽象产品角色( Product)
具体产品角色( Concrete Product)
优点
    1 隐藏了对象创建的实现细节
    2 客户端不需要修改代码
缺点:
    1 违反了单一职责原则,将创建逻辑几种到一个工厂类里
    2 当添加新产品时,需要修改工厂类代码,违反了开闭原则

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

class PaymentFactory:
    def creat_payment(self,method):
        if method=="alipay":
            return Alipay()
        elif method=="wechat":
            return WeChatpay()
        elif method=='huabei':
            return Alipay(use_huabei=True)
        else:
            raise TypeError("No such payment named %s" % method)

#隐藏内部类的实现
pf = PaymentFactory()
p=pf.creat_payment("huabei")
p.pay(100)